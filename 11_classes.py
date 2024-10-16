### Classes ###

class MyEmptyPerson:
    pass
print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
   def __init__(self,name,surname,alias = "Sin alias"):
       self.full_name = f"{name} {surname} ({alias})" # Propiedad pública
       self.__name = name # Propiedad privada
    
   def get__name(self):
       return self.__name
   def walk(self):
       print(f"{self.full_name} está caminando")
       
my_person = Person("Juanita","Tellez")
print(my_person.full_name)
print(my_person.get__name())
my_person.walk()

my_other_person = Person("Juanita", "Téllez", "mamita")
print(my_other_person.full_name)
my_other_person.walk()

my_other_person.full_name = "Carmelo Centeno (el trombomista feliz)"
print(my_other_person.full_name)
my_other_person.walk()

my_other_person.full_name = 777
print(my_other_person.full_name)
my_other_person.walk()