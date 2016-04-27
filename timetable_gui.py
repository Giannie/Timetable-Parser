from PyQt4 import QtGui, QtCore
import qt_layout
import timetable_parser as tp
import sys

class TimetableApp(QtGui.QMainWindow, qt_layout.Ui_MainWindow):
    def __init__(self, parent=None):
        super(TimetableApp, self).__init__(parent)
        self.setupUi(self)
        for date_edit in self.findChildren(QtGui.QDateEdit):
            date_edit.setDate(QtCore.QDate.currentDate())
        self.xml_choice_button.clicked.connect(self.selectXMLFile)
        self.target_choice_button.clicked.connect(self.selectTarget)
        self.genCalButton.clicked.connect(self.generateCalendars)

    def selectXMLFile(self):
        self.xml_line_edit.setText(QtGui.QFileDialog.getOpenFileName())

    def selectTarget(self):
        self.target_line_edit.setText(QtGui.QFileDialog.getExistingDirectory())

    def generateCalendars(self):
        calGroup = tp.TimeTableGroup(self.xml_line_edit.text)
        target = self.target_line_edit.text
        term_start = self.term_start_edit.date.toPyDate()
        half_end = self.half_end_edit.date.toPyDate()
        half_start = self.half_start_edit.date.toPyDate()
        term_end = self.term_end_edit.date.toPyDate()
        calGroup.generate_calendars(term_start, half_end, half_start, term_end, path=target)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    form = TimetableApp()
    form.show()
    app.exec_()
