# -*- coding: utf-8 -*-
# Pi-Day v.1.1.1
# Copyright (C) 2026 Juan Luis Rubio López
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, version 3.
#
# See the LICENSE file for details.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Credits(object):
    def setupUi(self, Credits):
        Credits.setObjectName("Credits")
        Credits.resize(600, 500)  # Tamaño inicial más adecuado
        
        # Configurar paleta de colores (igual que antes)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 235, 231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 235, 231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 235, 231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 235, 231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Credits.setPalette(palette)
        
        # Layout principal
        self.main_layout = QtWidgets.QVBoxLayout(Credits)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(15)
        
        # Área de scroll para el contenido
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        
        # Contenedor para el label
        self.content_widget = QtWidgets.QWidget()
        self.content_layout = QtWidgets.QVBoxLayout(self.content_widget)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        
        # Label con los créditos
        self.label = QtWidgets.QLabel()
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setTextFormat(QtCore.Qt.RichText)
        
        # Configurar paleta para la etiqueta (igual que antes)
        label_palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        label_palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        
        self.label.setPalette(label_palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        
        self.content_layout.addWidget(self.label)
        self.scroll_area.setWidget(self.content_widget)
        self.main_layout.addWidget(self.scroll_area, 1)  # Factor de estiramiento 1
        
        # Botón de cerrar (centrado)
        self.button_layout = QtWidgets.QHBoxLayout()
        self.button_layout.addStretch()
        
        self.tancar = QtWidgets.QPushButton()
        self.tancar.setFixedSize(100, 30)
        self.tancar.setObjectName("tancar")
        self.button_layout.addWidget(self.tancar)
        
        self.button_layout.addStretch()
        self.main_layout.addLayout(self.button_layout)

        self.retranslateUi(Credits)
        self.tancar.clicked.connect(Credits.close)
        QtCore.QMetaObject.connectSlotsByName(Credits)

    def retranslateUi(self, Credits):
        _translate = QtCore.QCoreApplication.translate
        Credits.setWindowTitle(_translate("Credits", "Crèdits"))
        self.label.setText(_translate("Credits", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; text-decoration: underline;\">Pi-Day v.1.1 </span></p><p align=\"center\"><br/><span style=\" font-size:small; font-weight:600; color:#0000ff;\">Creat per </span></p><p align=\"center\"><span style=\" font-size:small; font-weight:600;\">Juan Luis Rubio López</span><span style=\" font-size:small;\">, amb python3+pyqt5, a Terrassa (2021-25).</span></p><p align=\"center\"><span style=\" font-size:8pt;\">(com a millora de l\'antiga versió feta amb Visual Basic 6)</span><br/></p><p align=\"center\"><span style=\" font-size:small;\">Dubtes, comentaris i suggerències a</span></p><p align=\"center\"><span style=\" font-size:small; font-style:italic;\">juanluis.rubio@gmail.com</span></p><p align=\"center\"><span style=\" font-size:10pt; font-style:italic;\">jrubio46@xtec.cat</span><br/></p><p align=\"center\"><span style=\" font-size:small; font-weight:600; color:#0000ff;\">Agraïments</span></p><p align=\"center\"><span style=\" font-size:small;\">La idea d\'aquest programa va sorgir a partir d\'inspiradores converses</span></p><p align=\"center\"><span style=\" font-size:small;\">amb el Josep Anton Clua del IES Duc de Montblanc en relació amb el dia Pi.</span></p></body></html>"))
        self.tancar.setText(_translate("Credits", "TANCAR"))