#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" Este módulo contiene colores en código ANSI """
__author__ = "José Rodolfo"
__copyright__ = "Copyright 2020, JRIC2002"
__credits__ = "JRIC2002"
__license__ = "GNU General Public License v3.0"
__version__ = "1.0"
__maintainer__ = "JRIC2002"
__email__ = "example@gmail.com"
__status__ = "Production"

class Color:
    """ Colores en código ANSI """

    #Styles
    reset = "\033[0m"
    bold = "\033[1m"
    dark = "\033[2m"
    italic = "\033[3m"
    underline = "\033[4m"
    reverse = "\033[7m"
    hidden = "\033[8m"

    #Foreground
    black= "\033[30m"
    gray = "\033[1;30m"
    red= "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    magenta = "\033[35m"
    cyan = "\033[36m"
    white = "\033[37m"

    #Background
    bgBlack = "\033[40m"
    bgRed = "\033[41m"
    bgGreen = "\033[42m"
    bgYellow = "\033[43m"
    bgBlue = "\033[44m"
    bgMagenta = "\033[45m"
    bgCyan = "\033[46m"
    bgWhite = "\033[47m"

#Instancia de la clase Color
color = Color()

if __name__ == "__main__":
    print("Este archivo es un módulo...")