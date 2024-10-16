### Dictionaries ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Epifanio", "Apellido": "Centeno","Edad": 54, 1:"Python"}
my_dict = {
    "Nombre": "Epifanio",
    "Apellido": "Centeno",
    "Edad": 54,
    "Languages":{"Python", "Java","Kotlin"},
    1: "Azul"
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])

my_dict["Nombre"]="Juanito"
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Calle"]="Lago"
print(my_dict)

del my_dict["Calle"]
print(my_dict)

print("Centeno" in my_dict)
print("Apellido" in my_dict)
print(my_dict["Apellido"])

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
#print(my_dict.fromkeys())

my_list = ["Nombre", 1,"Piso"]
my_new_dict=dict.fromkeys(my_list)
print(my_new_dict)
my_new_dict=dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)
my_new_dict=dict.fromkeys(my_dict)
print(my_new_dict)
my_new_dict=dict.fromkeys(my_dict,("Manel"))
print(my_new_dict)

my_values=my_new_dict.values()
print(type(my_values))
print(my_new_dict.values())

print(list(dict.fromkeys(list(my_new_dict.keys()))))
print(tuple(my_new_dict))
print(set(my_new_dict))