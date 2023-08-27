### Dictionaries ###

my_dict = dict()

my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Brais", "Apellido":"Moure", "Edad":35, 1:"Python"}

my_dict = {
    "Nombre":"Brais",
    "Apellido":"Moure",
    "Edad":35, 
    "Lenguajes":{"Python", "Swift", "Kotlin"},
    1:1.77
}

# Diccionario tipo de estructura de datos de almacenamiento de tipo clave:valor

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])

# Reasignando el valor a la variable
my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

print(my_dict[1])

# Agregar un nuevo campo al diccionario
my_dict["Calle"] = "MoureDev"
print(my_dict)

# Eliminar un elemento del diccionario
del my_dict["Calle"]
print(my_dict)

# Esto solo busca en las claves
print("Moure" in my_dict) 
print("Apellido" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())


my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)
