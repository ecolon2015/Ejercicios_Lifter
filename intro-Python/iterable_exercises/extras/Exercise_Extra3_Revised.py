#Eduardo Colon
#Cree un programa que muestre el valor más pequeño de una lista sin usar min().
#Use una variable para comparar uno a uno
#Ejemplo:
#Entrada: my_list = [9, 4, 7, 1, 5]
#salidad: "El menor valor es 1"

my_list_numbers=[9,4,7,1,5]



lowest_number= my_list_numbers[0]

for num in (my_list_numbers): 
    if num < lowest_number:
        lowest_number = num
print(f"The Lowest value is {lowest_number}")


