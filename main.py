# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
================================================
Programa para el Concurso de Pi (versión python)
================================================
# Pi-Day v.1.1.1
# Copyright (C) 2026 Juan Luis Rubio López
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, version 3.
#
# See the LICENSE file for details.

El concursante introduce los decimales de Pi.
A medida que lo hace, el contador cuenta los decimales correctos.
En caso de fallo, aparece un mensaje de error..
La cadena de entrada (entrada) se compara carácter a carácter
con la cadena pi, con los primeros 1500 decimales.

03/08 Implementación de sonido de error, con pygame.
      (Sólo reproduce formato wav).
05/08 Implementación del duplicado, mediante una instancia a MyForm2().
      (Una nueva instancia de MyForm() daba error recursivo).
12/08 Duplicado: se muestran asteriscos y se ocultan algunos widgets.
      Método CloseEvent: Control del cierre de la aplicación.
      Con la ventana principal, se cierra también el duplicado. No a la inversa.
      Mejora de etiquetas.
      Cambio de QDialog a QMainWindow para la ventana.
      Barra de menus.
14/08 Implementación del submenú Carregar Logo con un QFileDialog. 
      Implementación de los submenús Instrucciones y Crèdits con nuevos módulos *.py
      (Se ha creado una clase aquí para cada módulo y se declaran sendas instancias 
       en el Bloque Principal).
      Duplicado: Se oculta el menubar.
      Cierre de la ventana principal: se cierran todas las posibles ventanas abiertas.
19/08 Crea archivo INI myfile.ini en cwd si no existe.
26/08 Implementación de métodos de Lectura/Escritura de archivo INI.
16/09 Carga Logo también en MyForm2, para el duplicado, aunque solo la primera vez.
20/09 Carga Logo en Duplicado, leído en ruta, cada vez que se clica en el botón Duplicado,
      incluso si se ha cambiado durante la ejecución actual del programa.
Julio-Septiembre de 2021, Terrassa.
******************************************************************************************
New version 2022:
12/08/22 Nueva gui con layouts provisional. 
         Modo final -> Cronómetro cuenta-atrás funcional provisional con QtCore.QTimer.singleShot()
14/08 Gui sin layouts. Botón cronómetro funcional.
15/08 Implementación leer/escribir en archivo INI la variable temps (tiempo de la cuenta atrás)
      La función LeerArchivoINI sigue siendo única, pero devuelve ahora dos variables.
      La funcioón EscribirArchivoINI se duplica, para escribir clave1, clave2.
Agosto de 2022, Terrassa.

V.1.1.
23/06/25 Las ventanas pueden ajustarse al contenido.
        Ui_MainWindows -> Se han creado layouts de tipo QtWidgets.QVBoxLayout()
        Ui_Instruccions, Ui_Credits -> Hay áreas de scroll en layouts.
        

by Rubio, J. L.
juanluis.rubio@gmail.com

