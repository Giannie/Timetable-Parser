# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_layout.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(550, 478)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.half_start_edit = QtGui.QDateEdit(self.centralwidget)
        self.half_start_edit.setCalendarPopup(True)
        self.half_start_edit.setObjectName(_fromUtf8("half_start_edit"))
        self.gridLayout.addWidget(self.half_start_edit, 2, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 4, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.target_choice_button = QtGui.QPushButton(self.centralwidget)
        self.target_choice_button.setObjectName(_fromUtf8("target_choice_button"))
        self.gridLayout.addWidget(self.target_choice_button, 6, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.term_start_edit = QtGui.QDateEdit(self.centralwidget)
        self.term_start_edit.setCalendarPopup(True)
        self.term_start_edit.setObjectName(_fromUtf8("term_start_edit"))
        self.gridLayout.addWidget(self.term_start_edit, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.half_end_edit = QtGui.QDateEdit(self.centralwidget)
        self.half_end_edit.setCalendarPopup(True)
        self.half_end_edit.setObjectName(_fromUtf8("half_end_edit"))
        self.gridLayout.addWidget(self.half_end_edit, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.xml_line_edit = QtGui.QLineEdit(self.centralwidget)
        self.xml_line_edit.setObjectName(_fromUtf8("xml_line_edit"))
        self.gridLayout.addWidget(self.xml_line_edit, 5, 1, 1, 4)
        self.xml_choice_button = QtGui.QPushButton(self.centralwidget)
        self.xml_choice_button.setObjectName(_fromUtf8("xml_choice_button"))
        self.gridLayout.addWidget(self.xml_choice_button, 5, 0, 1, 1)
        self.term_end_edit = QtGui.QDateEdit(self.centralwidget)
        self.term_end_edit.setCalendarPopup(True)
        self.term_end_edit.setObjectName(_fromUtf8("term_end_edit"))
        self.gridLayout.addWidget(self.term_end_edit, 3, 1, 1, 1)
        self.genCalButton = QtGui.QPushButton(self.centralwidget)
        self.genCalButton.setObjectName(_fromUtf8("genCalButton"))
        self.gridLayout.addWidget(self.genCalButton, 7, 0, 1, 1)
        self.target_line_edit = QtGui.QLineEdit(self.centralwidget)
        self.target_line_edit.setObjectName(_fromUtf8("target_line_edit"))
        self.gridLayout.addWidget(self.target_line_edit, 6, 1, 1, 4)
        self.quitButton = QtGui.QPushButton(self.centralwidget)
        self.quitButton.setObjectName(_fromUtf8("quitButton"))
        self.gridLayout.addWidget(self.quitButton, 8, 4, 1, 1)
        self.workLabel = QtGui.QLabel(self.centralwidget)
        self.workLabel.setText(_fromUtf8(""))
        self.workLabel.setObjectName(_fromUtf8("workLabel"))
        self.gridLayout.addWidget(self.workLabel, 7, 1, 1, 4)
        self.dateFileButton = QtGui.QPushButton(self.centralwidget)
        self.dateFileButton.setObjectName(_fromUtf8("dateFileButton"))
        self.gridLayout.addWidget(self.dateFileButton, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 550, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Timetable Generator", None))
        self.label_3.setText(_translate("MainWindow", "Start of second half term:", None))
        self.label.setText(_translate("MainWindow", "Start of Term:", None))
        self.target_choice_button.setText(_translate("MainWindow", "Choose target directory", None))
        self.label_4.setText(_translate("MainWindow", "End of term:", None))
        self.label_2.setText(_translate("MainWindow", "End of first half term:", None))
        self.xml_choice_button.setText(_translate("MainWindow", "Choose xml File", None))
        self.genCalButton.setText(_translate("MainWindow", "Generate Calendar", None))
        self.quitButton.setText(_translate("MainWindow", "Quit", None))
        self.dateFileButton.setText(_translate("MainWindow", "Dates from File", None))

