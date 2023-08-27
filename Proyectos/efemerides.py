import datetime
from my_dictionaries import meses

#VARIABLES GLOBALES DE FECHAS
HOY = datetime.date.today()
ACTUAL_YEAR = HOY.year

# Día del programador o día 256
PROGRAMMER_DAY = datetime.date(ACTUAL_YEAR, 1, 1) + datetime.timedelta(days=255)
   
# Día Pi
PI_DAY = datetime.date(ACTUAL_YEAR, 4, 3)

# 420, el día del Masarreal :D
DAY_420 = datetime.date(ACTUAL_YEAR, 4, 20)

#  mes = meses.get(dia_programador.month)
# print(f'El día del programador es el {dia_programador.day} de {mes}. Día 256 del {dia_programador.year}.')
    
