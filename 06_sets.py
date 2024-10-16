### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {"Epifanio", "Centeno", 54, 1.65}
print(my_set)
print(type(my_set))

print(len(my_other_set))

my_other_set.add("Pipis") # Un set no es una estructurada ordenada

print(my_other_set)

my_other_set.add("Pipis") # Un set no admite repetidos

print(my_other_set)

print("Pipis" in my_other_set)
print("Pifis" in my_other_set)

my_other_set.remove("Pipis")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
#print(my_other_set) NameError: name 'my_other_set' is not defined

my_set = ("Epifanio", "Centeno", 54, 1.65)
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_set={"Epifanio", "Centeno", 54, 1.65}
my_other_set={"Kotlin","Java","Swift", "Python"}
my_new_set = my_set.union(my_other_set)
print(my_new_set)
print(my_new_set.union(my_new_set).union({"C#",}))

print(my_new_set.difference(my_set))