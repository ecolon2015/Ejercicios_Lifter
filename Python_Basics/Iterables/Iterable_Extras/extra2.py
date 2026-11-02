#Eduardo Colon
#Cree un programa que verifique si todos los elementos de una lista 
# son positivos
#Entrada: my_list = [3, 6, 0, -2, 4]
#Salida:"Hay al menos un número negativo o cero"

my_list_numbers = [3,6,0,-2,4]
all_positive_numbers=True

for number in my_list_numbers:
    if number <= 0:
        all_positive_numbers=False

if all_positive_numbers:
    print("all the numbers are positive")
else:
    print("there are at least a negative number or zero")
    
