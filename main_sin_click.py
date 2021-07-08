"""
Esta es una aplicación para abrir un archivo CSV generado por Teams con la lista
de asistentes de una reunión, procesarlos y producir un archivo CSV de salida
con el resultado del proceso
"""

import csv
from csv import reader as readcsv
from parsers import parse_row, ServiceRecord
from errors import HeaderException


def main():
    file: str = "file"
    print('Copyrigth© 2021 Rafael Esteve Antonino')
    print('Todos los derechos reservados')

    while True:
        file = input("Introduce el nombre del archivo ('q' para salir): ")
        if file == "Q" or file == "q":
            break
        # controlamos la extensión del nombre de archivo, puede no llevarla o llevarla mal escrita
        if file[len(file) - 4: len(file) - 3: 1] == ".":
            if file[len(file) - 3: len(file): 1] != "csv":
                # file[len(file) - 3:len(file):1] = 'csv'
                file = file[0: len(file) - 3: 1] + "csv"
        else:
            file = file + ".csv"

        try:
            print("Leyendo lista...")
            parsed_list = []
            counter = 0
            with open(file, encoding="utf-16") as csvfile:
                # Lo leemos con csv.Reader()
                contenidocsv: readcsv = csv.reader(csvfile, dialect="excel-tab")

                for linea in contenidocsv:
                    try:
                        parsed_list.append(parse_row(linea, counter))
                    except HeaderException:
                        # cabecera = linea
                        # cabecera.append('T. Efectivo')
                        # next(contenidocsv)
                        ...
                    counter += 1

            service = ServiceRecord(parsed_list)
            with open(f"P {file}", "w", encoding="utf-16") as csvFileOutput:
                writer = csv.writer(csvFileOutput)
                attendees = service.get_names()
                # writer.writerow(cabecera)
                for attendee in attendees:
                    data = [
                        attendee,
                        service.get_joined_time(attendee).isoformat(),
                        service.get_leaving_time(attendee).isoformat(),
                        service.get_leaving_time(attendee) - service.get_joined_time(attendee)
                    ]
                    writer.writerow(data)

            print("Hecho ;)")
        except FileNotFoundError:
            print("**********************************")
            print("*** No se encuentra el archivo ***")
            print("**********************************")


if __name__ == "__main__":
    main()
