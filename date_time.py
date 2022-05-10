from datetime import datetime

date_string = "9/28/2021, 8:59:32 PM"

print(f'Lafecha en formato incorrecto es: {date_string}')
print(f'Es un dato tipo:  {type(date_string)}')

# Leemos la fecha
date_object = datetime.strptime(date_string, "%m/%d/%Y, %I:%M:%S %p")

print("date_object =", date_object)
print("type of date_object =", type(date_object))

# La escribimos en el formato adecuado
str_fecha = date_object.strftime("%d/%m/%Y %H:%M:%S")
print(str_fecha)
