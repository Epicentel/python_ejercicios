'''
TABLAS DE MULTIPLICAR
Crear las tablas de multiplicar 
del 1 a al 10
'''

for table_number in range(1,11):
    print(f"Tabla del {table_number}")
    for number in range(1,11):
        print(f"{number}x{table_number} = {number*table_number}")
    print()