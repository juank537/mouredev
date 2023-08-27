### List Comprehension ###

my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]

my_range = range(8)
print(list(my_range))

my_list = [i + 1 for i in range(8)]
print(my_list)

# el doble de cada elemento
my_list = [i * 2 for i in range(8)]
print(my_list)

# el cuadrado de cada elemento
my_list = [i * i for i in range(8)]
print(my_list)


# Llenando la lista modificada por una función
# Esto se puede utilizar para encriptar - desencriptars un texto
def sum_five(number):
    return number + 5

my_list = [sum_five(i) for i in range(8)]
print(my_list)