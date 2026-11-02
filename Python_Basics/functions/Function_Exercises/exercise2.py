
#Eduardo Colon
# 1. Experimente con el concepto de scope:
# A. Intente acceder a una variable definida dentro de una función desde afuera.
# B. Intente acceder a una variable global desde una función y cambiar su valor.

#Global Variable
number3 = 25

def multiply_two_numbers ():
    number1= 25
    number2= 5
    global number3 #referencing the global variable number3
    number3 = 20
    number1 = number1 + number3
    result =  number1 * number2
    print("The product of these two numbers is: ",result)

multiply_two_numbers()
#trying to use a local variable, I get that error
#print(result)
print(number3)


