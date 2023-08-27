### Exceptions Handling ###

numberOne = 5
numberTwo = 1
numberTwo = "1"

# try except

# try:
#     print(numberOne + numberTwo)
#     print("No se ha producido un error")
# except:
#     # Se ejecuta si se produce una excepción
#     print("Se ha producido un error")

    

# try except else

# try:
#     print(numberOne + numberTwo)
#     print("No se ha producido un error")
# except:
#     # Se ejecuta si se produce una excepción
#     print("Se ha producido un error")
# else:
#     # Se ejecuta si no se produce una excepción
#     print("La ejecución continúa correctamente")
    
    
# try except else finally

# try:
#     print(numberOne + numberTwo)
#     print("No se ha producido un error")
# except: # Opcional
#     #Se ejecuta si se produce una excepción
#     print("Se ha producido un error")
# else:
#     print("La ejecución continúa correctamente")
# finally: # Opcional
#     # Se ejecuta siempre
#     print("La ejecución continúa")

# Exceptions por tipo

# try:
#     print(numberOne + numberTwo)
#     print("No se ha producido un error")
# except ValueError as e:
#     print("Se ha producido un ValueError")
# except TypeError as e:
#     print("Se ha producido un TypeError")
#     print(e)

# Captura de la información de la información

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error:
    print(error)
except Exception as e:
    print(e)
