from datetime import time, datetime, timedelta
import xml.etree.ElementTree as et
import icalendar
import math
import os

xml_file = "/path/to/file.xml"

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
weeks = ["A", "B"]

day_list = []

for week in weeks:
    for day in days:
        day_list.append(day + week)

def LessonDict(group="", room="", period=None, cat=""):
    return {"group": group, "room": room, "period": period, "type": cat}

def PeriodDict(title, start, end):
    return {"title": title, "start": start, "end": end}

class TimeTableClass(list):
    def __init__(self, xml_tag):
        super(TimeTableClass, self).__init__()

        self.day_struct = [PeriodDict("SRG", time(8, 30), time(8, 40)),
              PeriodDict("S1", time(8, 45), time(9, 35)),
              PeriodDict("S2", time(9, 40), time(10, 30)),
              PeriodDict("SB1", time(10, 30), time(10, 50)),
              PeriodDict("SB2", time(10, 50), time(11, 10)),
              PeriodDict("S3", time(11, 15), time(12, 5)),
              PeriodDict("S4", time(12, 10), time(13, 0)),
              PeriodDict("SL1", time(13, 0), time(13, 25)),
              PeriodDict("SL2", time(13, 25), time(14, 5)),
              PeriodDict("S5", time(14, 15), time(15, 5)),
              PeriodDict("S6", time(15, 10), time(16, 0)),
              PeriodDict("SED", time(16, 10), time(17, 0))]

        period_count = 0

        for item in xml_tag[4:16]:
            row = []
            for lesson_xml in item[1:]:
                if len(lesson_xml) > 1 and lesson_xml[0].text != 'Blanking Code':
                    room_info = lesson_xml[1].text.split()
                    if len(room_info) > 1:
                        if room_info[0] == 'ICT':
                            room = room_info[0] + room_info[1]
                        else:
                            room = room_info[0]
                        cat = room_info[-1]
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
        event.add('rrule', {'freq': 'weekly', 'interval': 2, 'until': end_date})
        event.add('categories', lesson['type'])
        return event

    def write_calendar(self, filepath, term_start, half_end, half_start, term_end):
        with open(filepath, 'wb') as f:
            f.write(self.gen_calendar(term_start, half_end, half_start, term_end).to_ical())

class TimeTableGroup(dict):
    def __init__(self, xml_file):
        super(TimeTableGroup, self).__init__()
        tree = et.parse(xml_file)
        root = tree.getroot()
        timetables_tag = root[0][1]
        for xml_tag in timetables_tag:
            timetable = TimeTableClass(xml_tag)
            name = xml_tag[1].text
            self[name] = timetable
    
    def generate_calendars(self, term_start, half_end, half_start, term_end, path=''):
        for name, timetable in self.iteritems():
            timetable.write_calendar(os.path.join(path, name + '.ics'), term_start, half_end, half_start, term_end)
