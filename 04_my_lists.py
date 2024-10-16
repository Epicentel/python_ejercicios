### Lists = Vectores = Matrices ###

my_list = ()
my_other_list =[]

print(len(my_list))

my_list = [54,53,17,17,25,26,87]
print(my_list)
print(len(my_list))

my_other_list = [ 54,1.70, "Epifanio", "Centeno", 2501]

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-5])
print(my_list.count(17))
# print(my_other_list(5))  ErrorIndex
# print(my_other_list(-6))  ErrorIndex

age, height,name,surname,birthday = my_other_list
print(surname)

print(my_list + my_other_list)

my_other_list.append("Tellez")
print(my_other_list)

my_other_list.insert(2,"Rojo")
print(my_other_list)

my_other_list[2] = "Azul"
print(my_other_list)



my_other_list.remove("Azul")
print(my_other_list)

my_list.remove(17)
print(my_list)

my_list.pop()
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[0]
print(my_list)

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

print(my_new_list[1:2])
print(my_new_list[1:3])

my_list = "Hola Python"
print(my_list)
print(type(my_list)) 