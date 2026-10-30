#Eduardo Colon
#Cree un programa que pida 3 números al usuario. 
#Si uno de esos números es 30, o si los 3 sumados dan 30, 
#mostrar “Correcto”. Sino, mostrar “incorrecto”.
#Ejemplos:
#23, 30, 768 → Correcto (hay un 30)
#10, 15, 5 → Correcto (10 + 15 + 5 = 30)
#35, 56, 2 → Incorrecto (no hay ningún 30, y la suma de ellos tampoco da 30)

number1 = int(input("Enter first number "))
number2 = int(input("Enter second number "))
number3 = int(input("Enter third number "))

if number1 == 30 or number2 == 30 or number3 ==30:
    print("correct")
elif number1 + number2 + number3 ==30:
    print("correct")
else: 
    print ("incorrect")
