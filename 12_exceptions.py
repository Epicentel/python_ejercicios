### Exceptions Handling (manejo de errores)###

numberOne = 10
numberTwo = 7
numberTwo = "7"
 # try except

try:
  print(numberOne + numberTwo)
  print("No se ha producido un error")
except: # Se produce si ocurre una excepción
  print("Se ha producido un error")

# try except else finally

try:
  print(numberOne + numberTwo)
  print("No se ha producido un error")
except:
  print("Se ha producido un error")
else: # Opcional
   # Se ejecuta si no se produce una excepción
  print("La ejecución continúa correctamente")
finally: #Opcional
  # Se ejecuta siempre
  print("La ejecución continúa")

# Exceptions por tipo

try:
  print(numberOne + numberTwo)
  print("No se ha producido un error")
except ValueError:
  # Se ejecuta si se ha producido una excepción
  print("Se ha producido un ValueError")
except TypeError:
  # Se ejecuta si se ha producido una excepción
  print("Se ha producido un TypeError")
 
 # Captura de la información de la excepción

try:
  print(numberOne + numberTwo)
  print("No se ha producido un error")
except ValueError as error:
  print(error)
except Exception as exception:
  print(exception)






