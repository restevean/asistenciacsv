"""
Esta es una aplicación para abrir un archivo CSV generado por Teams con la lista
de asistentes de una reunión, procesarlos y producir un archivo CSV de salida
con el resultado del proceso
"""

import csv
from csv import reader as readcsv
from datetime import datetime


def parse(contenido_csv_param):
    """
    :type contenido_csv_param: list
    """
    finalreuniont = 'Final'
    lend = False  # Asistente no tiene linea de final

    # Procesamos el encabezado de archivo.csv
    cabecera = next(contenido_csv_param)
    # Cargamos el contenido leído en la lista
    listadeasistencia = list(contenido_csv_param)
    # Asignamos la cabecera a la primera linea de la nueva lista
    listanueva = [cabecera]
    listanueva[0].append('T. Efectivo')
    # Append first row
    listadeasistencia[0][2] = datetime.strptime(listadeasistencia[0][2], '%d/%m/%Y %H:%M:%S')
    listanueva.append(listadeasistencia[0])
    listanueva[1].append('')
    # Asignamos las variables de inicio reunión
    inicioreunion = listanueva[1][2]
    finalreunion = listanueva[1][2]
    t1 = listanueva[1][2]

    print('Parsing data...')

    # Procesamos la lista
    # 1ª vuelta
    for linea in listadeasistencia:
        if type(linea[2]) == str:
            linea[2] = datetime.strptime(linea[2], '%d/%m/%Y %H:%M:%S')

        if linea[0] != listanueva[len(listanueva) - 1][0]:
            if listanueva[len(listanueva) - 1][1] == 'Unido':
                listanueva.append([listanueva[len(listanueva) - 1][0], 'Abandonó', finalreuniont, ''])
                lend = True

            if linea[1] == 'Se unió antes':
                listanueva.append([linea[0], "Unido", inicioreunion, ''])
                lend = False
            elif linea[1] == 'Unido':
                listanueva.append([linea[0], linea[1], linea[2], ''])
                lend = False
            elif linea[1] == 'Abandonó':
                listanueva.append([linea[0], "Unido", inicioreunion, ''])
                listanueva.append([linea[0], "Abandonó", linea[2], ''])
                lend = True

        elif linea[0] == listanueva[len(listanueva) - 1][0]:
            if linea[1] == 'Unido':
                lend = False
            elif linea[1] == 'Abandonó':
                if listanueva[len(listanueva) - 1][1] == 'Unido':
                    if linea[1] == 'Abandonó':
                        listanueva.append([linea[0], linea[1], linea[2], ''])
                        lend = True
                    elif linea[1] == 'Unido':
                        lend = False
                elif listanueva[len(listanueva) - 1][1] == 'Abandonó':
                    listanueva[len(listanueva) - 1][2] = linea[2]
                    lend = True

        if finalreunion < linea[2]:
            finalreunion = linea[2]

    if not lend:
        if listanueva[len(listanueva) - 1][1] == 'Unido':
            listanueva.append([listanueva[len(listanueva) - 1][0], 'Abandonó', finalreuniont, ''])
        elif listanueva[len(listanueva) - 1][1] == 'Abandonó':
            listanueva[len(listanueva) - 1][2] = finalreuniont

    # 2ª vuelta
    for lineaN in listanueva:
        # Si no tiene tiempo de inicio le asignamos el inicio de la reunión
        if lineaN[2] == 'Inicio':
            lineaN[2] = inicioreunion

        # Si no tiene tiempo de fin, le asignamos el final de la reunión
        elif lineaN[2] == 'Final':
            lineaN[2] = finalreunion

        if lineaN[1] == 'Unido':
            t1 = lineaN[2]
        elif lineaN[1] == 'Abandonó':
            t2 = lineaN[2]
            # Calculamos el tiempo efectivo desde que entró hasta que salió
            pepe = t2 - t1
            lineaN[3] = pepe

    return listanueva


# Abrimos el archivo.csv
print('Reading csv file...')
with open("fixtures/2021-02-25.csv", encoding='utf-16') as csvfile:
    # Lo leemos con csv.Reader()
    contenidocsv: readcsv = csv.reader(csvfile, dialect='excel-tab')
    parsedlist = parse(contenidocsv)  # Recibimos la lista procesada

# Escribimos listaNueva en un archivo .csv delimitado por tabulaciones
with open("output.csv", 'w', encoding='utf-16') as csvFileOutput:
    # Lo escribimos con csv.Writter()
    contenidoNuevo = csv.writer(csvFileOutput, dialect='excel-tab')

    print('Writting csv file: output.csv')
    # Escribimos todas las líneas
    for evento in parsedlist:
        contenidoNuevo.writerow(evento)

print("Done ;)")
