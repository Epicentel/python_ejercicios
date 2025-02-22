### Regular Expressions ###

import re

# match
my_string = "Esta es la lección número 7:  Lección llamada Expresiones Regulares"
my_other_string = "Esta no es la lección número 6:Manejo de Ficheros"

match = re.match("Esta es la lección", my_string,re.I)
print(match)
start,end = match.span()
print(my_string[start:end])

match = re.match("Esta no es la lección",my_other_string)
#if not(match== None):# Otra forma de comprobar el None
#if match ==| None: # Otra forma de comprobar el None
if match is not None:
    print(match)
    start,end = match.span()
    print(my_other_string[start:end])

    
      
print(re.match("Esta es la lección", my_other_string))
print(re.match("Expresiones Reguares", my_string))

# search

search = re.search("lección", my_string,re.I)
print(search)
start,end = search.span()
print(my_string[start:end])

# findall

findall = re.findall("lección",my_string,re.I)
print(findall)

# split

print(re.split(":",my_string))

# sub

print(re.sub("[l|L]ección", "LECCION", my_string))
print(re.sub("Expresiones Regulares","Regex",my_string, ))

# Patterns
# Para aprender y validar expresiones regulares:https://regex101.com

pattern = r"[lL]ección|Expresiones"
print(re.findall(pattern,my_string))

pattern = r"[a-z]"
print(re.findall(pattern,my_string))

pattern = r"[0-9]"
print(re.findall(pattern,my_string))
print(re.search(pattern,my_string))

pattern = r"\D"
print(re.findall(pattern,my_string))

pattern = r"[l].*"
print(re.findall(pattern,my_string))

email = "mouredev@mouredev.com"
pattern = r"^[a-zA-z0-9_.+-]+@[a-zA-z0-9]+\.[a-zA-z0-9-.]+$"
print(re.match(pattern,email))
print(re.search(pattern,email))
print(re.findall(pattern,email))

email = "mouredev@mouredev.com.mx.112"
print(re.findall(pattern,email))




