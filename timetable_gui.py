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
        self.calThread = None

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
        if not(os.path.isfile(self.xml_line_edit.text())):
            self.workLabel.setText("XML file not found")
        elif not(os.path.isdir(self.target_line_edit.text())):
            self.workLabel.setText("Target directory not found")
        else:
            self.workLabel.setText('Working...')
            calGroup = tp.TimeTableGroup(self.xml_line_edit.text())
            if self.calThread:
                pass
            else:
                self.calThread = calendarThread(calGroup, term_start, half_end, half_start, term_end, target, parent=self)
                self.calThread.start()


class calendarThread(threading.Thread):
    def __init__(self, calendarGroup, term_start, half_end, half_start, term_end, target, parent=None):
        threading.Thread.__init__(self)
        self.calendarGroup = calendarGroup
        self.term_start = term_start
        self.term_end = term_end
        self.half_end = half_end
        self.half_start = half_start
        self.target = target
        self.parent = parent

    def run(self):
        try:
            self.calendarGroup.generate_calendars(self.term_start, self.half_end, self.half_start, self.term_end, path=self.target)
            self.parent.workLabel.setText('Done')
            self = None
        except:
            self.parent.workLabel.setText('Error')
            self = None


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    form = TimetableApp()
    form.show()
    app.exec_()
