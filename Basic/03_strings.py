### Strings ###

my_string = 'Mi String'
my_other_string = "Mi otro string"

print(len(my_string))
print(len(my_other_string))

print(my_string + ' ' + my_other_string)

my_new_line_string = 'Estes un string\ncon salto de línea'
print(my_new_line_string)

my_tab_string = '\tEste es un string con tabulación'
print(my_tab_string)

my_scape_string = '\\tEste es un string con \\n escapado'
print(my_scape_string)


### Formateo
 
name, surname, age = 'Juan Carlos', 'Aliaga', 33

#Es recomendable utilizar este estilo de formato antes que la concatenación simple con variables
#Esto se utiliza mucho en la internacionalización de los proyectos
print('Mi nombre es {} {} y tengo {} años.'.format(name, surname, age))
print('Mi nombre es %s %s y tengo %d años.' %(name, surname, age)) 
#Ejemplo con la concatenación, menos recomendado
print('Mi nomnbre es ' + name + ' ' + surname + ' y tengo ' + str(age) + ' años.')

#Formato con inferencia de datos
print(f'Mi nombre es {name} {surname} y tengo {age} años.') #ESTE ES EL FORMATO MÁS RECOMENDADO

# Desempaquetado de caracteres

language = "Python"
a, b,c, d, e, f = language
print(a)
print(e)

# División 

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)


# Reverse (Invertir string)

reversed_language = language[::-1]
print(reversed_language)

# Funciones

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print("1".isnumeric())
print(language.isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.startswith("Py"))
print("Py" == "py") # no es lo mismo

