### High Order Functions ###

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_add_value(first_value,second_value,f_sum):
    return f_sum(first_value + second_value)

print(sum_two_values_and_add_value(10,5,sum_one))
print(sum_two_values_and_add_value(10,5,sum_five))

### CLOSURES ###

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add

add_closure = sum_ten(1)
print(add_closure(7))

print(sum_ten(7)(1))

### Built-in-Higher Order Functions

from functools import reduce

numbers = [2,4,10,21,3,30]

# map 

def multilpy_two(number):
    return number * 2

print(list(map(multilpy_two,numbers)))
print(list(map(lambda number: number *2,numbers)))

# filters
def filter_greater_than_ten(number):
    if number >10:
        return True
    return False

print(list(filter(filter_greater_than_ten,numbers)))
print(list(filter(lambda number:number >10,numbers)))

# reduce

def sum_two_values(first_value, second_value):
    print(first_value)
    print(second_value)
    return first_value + second_value

print(reduce(sum_two_values,numbers))