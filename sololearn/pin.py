# Ejercicio de Excepciones. Crear PIN
pin = input("Inserte su PIN: ")

try:
    int(pin)
    print("PIN code is created!")
except ValueError:
    print("Please enter a number.")
    