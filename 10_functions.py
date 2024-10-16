### Functions ###

def my_function():
    print("Esto es una función")

my_function()
my_function()
my_function()

def sum_two_values(first_value, second_value):
    print(first_value + second_value)
sum_two_values(10,5)
sum_two_values(452689, 12433745)
sum_two_values("10", "7")
sum_two_values(9.81, 2.54)

def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum

my_result = sum_two_values(1.5, 3.5)
print(my_result)

my_result = sum_two_values_with_return(10, 5)
print(my_result)

def print_name (name, surname):
    print(f"{name} {surname}")

print_name(surname = "Centeno", name ="Manel")

def print_name_with_default (name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Juan", "Centeno")
print_name_with_default("Juan","Centeno","Juanito")

def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())

print_upper_texts("Hola", "Python", "Pipis")
-

