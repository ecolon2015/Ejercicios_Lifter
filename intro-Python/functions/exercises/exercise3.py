
#Eduardo Colon
#Cree una función que retorne la suma de todos los números de una lista.
#La función va a tener un parámetro (la lista) y retornar un número (la suma de todos sus elementos).
#[4, 6, 2, 29] → 41

my_list_numbers = [4,6,2,29]

def sum_all_numbers_in_List(my_list_numbers):
   total_sum = 0
   for number in my_list_numbers:
        total_sum = total_sum + number
   return total_sum
        
total_result = sum_all_numbers_in_List(my_list_numbers)
print("the total for all the elements is: ", total_result)