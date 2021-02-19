"""
Esta es una aplicación para abrir un archivo CSV generado por Teams con la lista
de asistentes de una reunión, procesarlos y producir un archivo CSV de salida
con el resultado del proceso
"""

import csv

with open("file.csv") as csvfile:
    reader = csv.reader(csvfile)
    for fileLine in reader:
        print(fileLine)

