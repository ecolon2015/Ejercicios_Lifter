#Eduardo Colon
#Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero.
#Debe investigar cómo generar un número aleatorio distinto cada vez que se ejecute.

import random

secret_number = random.randint(1,10)
user_guess= 0

while user_guess != secret_number:
    user_guess= int(input("Adivine el numero del 1 al 10 "))
    if user_guess == secret_number:
        message = "tu adivinaste el numero secreto"
    else:
        print("Por favor trate otra vez") 
print(message)