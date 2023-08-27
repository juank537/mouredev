# Saber si un número es par o impar
# SOLUCIÓN CON OPERADOR TERNARIO, menos líneas de código
# num = int(input("¿En qué número estás pensando? "))
# print(f'{num} es par.') if num % 2 == 0 else print(f'{num} es impar.')


### SOLUCIÓN SENCILLA
# num = int(input("Inserte un número: "))
# if num % 2 == 0:
#     print(f'{num} es par.')
# else:
#     print(f'{num} es impar.')

# Función de par o impar
def odd_even(n):
    print(f'{n} es par.') if n % 2 == 0 else print(f'{n} es impar.')
    

num = int(input('¿En qué número estás pensando? '))
while num:
    num = int(input("¿En qué número estás pensando? "))
    print(f'{num} es par.') if num % 2 == 0 else print(f'{num} es impar.')
print('Gracias por utilizar nuestro programa.')    