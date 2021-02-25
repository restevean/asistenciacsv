"""
Esta es una aplicación para abrir un archivo CSV generado por Teams con la lista
de asistentes de una reunión, procesarlos y producir un archivo CSV de salida
con el resultado del proceso
"""

import csv
from datetime import datetime

def parse(contenidoCsvParam):

    inicioreunion = 'Inicio'
    finalreuniont = 'Final'

    # Procesamos el encabezado de archivo.csv
    cabecera = next(contenidoCsvParam)
    # Cargamos el contenido leído en la lista
    listaDeAsistencia = list(contenidoCsvParam)
    # Asignamos la cabecera a la primera linea de la nueva lista
    listaNueva = [cabecera]
    listaNueva[0].append('')
    # Añadimos la primera linea de datos
    listaDeAsistencia[0][2] = datetime.strptime(listaDeAsistencia[0][2], '%d/%m/%Y %H:%M:%S')
    listaNueva.append(listaDeAsistencia[0])
    listaNueva[1].append('')
    inicioreunion = listaNueva[1][2]
    finalreunion = listaNueva[1][2]

    print('Parsing data...')

    # Procesamos la lista
    # 1ª vuelta
    for linea in listaDeAsistencia:

        # Convertimos el último elemento en datetime
        if type(linea[2]) == str:
            linea[2] = datetime.strptime(linea[2], '%d/%m/%Y %H:%M:%S')

        # Asignamos el nombre
        nombreAsistente = linea[0]
        # Asignamos la acción
        accion = linea[1]

        # Si el nombre anterior es distinto
        if nombreAsistente != listaNueva[len(listaNueva) - 1][0]:
            # Si la acción == Se unió antes
            if linea[1] == 'Se unió antes':
                linea[1] = 'Unido'
                linea[2] = inicioreunion
                listaNueva.append([linea[0], "Unido", inicioreunion, ''])
            # Si la acción == 'Unido'
            elif linea[1] == 'Unido':
                if listaNueva[len(listaNueva) - 1][1] == 'Unido' or listaNueva[len(listaNueva) - 1][1] == 'Acción del usuario':
                    listaNueva.append([listaNueva[len(listaNueva) - 1][0], 'Abandonó', finalreuniont, ''])
                    listaNueva.append([linea[0], linea[1], linea[2], ''])
            # Si la acción == 'Abandonó'
            elif linea[1] == 'Abandonó':
                listaNueva.append([linea[0], 'Unido', inicioreunion, ''])
                listaNueva.append([linea[0], 'Abandonó', linea[2], ''])
        if nombreAsistente == listaNueva[len(listaNueva) - 1][0]:
            if linea[1] == 'Abandonó':
                if listaNueva[len(listaNueva) - 1][1] == 'Abandonó':
                    listaNueva[len(listaNueva) - 1][2] = linea[2]
                else:
                    listaNueva.append([linea[0], linea[1], linea[2], ''])

        if listaNueva[len(listaNueva) - 1][2] > finalreunion:
            finalreunion = listaNueva[len(listaNueva) - 1][2]

    # 2ª vuelta
    for lineaN in listaNueva:
        # Si no tiene tiempo de inicio le asignamos el inicio de la reunión
        if lineaN[2] == 'Inicio':
            lineaN[2] = inicioreunion
        # Si no tiene tiempo de fin, le asignamos el final de la reunión
        elif lineaN[2] == 'Final':
            lineaN[2] = finalreunion

    return listaNueva

# Abrimos el archivo.csv
print('Reading csv file...')
with open("fixtures/file0.csv", encoding='utf-16') as csvfile:
    # Lo leemos con csv.Reader()
    contenidoCsv = csv.reader(csvfile, dialect='excel-tab')

    listaParseada = parse(contenidoCsv)

# Escribimos listaNueva en un archivo .csv delimitado por tabulaciones
with open("output.csv", 'w', encoding='utf-16') as csvFileOutput:
    # Lo escribimos con csv.Writter()
    contenidoNuevo = csv.writer(csvFileOutput, dialect='excel-tab')

    print('Writting csv file: output.csv')
    # Escribimos todas las líneas
    for evento in listaParseada:
        contenidoNuevo.writerow(evento)

print("Done ;)")