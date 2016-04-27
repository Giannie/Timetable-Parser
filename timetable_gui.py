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

    def selectXMLFile(self):
        self.xml_line_edit.setText(QtGui.QFileDialog)

    def selectTarget(self):
        self.target_line_edit.setText(QtGui.QFileDialog)
