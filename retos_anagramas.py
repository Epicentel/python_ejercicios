'''
ANAGRAMAS:
Determinar si dos 
cadenas de texto
 son anagramas

'''


def are_anagrams(string1, string2):
    return sorted(string1.lower()) == sorted(string2.lower())

print(are_anagrams("roma","amor"))
print(are_anagrams("amiga", "magia"))
print(are_anagramas("perro","cerro"))


      
