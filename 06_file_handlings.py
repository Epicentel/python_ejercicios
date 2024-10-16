

### File Handlings

import os

#.txt file
txt_file = open("./my_file.txt", "w+") #Leer y escribir
txt_file.write("Mi nombre es Epi\nMi apellido es Centeno\nMi edad es 54\nMi color favorito es azul\nMi lenguaje preferido es Python")
#print(txt_file.read())
print(txt_file.read(10))
print(txt_file.readline())
print(txt_file.readline())
print(txt_file.readlines())
for line in txt_file.readlines():
    print(line)



txt_file.write("\nAunque también me gusta Java")
print(txt_file.readline())

txt_file.close()
with open("./my_file.txt", "a") as my_other_file:
    my_other_file.write("\ Y Swift")
#os.remove("./my_file.txt")

#.json file
import json
json_file = open("./my_file.json", "w+")
json_test = {
    "name": "Epifanio",
    "surname": "Centeno",
    "age": 54, 
    "languages":["Python","Swift","Kotlin"],
    "website": "https://centeno.grow"
    }

json.dump(json_test,json_file,indent = 2)
json_file.close()

with open("./my_file.json") as my_other_file:
  for line in my_other_file.readlines():
    print(line)

json_dict = json.load(open("./my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])

#.csv file
json_test = {
    "name": "Epifanio",
    "surname": "Centeno",
    "age": 54, 
    "languages":["Python","Swift","Kotlin"],
    "website": "https://centeno.grow"
    }
import csv

csv_file = open("./my_file.csv", "w+")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name","surname","age","language","website"])
csv_writer.writerow(["Epi","Centeno",54,"Python","https://centeno.grow"])
csv_writer.writerow(["Laura","Tellez",44,"Cobbol","https://laura.faith"])

csv_file.close()

with open("./my_file.csv") as my_other_file:
   for line in my_other_file.readlines():
    print(line)


