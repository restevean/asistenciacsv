"""
Esta es una aplicación para abrir un archivo CSV generado por Teams con la lista
de asistentes de una reunión, procesarlos y producir un archivo CSV de salida
con el resultado del proceso
"""

import csv
from datetime import datetime

tiempoInicioReunion = 0 # Tiempo en que se inicia de la reunión
tiempoIFinalReunion = 0 # Tiempo en que finaliza la reunión

# Abrimos el archivo .csv
with open("file.csv", encoding='utf-16') as csvfile:
    # Lo leemos con csv.Reader()
    contenidoCsv = csv.reader(csvfile, dialect='excel-tab')
    # Cargamos el contenido leído en la lista
    listaDeAsistencia = list(contenidoCsv)

    tiempoInicioReunion = listaDeAsistencia

    # Imprimimos la lista
    for evento in listaDeAsistencia:
        # print(evento, 'last element is ', type(evento[2]), evento[2])
        # Convertimos el último elemento en datetime
        evento[2] = datetime.strptime(evento[2], '%d/%m/%Y %H:%M:%S')
        # no entiendo por qué no funciona el formato '%-d/%-m%Y %H:%M:%S'
        # print(evento, 'last element is ', type(evento[2]), evento[2])

print("Done ;)")
