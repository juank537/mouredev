### Functions ###

"""
Las funciones se utilizan para encapsular una lógica concreta
Gracias a las funciones podemos agrupar una solución en un único lugar.
"""

def my_function ():
    print("Esto es un función")
    
my_function()

def sum_two_values (first_number: int, second_number: int):
    print(first_number + second_number)
    
sum_two_values(12, 20)
sum_two_values("12", "20")

def sum_two_values_with_return (first_value, second_value):
    my_sum = first_value + second_value
    return my_sum

my_result = sum_two_values_with_return(3, 4)
print(my_result)


def print_name (name, surname):
    print(f"{name} {surname}")
    
    
print_name(surname = "Aliaga", name = "Juan Carlos ")

def print_name_with_default (name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")
    
    
print_name_with_default("Juan Carlos", "Aliaga")

def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())
    
print_upper_texts("Hola", "Mundo", "función con varios argumentos ")
