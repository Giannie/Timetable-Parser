# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_layout.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 478)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.target_choice_button = QtWidgets.QPushButton(self.centralwidget)
        self.target_choice_button.setObjectName("target_choice_button")
        self.gridLayout.addWidget(self.target_choice_button, 8, 0, 1, 1)
        self.genCalButton = QtWidgets.QPushButton(self.centralwidget)
        self.genCalButton.setObjectName("genCalButton")
        self.gridLayout.addWidget(self.genCalButton, 9, 0, 1, 1)
        self.term_start_edit = QtWidgets.QDateEdit(self.centralwidget)
        self.term_start_edit.setCalendarPopup(True)
        self.term_start_edit.setObjectName("term_start_edit")
        self.gridLayout.addWidget(self.term_start_edit, 0, 1, 1, 1)
        self.week_a = QtWidgets.QRadioButton(self.centralwidget)
        self.week_a.setChecked(True)
        self.week_a.setObjectName("week_a")
        self.startWeekGroup = QtWidgets.QButtonGroup(MainWindow)
        self.startWeekGroup.setObjectName("startWeekGroup")
        self.startWeekGroup.addButton(self.week_a)
        self.gridLayout.addWidget(self.week_a, 4, 1, 1, 1)
        self.xml_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.xml_line_edit.setObjectName("xml_line_edit")
        self.gridLayout.addWidget(self.xml_line_edit, 7, 1, 1, 4)
        self.dateFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.dateFileButton.setObjectName("dateFileButton")
        self.gridLayout.addWidget(self.dateFileButton, 6, 0, 1, 1)
        self.xml_choice_button = QtWidgets.QPushButton(self.centralwidget)
        self.xml_choice_button.setObjectName("xml_choice_button")
        self.gridLayout.addWidget(self.xml_choice_button, 7, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.half_start_edit = QtWidgets.QDateEdit(self.centralwidget)
        self.half_start_edit.setCalendarPopup(True)
        self.half_start_edit.setObjectName("half_start_edit")
        self.gridLayout.addWidget(self.half_start_edit, 2, 1, 1, 1)
        self.half_end_edit = QtWidgets.QDateEdit(self.centralwidget)
        self.half_end_edit.setCalendarPopup(True)
        self.half_end_edit.setObjectName("half_end_edit")
        self.gridLayout.addWidget(self.half_end_edit, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.quitButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitButton.setObjectName("quitButton")
        self.gridLayout.addWidget(self.quitButton, 10, 4, 1, 1)
        self.target_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.target_line_edit.setObjectName("target_line_edit")
        self.gridLayout.addWidget(self.target_line_edit, 8, 1, 1, 4)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.workLabel = QtWidgets.QLabel(self.centralwidget)
        self.workLabel.setText("")
        self.workLabel.setObjectName("workLabel")
        self.gridLayout.addWidget(self.workLabel, 9, 1, 1, 4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.term_end_edit = QtWidgets.QDateEdit(self.centralwidget)
        self.term_end_edit.setCalendarPopup(True)
        self.term_end_edit.setObjectName("term_end_edit")
        self.gridLayout.addWidget(self.term_end_edit, 3, 1, 1, 1)
        self.week_b = QtWidgets.QRadioButton(self.centralwidget)
        self.week_b.setObjectName("week_b")
        self.startWeekGroup.addButton(self.week_b)
        self.gridLayout.addWidget(self.week_b, 5, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 550, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Timetable Generator"))
        self.target_choice_button.setText(_translate("MainWindow", "Choose target directory"))
        self.genCalButton.setText(_translate("MainWindow", "Generate Calendar"))
        self.week_a.setText(_translate("MainWindow", "Week A"))
        self.dateFileButton.setText(_translate("MainWindow", "Dates from File"))
        self.xml_choice_button.setText(_translate("MainWindow", "Choose xml File"))
        self.label_3.setText(_translate("MainWindow", "Start of second half term:"))
        self.label_4.setText(_translate("MainWindow", "End of term:"))
        self.quitButton.setText(_translate("MainWindow", "Quit"))
        self.label.setText(_translate("MainWindow", "Start of Term:"))
        self.label_2.setText(_translate("MainWindow", "End of first half term:"))
        self.label_5.setText(_translate("MainWindow", "Start Week:"))
        self.week_b.setText(_translate("MainWindow", "Week B"))

