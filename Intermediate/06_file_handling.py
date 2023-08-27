### File Handling ###
"""
import os

# .txt file

txt_file = open("Intermediate/my_file.txt", "w+", encoding="utf-8") # Leer y escribir
txt_file.write("Me llamo Juan Carlos\nMi apellido es Aliaga\n33 años\nY mi lenguaje favorito es Python")

# print(txt_file.read())
print(txt_file.read(10))
print(txt_file.readline())
print(txt_file.readline())
for line in txt_file.readlines():
    print(line)
    
txt_file.write("\nAunque también me gusta JavaScript")
print(txt_file.readline())

txt_file.close()

with open("Intermediate/my_file.txt", "a") as my_other_file:
    my_other_file.write("\nY Java")

# os.remove("Intermediate/my_file.txt")
"""

# .json file
"""

import json

json_file = open("Intermediate/my_file.json", "w+")

json_test = {
    "name":"Juan Carlos", 
    "surname":"Aliaga", 
    "age":33, 
    "language":["Python", "PHP", "Java", "JavaScript"],
    "website":"https://moure.dev"}

json.dump(json_test, json_file, indent= 2)

json_file.close()

# with open("Intermediate/my_file.json") as my_other_file:
#     for line in my_other_file.readlines():
#         print(line)
        
json_dict = json.load(open("Intermediate/my_file.json"))

print(json_dict)
print(type(json_dict))
print(json_dict["name"])

"""

# .csv file

import csv

csv_file = open("Intermediate/my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language", "website"])
csv_writer.writerow(["Brais", "Moure", 35, "Python", "https://moure.dev"])
csv_writer.writerow(["Juan Carlos", "Aliaga", 33, "Python", "https://fb.com/juank537"])

csv_file.close()

 with open("Intermediate/my_file.csv") as my_other_file:
    for line in my_other_file:
        print(line)

# .xlsx file

# import xlrd # Debe instalarse el módulo


# .xml file

import xml
