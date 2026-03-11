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

class Ui_Llicencia(object):
    def setupUi(self, Llicencia):
        Llicencia.setObjectName("Llicencia")
        Llicencia.resize(600, 500)  # Tamaño inicial más adecuado
        
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
        Llicencia.setPalette(palette)
        
        # Layout principal
        self.main_layout = QtWidgets.QVBoxLayout(Llicencia)
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

        self.retranslateUi(Llicencia)
        self.tancar.clicked.connect(Llicencia.close)
        QtCore.QMetaObject.connectSlotsByName(Llicencia)

    def retranslateUi(self, Llicencia):
        _translate = QtCore.QCoreApplication.translate
        Llicencia.setWindowTitle(_translate("Llicencia", "Llicència"))
        
        ### v. 1.1.1
        self.label.setOpenExternalLinks(True)
        self.label.setTextFormat(QtCore.Qt.RichText)
        
        self.label.setText(
        "Pi-Day v1.1<br><br>"
        "(c) Juan Luis Rubio López<br>"
        "Terrassa (2021–2025)<br><br>"
        "Licència: GNU AGPLv3<br><br>"
        "El codi complet es troba disponible a:<br>"
        "<a href='https://github.com/jl1975/pi-day'>https://github.com/jl1975/pi-day</a><br><br>"
        "Aquest programa és software lliure: el pots distribuir i/o modificar<br>"
        "sota els termes de la llicència AGPL versió 3."
        )

        ###
        
       
        self.tancar.setText(_translate("Llicencia", "TANCAR"))