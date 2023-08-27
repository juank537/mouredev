### Regular Expressions ###

import re

# match


my_string = "Esta es la lección número 7: Lección llamada Expresiones Regulares"
my_other_string = "Esta no es la lección número 6: Manejo de ficheros"

# match empieza a buscar desde el principio
match = re.match("Esta es la lección", my_string, re.I)
print(match)
# Captura la tupla que da el rango de la coincidencia 
start, end = match.span()
print(match.span())
print(my_string[start:end])

match = re.match("Esta no es la lección", my_other_string)
# varias formas de preguntar que no es None
# if not(match == None):
# if match != None: 
if match is not None:
    print(match)
    start, end = match.span()
    print(match.span())
    print(my_other_string[start:end])
else:
    print("No se encontraron coincidencias.")

print(re.match("Esta es la lección", my_other_string))
print(re.match("Expresiones Regulares", my_string))

# search
# Encuentra la primera ocurre la primera semejanza

search = re.search("lección", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])

# findall

findall = re.findall("lección", my_string, re.I)
print(findall)


# split

print(re.split(":", my_string))

# sub

print(re.sub("[l|L]ección", "LECCIÓN", my_string))
print(re.sub("Expresiones Regulares", "RegEx", my_string))

# Buscar tabla de expresiones regulares que Brais compartió en el video

# Patterns
# Para aprender y validar expresiones regulares: https://regex101.com

pattern = r'[l|L]ección'
print(re.findall(pattern, my_string))

pattern = r'[l|L]ección|Expresiones'
print(re.findall(pattern, my_string))

pattern = r'[a-z]'
print(re.findall(pattern, my_string))

pattern = r'[0-9]'
print(re.findall(pattern, my_string))
print(re.match(pattern, my_string))
search = re.search(pattern, my_string)
start, end = search.span()
print(f'Se encontró el {my_string[start:end]} entre los caracteres {start} y {end} de la cadena de texto.')

pattern = r'\d' # solo caracteres numéricos
print(re.findall(pattern, my_string))

pattern = r'\D' # todos los caracteres menos los numéricos
print(re.findall(pattern, my_string))

pattern = r"[l]"
print(re.findall(pattern, my_string))

pattern = r"[l].*" 
print(re.findall(pattern, my_string))


# Ejemplo de un patrón de validación de email
email = "juank537@gmail.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = "juank537@gmail."
print(re.findall(pattern, email))
email = "juank537@gmail.com.mx"
print(re.findall(pattern, email))