

### Error Types ###

# SyntaxError

# print "¡Hola comunidad!"  # Descomntar para Error
print ("¡Hola comunidad!")

# NameError

language = "Spanish" # Comentar para Error
print(language)

# IndexError 

my_list = [ "Python", "Swift","Kotlin","Dart", "JavaScript","PHP"]
print(my_list[0])
print(my_list[4])
print(my_list[-1])
#print(my_list[5]) #Descomentar para Error"

#ModuleNotFoundError

#import maths #Descomentar para Error
import math

#AttributeError
#print(math.PI)#Descomentar para Error
print(math.pi)

#KeyError
my_dict = {"Nombre": "Epifanio", "Apellido": "Centeno","Edad": 54, 1:"Python"}
print(my_dict["Edad"])
#print(my_dict["Apelido"]) #Descomentar para Error
print(my_dict["Apellido"])

#TypeError
#print(my_list["0"]) #Descomentar para Error
print(my_list[0])

#ImportError
#from math import PII #Descomentar para Error
from math import pi
print(pi)

#ValueError
#my_int = int("10 años") #Descomentar para Error
my_int = int("10")
print(my_int)
print(type(my_int))

#ZeroDivisionError
#print(10/0) #Descomentar para Error
print(10/2)