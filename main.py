"""
Esta es una aplicación para abrir un archivo CSV generado por Teams con la lista
de asistentes de una reunión, procesarlos y producir un archivo CSV de salida
con el resultado del proceso
"""

import csv

stop=0

# Abrimos el archivo .csv
with open("file.csv", encoding='utf-16') as csvfile:
    # Lo leemos con csv.Reader()
    contenidoCsv = csv.reader(csvfile, dialect='excel-tab')
    # Cargamos el contenido leído en la lista
    listaDeAsistencia = list(contenidoCsv)
    print('==============Lista==============')
    # Imprimimos la lista
    for evento in listaDeAsistencia:
        print(evento)

print("Done ;)")

# print("==============Segundo print==============")
# with open("file.csv", encoding='utf-16') as csvfile:
    # lo leemos con csv.DictReader()
    #     dict_reader = csv.DictReader(csvfile, dialect='excel-tab')
    # for element in dict_reader:
    #   print(element['Nombre completo'], element['Acción del usuario'], element['Marca de tiempo'])
