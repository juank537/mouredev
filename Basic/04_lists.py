### Lists ###

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, "Brais", "Moure"]

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])

# IndexError:
# print(my_other_list[4]) 
# print(my_other_list[-5]) 

# count se utiliza para contar la cantidad de incidencias de un elemento
print(my_list.count(30))

# Esto no es recomendable
age, height, name, surname = my_other_list
print(age)

name, age, surname, height = my_other_list[2], my_other_list[0], my_other_list[3], my_other_list[1]
print(name)

# Concatenación de listas
print(my_list + my_other_list)

# Agregar un elemento a la lista
my_other_list.append("MoureDev")
print(my_other_list)

# Insertar un elemento en una lista, se le pasa el índice y el elemento
my_other_list.insert(1, "Rojo")
print(my_other_list)

my_other_list[1] = "Azul"
print(my_other_list)

my_other_list.remove("Azul")
print(my_other_list)

my_list.remove(30)
print(my_list)

# Elimina y devuelve el último elemento por defecto, pero se le puede 
# pasar el índice del elemento que se quiera eliminar
print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2]
print(my_list)

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

# invertir una lista
my_new_list.reverse()
print(my_new_list)
# Se puede utilizar el [::-1]
print(my_new_list[::-1])

# ordenar una lista
my_new_list.sort()
print(my_new_list)
my_new_list.sort(reverse=True)
print(my_new_list)