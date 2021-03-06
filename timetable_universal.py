import timetable_parser as tp
import sys
import datetime
import threading
import os
import configparser

# from PyQt5 import QtGui, QtCore, QtWidgets
# import qt5_layout as qt_layout

from PyQt4 import QtGui, QtCore
from PyQt4 import QtGui as QtWidgets
import qt_layout

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath('.')
    return os.path.join(base_path, relative_path)

with open(resource_path("style.qss"), 'r') as f:
    style = f.read()


class TimetableApp(QtWidgets.QMainWindow, qt_layout.Ui_MainWindow):
    def __init__(self, parent=None):
        super(TimetableApp, self).__init__(parent)
        self.setupUi(self)
        self.date_edit_list = [self.term_start_edit, self.half_end_edit, self.half_start_edit, self.term_end_edit]
        for index in range(len(self.date_edit_list)):
            date_edit = self.date_edit_list[index]
            date_edit.setDate(QtCore.QDate.currentDate())
            date_edit.calendarWidget().setFirstDayOfWeek(1)
            date_edit.dateChanged.connect(self.lambdaGen(index))
            cal = QStyledCalendar()
            cal.setMinimumHeight(200)
            cal.setFirstDayOfWeek(1)
            cal.setDayColor(6, "gray")
            cal.setDayColor(7, "gray")
            cal.setDirectionIcons(resource_path("icons/left-arrow.png"), resource_path("icons/right-arrow.png"))
            cal.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
            date_edit.setCalendarWidget(cal)
            if index > 0:
                date_edit.setMinimumDate(QtCore.QDate.currentDate())

        self.xml_choice_button.clicked.connect(self.selectXMLFile)
        self.target_choice_button.clicked.connect(self.selectTarget)
        self.genCalButton.clicked.connect(self.generateCalendars)
        self.dateFileButton.clicked.connect(self.selectDateFile)
        self.quitButton.clicked.connect(self.close)
        self.first_run = True

    def updateDates(self, index=0):
        if index < 3:
            self.date_edit_list[index + 1].setMinimumDate(self.date_edit_list[index].date())

    def lambdaGen(self, i):
        return lambda: self.updateDates(i)

    def selectXMLFile(self):
        self.xml_line_edit.setText(QtWidgets.QFileDialog.getOpenFileName())

    def selectTarget(self):
        self.target_line_edit.setText(QtWidgets.QFileDialog.getExistingDirectory())

    def selectDateFile(self):
        self.selectDates(QtWidgets.QFileDialog.getOpenFileName())

    def selectDates(self, filename):
        if filename and filename[0]:
            config = configparser.ConfigParser()
            config.read(filename)
            choices = config.sections()
            term, ok = QtWidgets.QInputDialog.getItem(self, "Select Term", "Select term: ", choices, 0, False)
            if ok:
                term_choice = config[term]
                self.term_start_edit.setDate(QtCore.QDate.fromString(term_choice["term_start"], "dd'/'MM'/'yyyy"))
                self.half_end_edit.setDate(QtCore.QDate.fromString(term_choice["half_end"], "dd'/'MM'/'yyyy"))
                self.half_start_edit.setDate(QtCore.QDate.fromString(term_choice["half_start"], "dd'/'MM'/'yyyy"))
                self.term_end_edit.setDate(QtCore.QDate.fromString(term_choice["term_end"], "dd'/'MM'/'yyyy"))

    def generateCalendars(self):
        target = self.target_line_edit.text()
        xml_file = self.xml_line_edit.text()
        term_start = datetime.datetime.combine(self.term_start_edit.date().toPyDate(), datetime.time())
        half_end = datetime.datetime.combine(self.half_end_edit.date().toPyDate(), datetime.time())
        half_start = datetime.datetime.combine(self.half_start_edit.date().toPyDate(), datetime.time())
        term_end = datetime.datetime.combine(self.term_end_edit.date().toPyDate(), datetime.time())
        print(xml_file)
        if not(os.path.isfile(xml_file)):
            self.workLabel.setText("XML file not found")
        elif not(os.path.isdir(target)):
            self.workLabel.setText("Target directory not found")
        else:
            self.workLabel.setText('Working...')
            if self.week_b.isChecked():
                week_start = "B"
            else:
                week_start = "A"
            dates = tp.timetableDates(term_start=term_start, half_end=half_end, half_start=half_start, term_end=term_end, week_start=week_start)
            calGroup = tp.TimeTableGroup(xml_file, dates)
            if not(self.first_run) and self.calThread.running:
                pass
            else:
                self.first_run = False
                self.calThread = calendarThread(calGroup, target, parent=self)
                self.calThread.start()


class calendarThread(threading.Thread):
    def __init__(self, calendarGroup, target, parent=None):
        threading.Thread.__init__(self)
        self.calendarGroup = calendarGroup
        self.target = target
        self.parent = parent
        self.running = True

    def run(self):
        try:
            self.calendarGroup.generate_calendars(self.target)
            self.parent.workLabel.setText('Done')
            self.running = False
        except:
            self.parent.workLabel.setText('Error')
            self.running = False

class QStyledCalendar(QtWidgets.QCalendarWidget):
    def __init__(self, parent=None):
        super(QStyledCalendar, self).__init__(parent)

    def setDayColor(self, day, color):
        if type(color) != QtGui.QColor:
            color = QtGui.QColor(color)
        form = self.weekdayTextFormat(day)
        form.setForeground(color)
        self.setWeekdayTextFormat(day, form)

    def setDirectionIcons(self, left_icon, right_icon):
        left_button = self.children()[3].children()[0]
        right_button = self.children()[3].children()[1]
        if type(left_icon) != QtGui.QIcon:
            left_icon = QtGui.QIcon(left_icon)
        if type(right_icon) != QtGui.QIcon:
            right_icon = QtGui.QIcon(right_icon)
        left_button.setIcon(left_icon)
        right_button.setIcon(right_icon)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(style)
    form = TimetableApp()
    form.show()
    app.exec_()
