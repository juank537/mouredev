
# ESTO funciona

"""
file = open("archivo.txt", "r")
lines = file.readlines()
listado = []
for line in lines:
	codigo_filme = line[0].capitalize() + str(len(line))
	listado.append(codigo_filme)
file.close()
print(listado)
"""

file = open("archivo.txt", "r+")
lines = file.readlines()
listado = []
for line in lines:
	codigo_filme = line[0].capitalize() + str(len(line)) + ' - ' + line
	print(codigo_filme)
	file.write(codigo_filme)
file.close()