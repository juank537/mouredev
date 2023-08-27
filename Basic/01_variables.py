# Variables
# Se recomienda usar snake_case para definir variables
my_string_variable= 'My String variable'
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

# Concatenación de variables en un print
print(my_string_variable, my_int_variable, my_bool_variable)
print("Este es el valor:", my_bool_variable)

# Algunas funciones del sistema
print(len(my_string_variable))

# Variables en una sola línea
name, surname, alias, age = "Brais", "Moure", "MoureDev", 35
print("Me llamo:", name, surname, ". Mi edad es:", age, '. Y mi alias es:', alias)     

# Inputs
"""
name = input('¿Cuál es tu nombre? ')                                  
age = input('¿Cuántos años tienes? ')                                  
print(name)
print(age)
"""

# Cambiamos su tipo
name = 35
age = "Brais"
print(name)
print(age)

# ¿Forzamos el tipo?
address: str = "Mi dirección"
address: int = 32
print(type(address))