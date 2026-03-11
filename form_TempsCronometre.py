# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'form_TempsCronometre.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!
#
# Pi-Day v.1.1.1
# Copyright (C) 2026 Juan Luis Rubio López
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, version 3.
#
# See the LICENSE file for details.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Temps(object):
    def setupUi(self, Temps):
        Temps.setObjectName("Temps")
        Temps.resize(201, 175)
        Temps.setMinimumSize(QtCore.QSize(201, 175))
        Temps.setMaximumSize(QtCore.QSize(201, 175))
        self.label = QtWidgets.QLabel(Temps)
        self.label.setGeometry(QtCore.QRect(20, 30, 161, 51))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Temps)
        self.lineEdit.setGeometry(QtCore.QRect(20, 90, 51, 23))
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.tancar = QtWidgets.QPushButton(Temps)
        self.tancar.setGeometry(QtCore.QRect(90, 140, 80, 23))
        self.tancar.setObjectName("tancar")

        self.retranslateUi(Temps)
        self.tancar.clicked.connect(Temps.close)
        QtCore.QMetaObject.connectSlotsByName(Temps)

    def retranslateUi(self, Temps):
        _translate = QtCore.QCoreApplication.translate
        Temps.setWindowTitle(_translate("Temps", "Temps"))
        self.label.setText(_translate("Temps", "<html><head/><body><p>Temps pel compte enrere</p><p>(en segons):</p></body></html>"))
        self.tancar.setText(_translate("Temps", "TANCAR"))