======================================================================================
'''
import sys
import os
import os.path as path
import configparser
import pygame
from datetime import datetime
from pathlib import Path
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from PyQt5.QtGui import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QResizeEvent
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QFile, QIODevice
# Módulos GUI y modulo1 (métodos propios)
#from form_Main import Ui_MainWindow
from form_Main_new2 import Ui_MainWindow
from form_Instruccions2 import Ui_Instruccions
from form_Credits2 import Ui_Credits
from form_License import Ui_Llicencia
from form_TempsCronometre import Ui_Temps
#from modulo1 import EsNumerico, LeerArchivoINI, EscribirArchivoINI1, EscribirArchivoINI2
from modulo2 import EsNumerico, LeerArchivoINI, EscribirArchivoINI1, EscribirArchivoINI2
from fbs_runtime.application_context.PyQt5 import ApplicationContext # EMPAQUETAMIENTO FBS
from PyQt5.QtWidgets import QMainWindow
#from fbs.application_context.PyQt5 import ApplicationContext # EMPAQUETAMIENTO FBS

parser = configparser.SafeConfigParser()
fichero = 'myfile.ini'
seccion = 'main'
clave1 = 'pathLogo'
clave2 = 'temps'

# Usaremos 1500 decimales de Pi
pi = "141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610454326648213393607260249141273724587006606315588174881520920962829254091715364367892590360011330530548820466521384146951941511609433057270365759591953092186117381932611793105118548074462379962749567351885752724891227938183011949129833673362440656643086021394946395224737190702179860943702770539217176293176752384674818467669405132000568127145263560827785771342757789609173637178721468440901224953430146549585371050792279689258923542019956112129021960864034418159813629774771309960518707211349999998372978049951059731732816096318595024459455346908302642522308253344685035261931188171010003137838752886587533208381420617177669147303598253490428755468731159562863882353787593751957781857780532171226806613001927876611195909216420198938095257201065485863278865936153381827968230301952035301852968995773622599413891249721775283479131515574857242454150695950829533116861727855889075098381754637464939319255060400927701671139009848824012858361603563707660104710181942955596198946767837449448255379774726847104047534646208046684259069491293313677028989152104752162056966024058038150193511253382430035587640247496473263914199272604269922796782354781636009341721641219924586315030286182974555706749838505494588586926995690927210797509302955"

class MyForm(QtWidgets.QMainWindow):
    
    # -- Método especial inicializador de la clase MyForm. Automático y sin retorno.
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Inicializa atributos
        global flag_error, flag_nonumerico, entrada, pos, RutaLeida, ruta, pepe, temps, t_cuentaatras
        global flag_cronometro, hora_inicio, lectura_cronometro, segundos_transcurridos
        flag_nonumerico = 0
        flag_cronometro = 0
        flag_error=0
        hora_inicio=0
        pepe=0
        #
        self.ui.mens_error.setStyleSheet("color: red")
        self.ui.num_aciertos.setStyleSheet("color: green")
        self.ui.lbl_num_aciertos.setText("N. d'encerts = ")
        self.ui.cronometre.setText("CRONÒMETRE")
        self.ui.cronometre.setStyleSheet("background-color: orange;border-radius : 3; font-weight: bold;border : 2px solid white")
        self.ui.mens_error.setText("")
        self.ui.num_aciertos.setText("")
        self.ui.input.setText("")
        self.ui.input.setFocus()
        self.ui.Flag_Sonido.setCheckState(False) # Es True de origen

        # Conecta cambio de la entrada y botones con métodos
        self.ui.input.textChanged.connect(self.validar)
        self.ui.iniciar.clicked.connect(self.iniciar)
        self.ui.duplicar.clicked.connect(self.duplicar)
        self.ui.cronometre.clicked.connect(self.cronometre)
        
        #Conecta acciones de los submenús a métodos
        self.ui.actionCarregar_Logo.triggered.connect(self.carregar_Logo)
        self.ui.actionInstruccions.triggered.connect(self.MostrarInstruccions)
        self.ui.actionCredits.triggered.connect(self.MostrarCredits)
        self.ui.actionLlicencia.triggered.connect(self.MostrarLlicencia)
        self.ui.actionTemps_Cron_metre.triggered.connect(self.MostrarTempsCronometre)
        
        
        #INICIALIZACIÓN de archivo INI
        #Crea archivo INI myfile.ini si no existe y lo prepara con una sección y dos claves
        cwd=os.getcwd() # Current work directory
        myfile = Path(cwd+'/myfile.ini')
        if (path.exists(myfile))==False:
            parser = configparser.SafeConfigParser()
            parser.add_section('main')  # Prepara nombre de sección: main.
            parser.set('main', 'pathLogo', '')  # Prepara valor de la clave1 pathLogo en blanco.
            parser.set('main', 'temps', '')  # Prepara valor de la clave2 pathLogo en blanco.
            f = open(myfile, 'w')
            parser.write(f)  # Escribe en el archivo.
            f.close()
            # Cuando crea el archivo por primera vez, escribe temps=60, por defecto.
            tt="60"
            EscribirArchivoINI2(tt) 
        

        #Lee la ruta del Logo y el temps del archivo INI y los carga.
        RutaLeida, temps = LeerArchivoINI()
        ruta = RutaLeida
        
        # Por esto:
        self.ui.lbl_logo.clear()  # Limpiar cualquier contenido previo
        if RutaLeida and os.path.exists(RutaLeida):
            try:
                pixmap = QPixmap(RutaLeida)
                if not pixmap.isNull():
                    self.ui.lbl_logo.setPixmap(pixmap.scaled(
                        self.ui.lbl_logo.size(),
                        QtCore.Qt.KeepAspectRatio,
                        QtCore.Qt.SmoothTransformation
                    ))
            except Exception as e:
                print(f"Error cargando logo: {e}")
                self.ui.lbl_logo.clear()
        
        # if RutaLeida:
        #     pixmap = QPixmap(RutaLeida)
        #     self.ui.lbl_logo.setPixmap(pixmap.scaled(self.ui.lbl_logo.size(),
        #                                              QtCore.Qt.KeepAspectRatio,
        #                                              QtCore.Qt.SmoothTransformation))
        t_cuentaatras = temps #t_cuentaatras va a escribirse en el lineedit de TempsCronometre.
    
    # --  Método para poner el cronómetro a la espera tras ser pulsado.
    def cronometre(self):
        
        global flag_cronometro
        
        flag_cronometro=1

        # Para la ventana principal
        self.ui.input.setText("")
        self.ui.input.setFocus()
        self.ui.mens_error.setText("")
        self.ui.lbl_num_aciertos.setText("N. d'encerts = ")
        self.ui.cronometre.setText("Waiting...")
        self.ui.num_aciertos.setText("")
        
        # Para el duplicado
        myapp2.ui.input.setText("")
        myapp2.ui.input.setFocus()
        myapp2.ui.mens_error.setText("")
        myapp2.ui.lbl_num_aciertos.setText("N. d'encerts = ")
        myapp2.ui.cronometre.setText("Waiting...")
        myapp2.ui.num_aciertos.setText("")


    # -- Método para validar si el carácter es numérico en modo normal y modo cronómetro.
    def validar(self):
        
        global UltimaEntrada, pos, entrada, entrada_modif, t_ini, pos
        global flag_cronometro, hora_inicio, segundos_transcurridos, pepe, flag_error
        
        entrada = self.ui.input.toPlainText()
        pos=len(entrada)
        entrada_asteriscos="*"*pos #cadena con tantos asteriscos como longitud de la entrada
        
        # Muestra asteriscos en el Duplicado
        if self.ui.Flag_TextoOculto.isChecked():
            myapp2.ui.input.setText(entrada_asteriscos)
        else:
            myapp2.ui.input.setText(entrada)
        
#xxxxxxxxxxxxxxxxxxxxx MODO FINAL - CRONÓMETRO xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx          
        # -- Método para refrescar la lectura de la cuenta atrás si fue activado el cronómetro
        # y mostrarla en el texto del botón Cronómetro
        # Lleva incorporado Qtimer.singleShot para autollamarse recurrentemente
        def refresca_label():
            
            global flag_error, tf
            
            #Lee el temps del archivo INI y lo carga
            RutaLeida, temps = LeerArchivoINI()
            t_cuentaatras = temps
            tf=int(t_cuentaatras)
            #Calcula minutos y segundos transcurridos para cada diferencia de tiempos.
            #segundos_transcurridos=int(60-(datetime.now() - hora_inicio).total_seconds())+(tf-60)
            segundos_transcurridos=int(tf-(datetime.now() - hora_inicio).total_seconds())
            minutos = segundos_transcurridos // 60 #cociente entero de la división
            segundos = segundos_transcurridos % 60 #residuo de la división
            #Muestra tiempos en botón Cronòmetre
            self.ui.cronometre.setText("{:02d}".format(minutos)+":"+"{:02d}".format(segundos))
            self.ui.cronometre.setStyleSheet("background-color: orange;border-radius : 3; font-weight: bold;border : 2px solid white")
            myapp2.ui.cronometre.setText("{:02d}".format(minutos)+":"+"{:02d}".format(segundos))
            myapp2.ui.cronometre.setStyleSheet("background-color: orange;border-radius : 3; font-weight: bold;border : 2px solid white")

            if flag_error==1: # Si hi ha un error
                QMessageBox.about(self, "Avís", "Error!")
                returnValue = QMessageBox.Accepted
                flag_error=0
                self.ui.cronometre.setText("CRONÒMETRE")
            elif minutos==0 and segundos==0: # Si finalitza el temps
                QMessageBox.about(self, "Avís", "Temps esgotat!")
                returnValue = QMessageBox.Accepted
                self.ui.cronometre.setText("CRONÒMETRE")
            else:
                QtCore.QTimer.singleShot(500, refresca_label) # Llamada recurrente cada 500 ms para actualizar reloj en segundo plano.

   
        # Si se pulsó el botón del cronómetro y se ha introducido la 1ª cifra
        # -> Toma hora actual y envía a refresca_label
        
        if pos==1 and flag_cronometro==1:
            hora_inicio=datetime.now()
            refresca_label()

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx   
        
        # Cazamos el último caràcter y declaramos la cadena sin él
        if pos>0:
            UltimaEntrada = entrada[pos-1] # Sólo el último carácter de la cadena
            # Último carácter no numérico -> Aviso, reescribimos la cadena sin él y recolocamos el cursor
            # Último carácter es numérico -> Comparamos con el de Pi
            if EsNumerico(UltimaEntrada) == False:
                flag_nonumerico=1
                QMessageBox.about(self, "Avís", "Caràcter no vàlid!")
                returnValue = QMessageBox.Accepted
                if returnValue == 1:
                    self.ui.input.setText(entrada_modif)
                    cursor = self.ui.input.textCursor() 
                    cursor.movePosition(QTextCursor.End)
                    self.ui.input.setTextCursor(cursor)
    
            else:
                flag_nonumerico=0
                self.comparar()
        
        entrada_modif = entrada[:-1] # Toda la cadena salvo el último carácter
    
    
    # -- Método para comparar Último carácter con el correspondiente de Pi
    def comparar(self):
        
        global flag_error, flag_nonumerico, UltimaEntrada, pos
        
        # Si ya se equivocó -> Mensaje de Aviso
        # Si continua correctamente -> Comparar con Pi
        if flag_error==1:
            QMessageBox.about(self, "Avís", "Torna a començar!")
            returnValue = QMessageBox.Accepted
            if returnValue == 1:
                self.iniciar()
        else:
            NumeroPiOk=pi[pos-1] # Tomamos el correspondiente de Pi
            
            # El númerico es correcto -> Modificamos el contador de aciertos
            if UltimaEntrada == NumeroPiOk:
                flag_error=0
                flag_nonumerico=0
                self.ui.lbl_num_aciertos.setText("N. d'encerts = ")
                myapp2.ui.lbl_num_aciertos.setText("N. d'encerts = ")
                self.ui.num_aciertos.setText(str(pos))
                myapp2.ui.num_aciertos.setText(str(pos))
            # El número es incorrecto -> Mensaje de error, flag_error=1 para lanzar aviso
            # y sonido de error si el CheckBox Flag_Sonido está a True
            else:
                flag_error=1
                flag_nonumerico=0
                self.ui.mens_error.setText("Error! El nombre correcte és " + NumeroPiOk)
                myapp2.ui.mens_error.setText("Error! El nombre correcte és " + NumeroPiOk)
                if self.ui.Flag_Sonido.isChecked():
                    self.sonidoerror()
        
    # -- Método para lanzar el archivo sonido.mp3
    def sonidoerror(self):
        
        try:
            # Verifica si pygame ya está inicializado
            if not pygame.get_init():
                pygame.init()
                pygame.mixer.init()
            
            # Obtiene la ruta del recurso
            try:
                filepath = appctxt.get_resource('sonido.wav')
            except:
                # Fallback para desarrollo
                filepath = 'src/main/resources/sonido.wav' if os.path.exists('src/main/resources/sonido.wav') else 'sonido.wav'
            
            # Carga y reproduce el sonido
            if os.path.exists(filepath):
                try:
                    sound = pygame.mixer.Sound(filepath)
                    sound.play()
                except Exception as e:
                    print(f"Error reproduciendo sonido: {e}")
            else:
                print(f"Archivo de sonido no encontrado en: {filepath}")
        except Exception as e:
            print(f"Error inicializando pygame: {e}")
    
    
    # -- Método para reiniciar la entrada de datos tras un error
    def iniciar(self):
        
        global flag_error, flag_nonumerico, flag_cronometro, ruta
        
        flag_error=0
        flag_nonumerico=0
        flag_cronometro=0
        
        pixmap = QPixmap(ruta)
        
        # Para la ventana principal
        self.ui.input.setText("")
        self.ui.input.setFocus()
        self.ui.mens_error.setText("")
        self.ui.lbl_num_aciertos.setText("N. d'encerts = ")
        self.ui.cronometre.setText("CRONÒMETRE")
        self.ui.num_aciertos.setText("")
        
        # Para el duplicado
        myapp2.ui.input.setText("")
        myapp2.ui.input.setFocus()
        myapp2.ui.mens_error.setText("")
        myapp2.ui.cronometre.setText("CRONÒMETRE")
        myapp2.ui.lbl_num_aciertos.setText("N. d'encerts = ")
        myapp2.ui.lbl_logo.setPixmap(pixmap.scaled(self.ui.lbl_logo.size(),
                                                     QtCore.Qt.KeepAspectRatio,
                                                     QtCore.Qt.SmoothTransformation))
        myapp2.ui.num_aciertos.setText("")
        
    # --  Método para hacer un duplicado de la ventana, con opción a input oculto por asteriscos
    def duplicar(self):
        
        global ruta
        
        # Carga Logo de la ruta en el duplicado
        pixmap = QPixmap(ruta)
        myapp2.ui.lbl_logo.setPixmap(pixmap.scaled(self.ui.lbl_logo.size(),
                                                     QtCore.Qt.KeepAspectRatio,
                                                     QtCore.Qt.SmoothTransformation))
        myapp2.show() # Mostramos la segunda instancia de la clase MyForm(), el duplicado
        
    # -- Método para controlar el cierre de la ventana principal
    def closeEvent(self, event):
        
        # respuesta = QMessage.Box.question(self, título, pregunta, Botones, Botón por defecto) 
        reply = QMessageBox.question(self, 'Sortir', 'Segur que vol tancar aquesta finestra?', 
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
            myapp2.close() # También cierra la ventana del duplicado y otras
            VentanaInstruccions.close()
            VentanaCredits.close()
            #TempsCronometre.close()
            print('Windows closed')
        else:
            event.ignore()
    
    # -- Método para cargar Logo con la acción del submenú actionCarregar_Logo
    def carregar_Logo(self):
        
        global ruta, info_dialog
        
        # Obtenemos ruta del logo y la cargamos en un QPixmap
        info_dialog=QFileDialog.getOpenFileName(self,
                "Obrir arxiu d'imatge","~/pCloudDrive/projects-python/pyqt_projects/pi_concurso","Archivos de imagen (*.png *.jpg *.bmp)")
        ruta=info_dialog[0]
        pixmap = QPixmap(ruta)
        self.ui.lbl_logo.setPixmap(pixmap.scaled(self.ui.lbl_logo.size(),
                                                     QtCore.Qt.KeepAspectRatio,
                                                     QtCore.Qt.SmoothTransformation))
        
        # Escribimos la ruta del nuevo Logo en el archivo INI
        EscribirArchivoINI1(ruta)
        # EscribirArchivoINI("~/pCloudDrive/projects-python/pyqt_projects/pi_concurso/pi.png")
        
        
    def MostrarInstruccions(self):
        VentanaInstruccions.show()
        
    
    def MostrarCredits(self):
        VentanaCredits.show()
        
    def MostrarLlicencia(self):
        VentanaLlicencia.show()
    
    def MostrarTempsCronometre(self):
        VentanaTempsCronometre.show()
        
    
class MyForm2(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.mens_error.setStyleSheet("color: red")
        self.ui.num_aciertos.setStyleSheet("color: green")
        self.ui.lbl_num_aciertos.setText("N. d'encerts = ")
        self.ui.mens_error.setText("")
        self.ui.num_aciertos.setText("")
        self.ui.input.setText("")
        self.ui.input.setFocus()
        self.ui.cronometre.setStyleSheet("background-color: orange;border-radius : 3; font-weight: bold;border : 2px solid white")
        self.ui.Flag_Sonido.setCheckState(False) # Es True de origen
        
        #Lee la ruta del Logo en archivo INI y lo carga en la imagen.
        RutaLeida, temps = LeerArchivoINI()
        if RutaLeida:
            pixmap = QPixmap(RutaLeida)
            self.ui.lbl_logo.setPixmap(pixmap.scaled(self.ui.lbl_logo.size(),
                                                     QtCore.Qt.KeepAspectRatio,
                                                     QtCore.Qt.SmoothTransformation))
        
        # Ocultamos algunos widgets en el duplicado
        self.ui.iniciar.hide()
        self.ui.duplicar.hide()
        self.ui.Flag_Sonido.hide()
        self.ui.Flag_TextoOculto.hide()
        self.ui.menubar.hide()
        
class Instruccions(QtWidgets.QWidget):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.ui = Ui_Instruccions()
        self.ui.setupUi(self)
        
class Credits(QtWidgets.QWidget):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.ui = Ui_Credits()
        self.ui.setupUi(self)
        
class Llicencia(QtWidgets.QWidget):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.ui = Ui_Llicencia()
        self.ui.setupUi(self)
        
class TempsCronometre(QtWidgets.QWidget):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.ui = Ui_Temps()
        self.ui.setupUi(self)
        self.ui.lineEdit.setText(t_cuentaatras) # t_cuentaatras (=temps), leído del archivoINI en el iniciador de MyForm().
        self.ui.lineEdit.setFocus()
    # Al cerrar, preguntamos si se desea guardar el nuevo tiempo.
    def closeEvent(self, event):
        # respuesta = QMessage.Box.question(self, título, pregunta, Botones, Botón por defecto) 
        reply = QMessageBox.question(self, 'Tancar', 'Desar canvis abans de tancar?', 
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            tt=self.ui.lineEdit.text()
            EscribirArchivoINI2(tt)
            self.close()
        else:
            event.accept()
            self.close()
        

# BLOQUE PRINCIPAL

# Si este .pyw se ejecuta como programa principal, e.g., python pi_concurso.bck.pyw,
# entonces, el valor del atributo __name__ se pasa a la cadena "__main__"
# y se ejecuta el código del condicional.
# Si no fuera así y este .pyw es llamado desde otro, como un módulo importado,
# entonces __name__ es el nombre del módulo y no se ejecutará el código del condicional

if __name__ == "__main__":
    appctxt = ApplicationContext()       # 1. EMPAQUETAMIENTO FBS
    #app = QtWidgets.QApplication(sys.argv) # EMPAQUETAMIENTO FBS
    myapp = MyForm() # Instancia principal de la clase MyForm()
    myapp2 = MyForm2() # El duplicado, instancia de MyForm2(), que se construye como MyForm().
    VentanaInstruccions = Instruccions()
    VentanaCredits = Credits()
    VentanaLlicencia = Llicencia()
    VentanaTempsCronometre = TempsCronometre()
    myapp.show() # Mostramos la instancia principal.
    exit_code = appctxt.app.exec()       # 2. EMPAQUETAMIENTO FBS
    sys.exit(exit_code) # EMPAQUETAMIENTO FBS
    #sys.exit(app.exec_()) #EMPAQUETAMIENTO FBS

    
    