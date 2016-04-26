from datetime import time, datetime
import xml.etree.ElementTree as et

xml_file = "/path/to/file.xml"

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
weeks = ["A", "B"]

day_list = []

for week in weeks:
    for day in days:
        day_list.append(day + week)

def LessonDict(group="", room=""):
    return {"group": group, "room": room}

def PeriodDict(title, start, end):
    return {"title": title, "start": start, "end": end}

class TimeTableClass(list):
    def __init__(self, xml_file):
        super(TimeTableClass, self).__init__()
        tree = et.parse(xml_file)
        root = tree.getroot()
        
        day_struct = [PeriodDict("SRG", time(8, 30), time(8, 40)),
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
        
        for item in root[0][1][0][4:16]:
            row = []
            for lesson_xml in item[1:]:
                if len(lesson_xml) > 1:
                    lesson = LessonDict(group=lesson_xml[0].text, room=lesson_xml[1].text)
                else:
                    lesson = LessonDict()
                row.append(lesson)
            self.append(row)
    def column(self, number):
        c = [self[i][0] for i in range(len(self))]
        return c
