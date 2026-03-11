# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Pi-Day v.1.1.1
# Copyright (C) 2026 Juan Luis Rubio López
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, version 3.
#
# See the LICENSE file for details.
'''
===============================
Módulo con funciones útiles
===============================

EsNumerico -> Test booleano. ¿El string <cadena> es numérico?
LeerArchivoINI -> Lee el archivo de configuración <archivoINI>. Devuelve dos parámetros
EscribirArchivoINI1,2 -> Escribe en el archivo de configuración <archivoINI>

Julio-Agosto de 2021, Terrassa.
by Rubio, J. L.
=========================================================================
'''


import os
import configparser
from pathlib import Path

config = configparser.ConfigParser()

fichero = 'myfile.ini'
seccion = 'main'
clave1 = 'pathLogo'
clave2 = 'temps'


APP_NAME = "Pi-Day"

config_dir = Path(os.getenv("APPDATA")) / APP_NAME
config_dir.mkdir(parents=True, exist_ok=True)

ini_path = config_dir / fichero



def CrearArchivoINI():

    if not ini_path.exists():

        config[seccion] = {
            clave1: "",
            clave2: "10"
        }

        with open(ini_path, "w") as configfile:
            config.write(configfile)



def LeerArchivoINI():

    CrearArchivoINI()

    config.read(ini_path)

    RutaLeida = config.get(seccion, clave1)
    temps = config.get(seccion, clave2)

    return RutaLeida, temps



def EscribirArchivoINI1(valor):

    CrearArchivoINI()

    config.read(ini_path)

    config.set(seccion, clave1, valor)

    with open(ini_path, 'w') as configfile:
        config.write(configfile)



def EscribirArchivoINI2(valor):

    CrearArchivoINI()

    config.read(ini_path)

    config.set(seccion, clave2, valor)

    with open(ini_path, 'w') as configfile:
        config.write(configfile)


# --------------------------------------------------
# Comprobar si cadena es numérica
# --------------------------------------------------

def EsNumerico(cadena):

    try:
        int(cadena)
        return True
    except (TypeError, ValueError):
        return False