
### Python Package Manager

# PIP https://pypi.org

#install pip
#pip install version

#pip install numpysour
#import numpy 
#print(numpy.version.version)
#numpy_array = numpy.array([60,24,18,35,54,17,40])
#print(type(numpy_array))

#print(numpy_array*2)

#pip install pandas
#import pandas 
#pip list
#pip uninstall pandas
#pip show numpy


#pip install requests
import requests


response=requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)

print("Epi")