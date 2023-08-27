from datetime import datetime

# fecha = datetime.date(2022, 12, 31)

# dia_programador = fecha + datetime.timedelta(days=256)
# # for i in range(1, 257):
# #     dia_programador = fecha + datetime.timedelta(days=i)
# #     print(f"Hoy es el día número {i} y la fecha es {dia_programador}")
# print('Felicidades programadores')


# Calcular cantidad de días que faltan para un fecha
# d0 = datetime.date.today()
# d1 = datetime.date(2023, 11, 12)
# delta = d1 - d0
# print(delta)
# print(f'Faltan {delta.days} días para tu cumpleaños.')

# date_format = "%m/%d/%Y"

# a = datetime.strptime('5/4/2023', date_format)
# b = datetime.strptime('11/12/2023', date_format)

# delta = b - a

# print(delta.days) 


def diff_btw_hoy_fecha_dias(d, m, a):
    '''
    Calcular la cantidad de días entre el día de hoy y otra fecha
    Se debe insertar los valores de la fecha
    '''
    today = datetime.date.today()
    someday = datetime.date(a, m, d)
    diff = someday - today
    return diff.days

# diff = diff_btw_hoy_fecha_dias(12, 11, 2023)


# print(f"Faltan {diff_btw_hoy_fecha_dias(1, 6, 2023)} días para la fecha.")

def crear_fecha(fecha):
    fecha = datetime.strptime(fecha, "%d/%m/%Y")
    return fecha

# fecha_inp = input('Inserte la fecha d/m/y: ')

# print(crear_fecha(fecha_inp))


'''
Datetime.replace() function is used to replace the contents of the DateTime object with the given parameters.

    Syntax: Datetime_object.replace(year,month,day,hour,minute,second,microsecond,tzinfo)

    Parameters:

        year: New year value in range-[1,9999],
        month: New month value in range-[1,12],
        day: New day value in range-[1,31],
        hour: New hour value in range-[24],
        minute: New minute value in range-[60],
        second: New second value in range-[60],
        microsecond: New microsecond value in range-[1000000],
        tzinfo: New time zone info.

    Returns: It returns the modified datetime object
    
'''

# importing the datetime module
# import datetime
  
# Getting current date using today()
# function of the datetime class
todays_date = datetime.date.today()
print("Original Date:", todays_date)
  
# Replacing the todays_date year with
# 2000 using replace() function
modified_date = todays_date.replace(year=2000)
print("Modified Date:", modified_date)