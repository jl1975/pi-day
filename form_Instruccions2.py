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

class Ui_Instruccions(object):
    def setupUi(self, Instruccions):
        Instruccions.setObjectName("Instruccions")
        Instruccions.resize(800, 700)  # Tamaño inicial más adecuado
        
        # Configurar paleta de colores
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 236, 233))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 236, 233))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 236, 233))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 236, 233))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Instruccions.setPalette(palette)
        Instruccions.setWindowOpacity(1.0)
        
        # Layout principal directamente en el diálogo
        self.main_layout = QtWidgets.QVBoxLayout(Instruccions)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(15)
        
        # Etiqueta de instrucciones con scroll
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        
        self.label = QtWidgets.QLabel()
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setObjectName("label")
        
        # Configurar paleta para la etiqueta
        label_palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(239, 235, 231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        label_palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        label_palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        label_palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.label.setPalette(label_palette)
        
        self.scroll_area.setWidget(self.label)
        self.main_layout.addWidget(self.scroll_area, 1)  # Factor de estiramiento 1
        
        # Botón de cerrar (centrado)
        self.button_layout = QtWidgets.QHBoxLayout()
        self.button_layout.addStretch()  # Espacio a la izquierda
        
        self.tancar = QtWidgets.QPushButton()
        self.tancar.setObjectName("tancar")
        self.tancar.setFixedSize(100, 30)
        self.button_layout.addWidget(self.tancar)
        
        self.button_layout.addStretch()  # Espacio a la derecha
        self.main_layout.addLayout(self.button_layout)
        
        self.retranslateUi(Instruccions)
        self.tancar.clicked.connect(Instruccions.close)
        QtCore.QMetaObject.connectSlotsByName(Instruccions)

    def retranslateUi(self, Instruccions):
        _translate = QtCore.QCoreApplication.translate
        Instruccions.setWindowTitle(_translate("Instruccions", "Instruccions"))
        self.label.setText(_translate("Instruccions", "<html><head/><body><p align=\"center\"><span style=\" font-size:small; font-weight:600; text-decoration: underline;\">INSTRUCCIONS</span></p><p align=\"center\"><span style=\" font-size:small;\"><br/>Aquest programa permet dur a terme un concurs de memorització dels decimals </span></p><p align=\"center\"><span style=\" font-size:small;\">del nombre Pi, a on els participants van introduïnt els decimals i un comptador</span></p><p align=\"center\"><span style=\" font-size:small;\">comptabilitza el nombre d\'encerts.</span></p><p align=\"center\"><br/><span style=\" font-size:small; font-weight:600; color:#00007f;\">Menú Configuració -&gt; Carregar Logo</span></p><p align=\"center\"><span style=\" font-size:small;\">Aquí podeu carregar el logo de la vostra organització, que apareixerà a la caixa </span></p><p align=\"center\"><span style=\" font-size:small;\">de l\'esquerra de la finestra. Es recomana que tingui proporcions quadrades, </span></p><p align=\"center\"><span style=\" font-size:small;\">En cas contrari, pot mostrar-se lleugerament deformat. </span></p><p align=\"center\"><span style=\" font-size:small; font-weight:600; color:#00007f;\">Menú Configuració -&gt; Temps Cronòmetre</span></p><p align=\"center\"><span style=\" font-size:small;\">Permet fixar el temps pel compte enrere quan s\'activa el botó &quot;Cronòmetre&quot;.</span></p><p align=\"center\"><span style=\" font-size:small;\">Útil per fer una final amb els guanyadors de cada centre.</span></p><p align=\"center\"><span style=\" font-size:small; font-weight:600; color:#00007f;\">So d\'error</span></p><p align=\"center\"><span style=\" font-size:small;\">S\'emet un so d\'error quan l\'usuari introdueix un decimal incorrecte. </span></p><p align=\"center\"><span style=\" font-size:small; font-weight:600; color:#00007f;\">Duplicar</span></p><p align=\"center\"><span style=\" font-size:small;\">Permet obrir una segona finestra, semblant a la principal, que pot ser col·locada </span></p><p align=\"center\"><span style=\" font-size:small;\">a una segona pantalla (com la d\'un projector) i que serà la que veurà el públic participant </span></p><p align=\"center\"><span style=\" font-size:small;\">del concurs. En aquest cas, s\'ha d\'utilitzar la opció &quot;Expandir la pantalla principal&quot;. </span></p><p align=\"center\"><span style=\" font-size:small;\">Activant l\'opció &quot;Text ocult al duplicat&quot;, els nombres introduïts són substituïts </span></p><p align=\"center\"><span style=\" font-size:small;\">per asteriscs a la segona finestra, de manera que els futurs participants, situats </span></p><p align=\"center\"><span style=\" font-size:small;\">entre el públic, no tindran avantatge memorístic.</span><br/></p><p align=\"center\"><span style=\" font-size:small;\">Bona sort! </span></p></body></html>"))
        self.tancar.setText(_translate("Instruccions", "TANCAR"))