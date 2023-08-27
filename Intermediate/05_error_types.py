### Error Types ###
 
# SyntaxError
#print "¡Hola comunidad!" # Descomentar para Error
print("¡Hola comunidad!")

# NameError
language = "Spanish" # Comentar para Error
print(language)

# IndexError
my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
#print(my_list[5]) # Descomentar para Error
print(my_list[-1])

# ModuleNotFoundError
# import maths # Descomentar para Error
import math

# AttributeError
# print(math.PI) # Descomentar para Error
print(math.pi)

# KeyError
my_dict = {"Nombre": "Juan Carlos", "Apellido":"Aliaga", "Edad": 33}
print(my_dict["Edad"])
#print(my_dict["Apelido"]) # Descomentar para Error

# TypeError
#print(my_list["Nombre"]) # Descomentar para Error
print(my_list[0])

# ImportError
# from math import PI # c
from math import pi
print(pi)

# ValueError
#my_int = int("10 Años") # Descomentar para Error
my_int = int("10")
print(type(my_int))

# ZeroDivisionError
print(4/2)
#print(4/0) # Descomentar para Error