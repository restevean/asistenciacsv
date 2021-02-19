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

# Supongo que es un tema del dialecto del CSV, está delimitado por TAB en lugar de por comas",
# no encuentro donde decirle que es un CSV de estilo excel
