### tuples ###
my_tuple = tuple()
my_other_tuple = ()

my_tuple = (54,1.65,"Epifanio", "Centeno","Centeno")
my_other_tuple = (54, 54, 26, 17, 25)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

# print(my_tuple[4]) IndexError: tuple index out of range
# print(my_tuple[-5]) IndexError: tuple index out of range

print(my_tuple.count("Centeno"))
print(my_tuple.count(54))
print(my_tuple.count("Tellez"))

print(my_tuple.index("Centeno"))
print(my_tuple.index(1.65))


# my_tuple[1]=1.70 'tuple' object does not suppsort item assigment
print(my_tuple)

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)
print(my_sum_tuple[2:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[2] = "Pipis"
my_tuple.insert(5,"Tellez")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))


# del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion

del my_tuple
# print(my_tuple) NameError: name 'my_tuple' is not defined