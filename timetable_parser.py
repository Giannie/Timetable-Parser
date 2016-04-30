from datetime import time, datetime, timedelta
import xml.etree.ElementTree as et
import icalendar
import math
import os
import re


days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
weeks = ["A", "B"]

day_list = []

for week in weeks:
    for day in days:
        day_list.append(week + day)

day_struct = [[time(8, 30), time(8, 40)],
              [time(8, 45), time(9, 35)],
              [time(9, 40), time(10, 30)],
              [time(10, 30), time(10, 50)],
              [time(10, 50), time(11, 10)],
              [time(11, 15), time(12, 5)],
              [time(12, 10), time(13, 0)],
              [time(13, 0), time(13, 25)],
              [time(13, 25), time(14, 5)],
              [time(14, 15), time(15, 5)],
              [time(15, 10), time(16, 0)],
              [time(16, 10), time(17, 0)]]


def LessonDict(group="", room="", period=None, cat=""):
    return {"group": group, "room": room, "period": period, "type": cat}

def PeriodDict(title, start, end):
    return {"title": title, "start": start, "end": end}

class TimeTableClass(list):
    def __init__(self, xml_tag):
        super(TimeTableClass, self).__init__()

        period_count = 0

        for item in xml_tag[4:16]:
            row = []
            for lesson_xml in item[1:]:
                if len(lesson_xml) > 1 and lesson_xml[0].text != 'Blanking Code':
                    if lesson_xml[1].text:
                        room_info = lesson_xml[1].text.split()
                        if len(room_info) > 1:
                            room = ''
                            for s in room_info[:-1]:
                                room += s
                            cat = room_info[-1]
                        else:
                            room = ''
                            cat = ''
                    else:
                        room = ''
                        cat = ''
                    lesson = LessonDict(group=lesson_xml[0].text, room=room, period=self.day_struct[period_count], cat=cat)
                else:
                    lesson = LessonDict()
                row.append(lesson)
            self.append(row)
            period_count += 1

    def column(self, number):
        c = [self[i][0] for i in range(len(self))]
        return c

    def gen_calendar(self, term_start, half_end, half_start, term_end):
        cal = icalendar.Calendar()
        cal.add('prodid', '-//Timetable Calendar//')
        cal.add('version', '2.0')
        end_date = half_end
        for row in self:
            start_date = term_start
            for lesson in row:
                if lesson["group"]:
                    cal.add_component(self.gen_ical_event(lesson, start_date, end_date))
                if start_date.isoweekday() == 5:
                    start_date += timedelta(days=3)
                else:
                    start_date += timedelta(days=1)
        half_length = half_end - term_start
        if math.ceil(half_length.days / 7) % 2:
            b_start = True
        else:
            b_start = False
        end_date = term_end
        for row in self:
            start_date = half_start
            if b_start:
                row = row[5:] + row[:5]
            for lesson in row:
                if lesson["group"]:
                    cal.add_component(self.gen_ical_event(lesson, start_date, end_date))
                if start_date.isoweekday() == 5:
                    start_date += timedelta(days=3)
                else:
                    start_date += timedelta(days=1)
        return cal

    def gen_ical_event(self, lesson, start_date, end_date):
        event = icalendar.Event()
        event.add('summary', lesson['group'])
        start_date = start_date.replace(hour=lesson['period']['start'].hour, minute=lesson['period']['start'].minute)
        event.add('dtstart', start_date)
        start_date = start_date.replace(hour=lesson['period']['end'].hour, minute=lesson['period']['end'].minute)
        event.add('dtend', start_date)
        event['location'] = icalendar.vText(lesson["room"])
        event.add('rrule', {'freq': 'weekly', 'interval': 2, 'until': end_date + timedelta(days=1)})
        event.add('categories', [lesson['type'], lesson['group']])
        return event

    def write_calendar(self, filepath, term_start, half_end, half_start, term_end):
        with open(filepath, 'wb') as f:
            f.write(self.gen_calendar(term_start, half_end, half_start, term_end).to_ical())

class TimeTableGroup(dict):
    def __init__(self, xml_file, dates):
        super(TimeTableGroup, self).__init__()
        self.dates = dates
        tree = et.parse(xml_file)
        root = tree.getroot()
        timetablesData = root[0].find("TimeTables")
        for timetable in timetablesData.findall("TimetableData"):
            teacher_name = re.sub("Timetable  - ", "", timetable.find("ResourceName").text)
            self[teacher_name] = []
            row_count = 0
            for row in timetable.findall("TableRow"):
                period_start, period_end = day_struct[row_count]
                column_count = 0
                for column in row.findall("CellData")[1:]:
                    if len(column) > 0 and column[0].text != "Blanking Code":
                        day = day_list[column_count]
                        group = column[0].text
                        room_info = column[1].text.strip("-")
                        if len(room_info) > 0:
                            room_info = room_info.split()
                            subject = room_info[-1]
                            room = room_info[0]
                            for add_room in room_info[1:-1]:
                                room += " " + add_room
                        else:
                            room = ''
                            subject = ''
                        lesson_dict = {"day": day, "start": period_start, "end": period_end, "group": group, "room": room, "subject": subject}
                        for event in self.generate_event(lesson_dict, dates):
                            self[teacher_name].append(event)
                    column_count += 1
                row_count += 1
                if row_count > 11:
                    break

    def generate_event(self, lesson, dates):
        events = []
        for i in range(2):
            event = icalendar.Event()
            start_date = dates[lesson["day"]][i]
            start_date = start_date.replace(minute=lesson["start"].minute, hour=lesson["start"].hour)
            end_date = start_date.replace(minute=lesson["end"].minute, hour=lesson["end"].hour)
            if i == 0:
                until = dates["half_end"]
            else:
                until = dates["term_end"]
            event.add('summary', lesson['group'])
            event.add('location', lesson['room'])
            event.add('dtstart', start_date)
            event.add('dtend', end_date)
            event.add('rrule', {'freq': 'weekly', 'interval': 2, 'until': until})
            event.add('categories', [lesson['subject'], lesson['group'], "auto-generated"])
            events.append(event)
        return events

    def generate_calendars(self, path):
        for name in self.keys():
            cal = icalendar.Calendar()
            cal.add('prodid', '-//Timetable Calendar//')
            cal.add('version', '2.0')
            for event in self[name]:
                cal.add_component(event)
            name = re.sub('[\\/:"*?<>|()]+','',name)
            with open(os.path.join(path, name + '.ics'), 'wb') as f:
                f.write(cal.to_ical())

class timetableDates(dict):
    def __init__(self, term_start=None, half_start=None, half_end=None, term_end=None, xml_date_file=None):
        if xml_date_file:
            # Fill in code parsing for xml file containing term dates here
            pass
        elif len([v for v in locals().values() if v is None]) > 1:
            raise TypeError('Must supply term dates or an xml file containing them')
        for i in range(len(day_list)):
            if i <= 4:
                offset = i
            else:
                offset = i + 2
            self[day_list[i]] = [term_start + timedelta(days=offset), half_start + timedelta(days=offset)]
        self['half_end'] = half_end + timedelta(days=1)
        self['term_end'] = term_end + timedelta(days=1)
