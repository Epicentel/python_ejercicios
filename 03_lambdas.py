### Lambdas ###

sum_two_values = lambda first_value,second_value: first_value + second_value
print(sum_two_values(6,8))

multiply_values = lambda first_value,second_value: first_value * second_value - 5
print(multiply_values(6,8))

def sum_three_values(value):
    return lambda first_value,second_value: first_value + second_value + value
print(sum_three_values(4),(6,8))
