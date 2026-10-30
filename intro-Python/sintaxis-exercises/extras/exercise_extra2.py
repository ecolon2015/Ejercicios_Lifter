#Eduardo Colon
#Cree un pseudocódigo que le pida un tiempo en segundos 
#al usuario y calcule si es menor o mayor a 10 minutos. Si es menor, 
#muestre cuantos segundos faltarían para llegar a 10 minutos. 
#Si es mayor, muestre “Mayor”. Si es exactamente igual, muestre “Igual”.
#Ejemplos:
#1040 → Mayor
#140 → 460
#600 → Igual
#599 → 1

seconds= int(input("Enter a time in seconds "))

if seconds < 600:
    seconds_left = 600 - seconds
    print("you are ",seconds_left,"seconds to get to 10 minutes")
elif seconds >600:
    print("greater")
else:
    print("Equal")