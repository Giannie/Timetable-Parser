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
    def __init__(self, term_start=None, half_start=None, half_end=None, term_end=None):
        if len([v for v in locals().values() if v is None]) > 1:
            raise TypeError('Must supply term dates or an xml file containing them')
        for i in range(len(day_list)):
            if i <= 4:
                offset = i
            else:
                offset = i + 2
            self[day_list[i]] = [term_start + timedelta(days=offset)]
            half_length = half_end - term_start
            if math.ceil(half_length.days/7) % 2 == 1:
                if i <= 4:
                    offset = i + 7
                else:
                    offset = i - 5
            self[day_list[i]].append(half_start + timedelta(days=offset))
        self['half_end'] = half_end + timedelta(days=1)
        self['term_end'] = term_end + timedelta(days=1)
