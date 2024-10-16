### Loops = Bucles = Ciclos ###

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2

else: # Es opcional
    print("Mi condición es mayor o igual a 10")

while my_condition < 20:
    my_condition += 1
    if my_condition ==15:
        print("Se detiene la ejecución")
        break
    
    print(my_condition)

print("La ejecución continúa")

# For

my_list = [54,53,17,17,25,26,87]
for element in my_list:
    print(element)

my_tuple = (54,1.65,"Epifanio", "Centeno","Centeno")
for element in my_tuple:
    print(element)

my_set= {"Kotlin","Java","Swift", "Python"}
for element in my_set:
    print(element)

my_dict = {"Nombre": "Epifanio", "Apellido": "Centeno","Edad": 54, 1:"Python"}
for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")
else:
    print("El bucle for para diccionario ha finalizado")

print("La ejecución continúa")