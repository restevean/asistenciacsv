"""
Esta es una aplicación para abrir un archivo CSV generado por Teams con la lista
de asistentes de una reunión, procesarlos y producir un archivo CSV de salida
con el resultado del proceso
"""

import csv
from datetime import datetime

def parse(contenidoCsvParam):
    listaNueva = [['Nombre completo', 'Acción del usuario', 'Marca de tiempo']]
    inicioReunion = 0
    finalReunion = 'Final'

    # Omitimos el encabezado del archivo .csv
    next(contenidoCsvParam)

    # Cargamos el contenido leído en la lista
    listaDeAsistencia = list(contenidoCsvParam)

    print('Parsing data...')

    # Procesamos la lista
    for linea in listaDeAsistencia:

        # Convertimos el último elemento en datetime
        linea[2] = datetime.strptime(linea[2], '%d/%m/%Y %H:%M:%S')

        # Si no hay inicio de reunión, asignamos el tiempo de inicio de la reunión
        if inicioReunion == 0:
            inicioReunion = linea[2]

        # Tomamos la cabecera
        cabeceraArchivo = listaDeAsistencia[0]
        # Asignamos el nombre
        nombreAsistente = linea[0]
        # Asignamos la acción
        accion = linea[1]
        # asignamos el tiempo de inicio de la reunión
        tiempoInicioReunion = linea[2]

        # Si el nombre anterior es distinto
        if nombreAsistente != listaNueva[len(listaNueva) - 1][0]:
            # Si la acción == Se unió antes
            if linea[1] == 'Se unió antes':
                linea[1] = 'Unido'
                linea[2] = tiempoInicioReunion
                listaNueva.append([linea[0], "Unido", TI, ''])
            # Si la acción == 'Unido'
            elif linea[1] == 'Unido':
                if listaNueva[len(listaNueva) - 1][1] == 'Unido':
                    listaNueva.append(
                        [listaNueva[len(listaNueva) - 1][0], 'Abandonó', listaNueva[len(listaNueva) - 1][2], 'TF'])
                listaNueva.append([linea[0], linea[1], linea[2], ''])
            # Si la acción == 'Abandonó'
            elif linea[1] == 'Abandonó':
                listaNueva.append([linea[0], 'Unido', TI, ''])
                listaNueva.append([linea[0], 'Abandonó', linea[2], ''])
        if nombreAsistente == listaNueva[len(listaNueva) - 1]:
            if linea[1] == 'Abandonó':
                listaNueva.append([linea[0], linea[1], linea[2], ''])

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