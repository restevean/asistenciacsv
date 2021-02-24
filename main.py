"""
Esta es una aplicación para abrir un archivo CSV generado por Teams con la lista
de asistentes de una reunión, procesarlos y producir un archivo CSV de salida
con el resultado del proceso
"""

import csv
from datetime import datetime

listaNueva = [['Nombre completo', 'Acción del usuario', 'Marca de tiempo']]
inicioReunion = 0
finalReunion = 'Final'

# Abrimos el archivo .csv
print('Reading csv file...')
with open("fixtures/file0.csv", encoding='utf-16') as csvfile:
    # Lo leemos con csv.Reader()
    contenidoCsv = csv.reader(csvfile, dialect='excel-tab')

    # Omitimos el encabezado del archivo .csv
    next(contenidoCsv)

    # Cargamos el contenido leído en la lista
    listaDeAsistencia = list(contenidoCsv)

    print('Parsing data...')

    # Procesamos la lista
    for evento in listaDeAsistencia:

        # Convertimos el último elemento en datetime
        evento[2] = datetime.strptime(evento[2], '%d/%m/%Y %H:%M:%S')

        # Si no hay inicio de reunión, asignamos el tiempo de inicio de la reunión
        if inicioReunion == 0:
            inicioReunion = evento[2]

        # Tomamos la cabecera
        cabeceraArchivo = listaDeAsistencia[0]
        # Asignamos el nombre
        nombreAsistente = evento[0]
        # Asignamos la acción
        accion = evento[1]
        # asignamos el tiempo de inicio de la reunión
        tiempoInicioReunion = evento[2]

        # Si el nombre anterior es distinto
        if nombreAsistente != listaNueva[len(listaNueva) - 1][0]:
            # Si la acción == Se unió antes
            if evento[1] == 'Se unió antes':
                evento[1] = 'Unido'
                evento[2] = tiempoInicioReunion
                listaNueva.append([evento[0], "Unido", TI, ''])
            # Si la acción == 'Unido'
            elif evento[1] == 'Unido':
                if listaNueva[len(listaNueva) - 1][1] == 'Unido':
                    listaNueva.append(
                        [listaNueva[len(listaNueva) - 1][0], 'Abandonó', listaNueva[len(listaNueva) - 1][2], 'TF'])
                listaNueva.append([evento[0], evento[1], evento[2], ''])
            # Si la acción == 'Abandonó'
            elif evento[1] == 'Abandonó':
                listaNueva.append([evento[0], 'Unido', TI, ''])
                listaNueva.append([evento[0], 'Abandonó', evento[2], ''])
        if nombreAsistente == listaNueva[len(listaNueva) - 1]:
            if evento[1] == 'Abandonó':
                listaNueva.append([evento[0], evento[1], evento[2], ''])

# Escribimos listaNueva en un archivo .csv delimitado por tabulaciones
with open("output.csv", 'w', encoding='utf-16') as csvFileOutput:
    # Lo escribimos con csv.Writter()
    contenidoNuevo = csv.writer(csvFileOutput, dialect='excel-tab')

    print('Writting csv file: output.csv')
    # Escribimos todas las líneas
    for eventoN in listaNueva:
        contenidoNuevo.writerow(eventoN)

print("Done ;)")


def parse(contenidoCsv):


    return