### Dates ###

# import datetime
# Así es más fácil acceder a las funciones del módulo
from datetime import datetime 

# Una fecha es un objeto que representa un espacio de tiempo

now = datetime.now()

# print(now.year) # Año
# print(now.month) # Mes
# print(now.day) # Día
# print(now.hour) # Hora formato 24
# print(now.minute) # minuto
# print(now.second) # segundo

# Representación única de un tiempo
timestamp = now.timestamp() 
print(timestamp)

year_2024 = datetime(2024, 1, 1)

def print_date (date):
    print(date.year) 
    print(date.month) 
    print(date.day) 
    print(date.hour) 
    print(date.minute) 
    print(date.second) 
    print(date.timestamp())
    
print_date(now)
print_date(year_2024)

from datetime import time

# Creando una hora
current_time = time(now.hour, now.minute, now.second) 

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(1989, 11, 12) # Creando una fecha

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year + 34, current_date.month, current_date.day)

print(current_date.month)

diff = year_2024 - now
print(diff)

diff = year_2024.date() - current_date
print(diff)

print(year_2024.time())

from datetime import timedelta

time_delta = timedelta()

print()