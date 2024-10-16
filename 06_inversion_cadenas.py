# INVERSION DE CADENAS DE TEXTO

def reverse_string(text):
    reverse_string = ""
    for char in text:
        reverse_string = char+reverse_string
    return reverse_string

print(reverse_string("Feliz y bendecida noche"))
