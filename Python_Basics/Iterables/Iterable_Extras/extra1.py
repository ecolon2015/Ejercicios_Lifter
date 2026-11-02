#Eduardo Colon
#Cree un programa que cuente cuántas veces aparece un número específico en una lista. 
# Pida al usuario una lista de números y otro número a buscar
#Ejemplo:
#my_list =[4,2,7,2,8,2,1]
#numero_a_buscar =2
#salida: "El número 2 aparece 3 veces"

my_list_numbers =[4,2,7,2,8,2,1]
number_to_search = int(input("Enter the number to search for: "))

count = 0
for  number in  my_list_numbers:
    if number == number_to_search:
        count= count + 1
print(f"the number {number_to_search} appears {count} times in the list")