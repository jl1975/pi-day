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
from fbs_runtime.application_context.PyQt5 import ApplicationContext # EMPAQUETAMIENTO FBS
appctxt = ApplicationContext()       # 1. EMPAQUETAMIENTO FBS


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1024, 650)  # Tamaño inicial ligeramente mayor
        
        # Configuración de tamaño adaptable
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        
        # Widget central y layout principal
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.main_layout.setContentsMargins(15, 15, 15, 15)  # Márgenes más generosos
        self.main_layout.setSpacing(15)
        
        # --- SECCIÓN SUPERIOR (logo, título, imagen pi) ---
        self.top_layout = QtWidgets.QHBoxLayout()
        self.top_layout.setContentsMargins(0, 0, 0, 0)
        self.top_layout.setSpacing(20)
        
        # Logo (izquierda)
        self.lbl_logo = QtWidgets.QLabel()
        self.lbl_logo.setMinimumSize(QtCore.QSize(151, 151))
        self.lbl_logo.setMaximumSize(QtCore.QSize(151, 151))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.lbl_logo.setFont(font)
        self.lbl_logo.setAutoFillBackground(False)
        self.lbl_logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lbl_logo.setText("")
        self.lbl_logo.setScaledContents(False)
        self.lbl_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_logo.setWordWrap(False)
        self.lbl_logo.setOpenExternalLinks(False)
        self.lbl_logo.setObjectName("lbl_logo")
        self.top_layout.addWidget(self.lbl_logo)
        
        # Título (centro)
        self.lbl_Titulo = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_Titulo.sizePolicy().hasHeightForWidth())
        self.lbl_Titulo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        font.setBold(True)
        self.lbl_Titulo.setFont(font)
        self.lbl_Titulo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_Titulo.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_Titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_Titulo.setObjectName("lbl_Titulo")
        self.top_layout.addWidget(self.lbl_Titulo, 1)  # Factor de expansión 1
        
        # Imagen Pi (derecha)
        self.lbl_Pi = QtWidgets.QLabel()
        self.lbl_Pi.setMinimumSize(QtCore.QSize(161, 141))
        self.lbl_Pi.setMaximumSize(QtCore.QSize(161, 141))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.lbl_Pi.setFont(font)
        self.lbl_Pi.setText("")
        
        filepath=appctxt.get_resource('pi.png') # EMPAQUETAMIENTO FBS
        self.lbl_Pi.setPixmap(QtGui.QPixmap(filepath)) # EMPAQUETAMIENTO FBS
        #self.lbl_Pi.setPixmap(QtGui.QPixmap("pi.png")) # EMPAQUETAMIENTO FBS
        self.lbl_Pi.setScaledContents(True)
        self.lbl_Pi.setObjectName("lbl_Pi")
        self.top_layout.addWidget(self.lbl_Pi)
        
        self.main_layout.addLayout(self.top_layout)
        
        # --- LÍNEA SEPARADORA ---
        self.line = QtWidgets.QFrame()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.main_layout.addWidget(self.line)
        
        # --- SECCIÓN DE MENSAJES Y CONTROLES ---
        self.middle_layout = QtWidgets.QVBoxLayout()
        self.middle_layout.setContentsMargins(0, 0, 0, 0)
        self.middle_layout.setSpacing(10)
        
        # Mensaje de error
        self.mens_error = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setBold(True)
        self.mens_error.setFont(font)
        self.mens_error.setObjectName("mens_error")
        self.middle_layout.addWidget(self.mens_error)
        
        # Layout para aciertos y controles
        self.controls_layout = QtWidgets.QHBoxLayout()
        self.controls_layout.setSpacing(20)  # Más espacio entre elementos
        
        # Aciertos (izquierda)
        self.aciertos_layout = QtWidgets.QHBoxLayout()
        self.lbl_num_aciertos = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_num_aciertos.sizePolicy().hasHeightForWidth())
        self.lbl_num_aciertos.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setBold(True)
        self.lbl_num_aciertos.setFont(font)
        self.lbl_num_aciertos.setObjectName("lbl_num_aciertos")
        self.aciertos_layout.addWidget(self.lbl_num_aciertos, 0, QtCore.Qt.AlignLeft)
        
        self.num_aciertos = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setBold(True)
        self.num_aciertos.setFont(font)
        self.num_aciertos.setObjectName("num_aciertos")
        self.aciertos_layout.addWidget(self.num_aciertos)
        self.controls_layout.addLayout(self.aciertos_layout, 1)  # Factor de expansión 1
        
        # Checkboxes (centro) - Ajustados para evitar recorte
        self.checkbox_layout = QtWidgets.QVBoxLayout()
        self.checkbox_layout.setSpacing(10)
        self.checkbox_layout.setContentsMargins(10, 0, 10, 0)  # Márgenes internos
        
        self.Flag_Sonido = QtWidgets.QCheckBox()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Flag_Sonido.sizePolicy().hasHeightForWidth())
        self.Flag_Sonido.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)  # Tamaño de fuente ajustado
        self.Flag_Sonido.setFont(font)
        self.Flag_Sonido.setObjectName("Flag_Sonido")
        self.checkbox_layout.addWidget(self.Flag_Sonido, 0, QtCore.Qt.AlignLeft)
        
        self.Flag_TextoOculto = QtWidgets.QCheckBox()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Flag_TextoOculto.sizePolicy().hasHeightForWidth())
        self.Flag_TextoOculto.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)  # Tamaño de fuente ajustado
        self.Flag_TextoOculto.setFont(font)
        self.Flag_TextoOculto.setObjectName("Flag_TextoOculto")
        self.checkbox_layout.addWidget(self.Flag_TextoOculto, 0, QtCore.Qt.AlignLeft)
        self.controls_layout.addLayout(self.checkbox_layout)
        
        # Botones (derecha) - Ajustados para evitar recorte
        self.button_layout = QtWidgets.QVBoxLayout()
        self.button_layout.setSpacing(8)
        self.button_layout.setContentsMargins(0, 0, 0, 0)
        
        # Configuración común para botones
        button_font = QtGui.QFont()
        button_font.setFamily("Arial")
        button_font.setPointSize(10)  # Fuente ligeramente más pequeña para caber mejor
        
        button_size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        button_size_policy.setHorizontalStretch(0)
        button_size_policy.setVerticalStretch(0)
        
        min_button_width = 120  # Ancho mínimo para todos los botones
        button_height = 35  # Altura uniforme
        
        self.iniciar = QtWidgets.QPushButton()
        button_size_policy.setHeightForWidth(self.iniciar.sizePolicy().hasHeightForWidth())
        self.iniciar.setSizePolicy(button_size_policy)
        self.iniciar.setFont(button_font)
        self.iniciar.setMinimumSize(QtCore.QSize(min_button_width, button_height))
        self.iniciar.setObjectName("iniciar")
        self.button_layout.addWidget(self.iniciar)
        
        self.duplicar = QtWidgets.QPushButton()
        button_size_policy.setHeightForWidth(self.duplicar.sizePolicy().hasHeightForWidth())
        self.duplicar.setSizePolicy(button_size_policy)
        self.duplicar.setFont(button_font)
        self.duplicar.setMinimumSize(QtCore.QSize(min_button_width, button_height))
        self.duplicar.setObjectName("duplicar")
        self.button_layout.addWidget(self.duplicar)
        
        self.cronometre = QtWidgets.QPushButton()
        button_size_policy.setHeightForWidth(self.cronometre.sizePolicy().hasHeightForWidth())
        self.cronometre.setSizePolicy(button_size_policy)
        self.cronometre.setFont(button_font)
        self.cronometre.setMinimumSize(QtCore.QSize(min_button_width, button_height))
        self.cronometre.setObjectName("cronometre")
        self.button_layout.addWidget(self.cronometre)
        
        self.controls_layout.addLayout(self.button_layout)
        self.middle_layout.addLayout(self.controls_layout)
        self.main_layout.addLayout(self.middle_layout)
        
        # --- SECCIÓN DE ENTRADA (3. + campo de texto) ---
        self.input_layout = QtWidgets.QHBoxLayout()
        self.input_layout.setContentsMargins(0, 0, 0, 0)
        self.input_layout.setSpacing(15)
        
        # Label "3." - Ajustado para subirlo (márgen superior negativo)
        self.lbl_Tres = QtWidgets.QLabel()
        self.lbl_Tres.setMinimumSize(QtCore.QSize(111, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(52)
        font.setBold(True)
        self.lbl_Tres.setFont(font)
        self.lbl_Tres.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_Tres.setObjectName("lbl_Tres")
        
        # Contenedor para el "3." con márgen superior negativo
        self.tres_container = QtWidgets.QWidget()
        self.tres_layout = QtWidgets.QVBoxLayout(self.tres_container)
        self.tres_layout.setContentsMargins(0, -20, 0, 0)  # Margen superior negativo para subirlo
        self.tres_layout.addWidget(self.lbl_Tres)
        self.input_layout.addWidget(self.tres_container)
        
        # Campo de entrada de texto
        self.input = QtWidgets.QTextEdit()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input.sizePolicy().hasHeightForWidth())
        self.input.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        self.input.setFont(font)
        self.input.setObjectName("input")
        self.input_layout.addWidget(self.input, 1)  # Factor de expansión 1
        
        self.main_layout.addLayout(self.input_layout, 1)  # Prioridad alta para esta sección
        
        # Configuración de la barra de menú
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 22))
        self.menubar.setObjectName("menubar")
        
        self.menuConfiguraci = QtWidgets.QMenu(self.menubar)
        self.menuConfiguraci.setObjectName("menuConfiguraci")
        
        self.menuAjuda = QtWidgets.QMenu(self.menubar)
        self.menuAjuda.setObjectName("menuAjuda")
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.actionCarregar_Logo = QtWidgets.QAction(MainWindow)
        self.actionCarregar_Logo.setObjectName("actionCarregar_Logo")
        
        self.actionInstruccions = QtWidgets.QAction(MainWindow)
        self.actionInstruccions.setObjectName("actionInstruccions")
        
        self.actionCredits = QtWidgets.QAction(MainWindow)
        self.actionCredits.setObjectName("actionCredits")
        
        ### v. 1.1.1
        
        self.actionLlicencia = QtWidgets.QAction(MainWindow)
        self.actionLlicencia.setObjectName("actionLlicencia")
        
        ###
        
        self.actionTemps_Cron_metre = QtWidgets.QAction(MainWindow)
        self.actionTemps_Cron_metre.setObjectName("actionTemps_Cron_metre")
        
        self.menuConfiguraci.addAction(self.actionCarregar_Logo)
        self.menuConfiguraci.addAction(self.actionTemps_Cron_metre)
        self.menuAjuda.addAction(self.actionInstruccions)
        self.menuAjuda.addAction(self.actionCredits)
        
        ### v. 1.1.1
        self.menuAjuda.addAction(self.actionLlicencia)
        ###
        
        self.menubar.addAction(self.menuConfiguraci.menuAction())
        self.menubar.addAction(self.menuAjuda.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pi-day"))
        self.lbl_Tres.setText(_translate("MainWindow", "3."))
        self.duplicar.setText(_translate("MainWindow", "DUPLICAR"))
        self.Flag_Sonido.setText(_translate("MainWindow", "So d\'error"))
        self.num_aciertos.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#00aa00;\">TextLabel</span></p></body></html>"))
        self.lbl_num_aciertos.setText(_translate("MainWindow", "N. d\'encerts:"))
        self.iniciar.setText(_translate("MainWindow", "COMENÇAR"))
        self.Flag_TextoOculto.setText(_translate("MainWindow", "Text ocult \n"
"al duplicat"))
        self.mens_error.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#aa0000;\">Error! El nombre correcte és</span></p></body></html>"))
        self.lbl_Titulo.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; color:#555500;\">Concurs Pi-Day </span></p></body></html>"))
        self.cronometre.setText(_translate("MainWindow", "CRONÒMETRE"))
        self.menuConfiguraci.setTitle(_translate("MainWindow", "Configuració"))
        self.menuAjuda.setTitle(_translate("MainWindow", "Ajuda"))
        self.actionCarregar_Logo.setText(_translate("MainWindow", "Carregar Logo"))
        self.actionInstruccions.setText(_translate("MainWindow", "Instruccions"))
        self.actionCredits.setText(_translate("MainWindow", "Crèdits"))
        
        ### v. 1.1.1
        self.actionLlicencia.setText(_translate("MainWindow", "Llicència"))
        ###
        
        self.actionTemps_Cron_metre.setText(_translate("MainWindow", "Temps Cronòmetre"))