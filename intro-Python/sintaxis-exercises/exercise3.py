
#Eduardo Colon
#Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero.
#Debe investigar cómo generar un número aleatorio distinto cada vez que se ejecute.

import random

secret_number = random.randint(1,10)
attempts= 0

while attempts != secret_number:
    attempts= int(input("Adivine el numero del 1 al 10 "))
    if attempts == secret_number:
        message = "tu adivinaste the secret number"
    else:
        print("please try again") 
print(message)