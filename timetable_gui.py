from PyQt4 import QtGui, QtCore
import qt_layout
import timetable_parser as tp
import sys
import datetime
import threading
import os

class TimetableApp(QtGui.QMainWindow, qt_layout.Ui_MainWindow):
    def __init__(self, parent=None):
        super(TimetableApp, self).__init__(parent)
        self.setupUi(self)
        self.date_edit_list = [self.term_start_edit, self.half_end_edit, self.half_start_edit, self.term_end_edit]
        for index in range(len(self.date_edit_list)):
            date_edit = self.date_edit_list[index]
            date_edit.setDate(QtCore.QDate.currentDate())
            date_edit.calendarWidget().setFirstDayOfWeek(1)
            date_edit.dateChanged.connect(self.lambdaGen(index))
            if index > 0:
                date_edit.setMinimumDate(QtCore.QDate.currentDate())

        self.xml_choice_button.clicked.connect(self.selectXMLFile)
        self.target_choice_button.clicked.connect(self.selectTarget)
        self.genCalButton.clicked.connect(self.generateCalendars)
        self.quitButton.clicked.connect(self.close)
        self.first_run = True

    def updateDates(self, index=0):
        if index < 3:
            self.date_edit_list[index + 1].setMinimumDate(self.date_edit_list[index].date())

    def lambdaGen(self, i):
        return lambda: self.updateDates(i)

    def selectXMLFile(self):
        self.xml_line_edit.setText(QtGui.QFileDialog.getOpenFileName())

    def selectTarget(self):
        self.target_line_edit.setText(QtGui.QFileDialog.getExistingDirectory())

    def generateCalendars(self):
        target = self.target_line_edit.text()
        term_start = datetime.datetime.combine(self.term_start_edit.date().toPyDate(), datetime.time())
        half_end = datetime.datetime.combine(self.half_end_edit.date().toPyDate(), datetime.time())
        half_start = datetime.datetime.combine(self.half_start_edit.date().toPyDate(), datetime.time())
        term_end = datetime.datetime.combine(self.term_end_edit.date().toPyDate(), datetime.time())
        dates = tp.timetableDates(term_start=term_start, half_end=half_end, half_start=half_start, term_end=term_end)
        if not(os.path.isfile(self.xml_line_edit.text())):
            self.workLabel.setText("XML file not found")
        elif not(os.path.isdir(self.target_line_edit.text())):
            self.workLabel.setText("Target directory not found")
        else:
            self.workLabel.setText('Working...')
            calGroup = tp.TimeTableGroup(self.xml_line_edit.text(), dates)
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


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    form = TimetableApp()
    form.show()
    app.exec_()
