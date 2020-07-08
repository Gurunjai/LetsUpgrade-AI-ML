## Program to convert the provided farenheit to a Kelvin and Celsius
## Day-3 Question 5 from LetsUpgrade AI ML 

faren = 100

"""
    The value of farenheit can be converted to a Kelvin with the help of the following convention

    (32°F − 32) × 5/9 + 273.15 = 273.15K
"""
kelvin = (faren - 32) * 5/9 + 273.15
print("Provided Farenheit = ", faren, ", converted Kelvin: ", kelvin)

"""
    The value of farenheit can be converted to a celsius with the help of the following convention

    (32°F − 32) × 5/9 = 0°C
"""
celsius = (faren - 32) * 5/9 
print("Provided Farenheit = ", faren, ", converted Celsius: ", celsius)
