### Programa para Calcular la Media ###


juan_centeno = [23,24,25,17,18,21,26,20,19,24,23,24]
manel_centeno = [24,24,21,29,20,22,28,23,25,19,19,25]

def mean(numbers):
    return sum(numbers)/len(numbers)

juan_mean = mean(juan_centeno)
manel_mean = mean(manel_centeno)

print(f"Media Juan {juan_mean:.1f}")
print(f"Media Manel {manel_mean:.1f}")