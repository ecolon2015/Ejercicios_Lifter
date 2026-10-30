#Eduardo Colon
#Convertidor de unidades de temperatura
#Pida al usuario ingresar una temperatura en Celsius
#Conviértala a Fahrenheit y Kelvin
#Muestre los tres valores
#Ejemplo:
#Entrada
#"Ingrese temperatura en Celsius: " 25
#Salida:
#Fahrenheit:77.0
#Kelvin:298.15

celcius = int (input ("Enter a temperature in Celcius " ))

if celcius>1:
    fahrenheit=celcius * 1.8 + 32
    kelvin = celcius + 273.15
print("Fahrenheit", fahrenheit)
print("Kelvin", kelvin)
