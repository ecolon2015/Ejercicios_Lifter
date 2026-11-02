
#Eduardo Colon

#Cree un programa que elimine todos los números impares de una lista.
#Ejemplos:
#my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] → [2, 4, 6, 8]
even_numbers = []
my_numbers_list=[1,2,3,4,5,6,7,8,9]
for index in range(len(my_numbers_list)):
     if my_numbers_list[index] % 2 == 0:
        even_numbers.append(my_numbers_list[index])
print(even_numbers)
