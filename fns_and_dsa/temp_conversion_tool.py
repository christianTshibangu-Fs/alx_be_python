
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):

    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius


def convert_to_fahrenheit(celsius):

    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit



temperature = float(input("Entrez la température: ")) 
unit = input("Convertir en (F)ahrenheit ou (C)elsius? ").strip().upper()
if unit == 'F' :
    convert_to_celsius = convert_to_celsius(temperature)
    print(f"{temperature}°C est égal à {convert_to_celsius}°F")
elif unit == 'C' :
    convert_to_fahrenheit = convert_to_fahrenheit(temperature)
    print(f"{temperature}°F est égal à {convert_to_fahrenheit}°C")
else :
    print("Unité non reconnue. Veuillez entrer 'F' ou 'C'.")

