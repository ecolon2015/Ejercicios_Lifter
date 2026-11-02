
#Eduardo Colon
#Cree una función que acepte una lista de números y retorne 
# una lista con los números primos de la misma.
#[1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
#Tip 1: Investigue la lógica matemática para averiguar si un número es primo, y conviértala a código. No busque el código, eso no ayudaría.
#Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo, y agregarlo a otra lista). Así que lo mejor es agregar otra función 
# para revisar si el numero es primo o no.


possible_prime_numbers_list = [1,4,6, 7, 13,9,49,67]

def print_prime_numbers (possible_prime_numbers_list):
   prime_number_list = []
   for prime_number in possible_prime_numbers_list:
        if check_prime_numbers(prime_number):
             prime_number_list.append(prime_number)
   return prime_number_list
  

def check_prime_numbers(candidate):
   if candidate < 2:
       return False
   for possible_prime_number in range(2,candidate):
            if candidate % possible_prime_number == 0:
                return False
   return True
   
    
    

result=print_prime_numbers(possible_prime_numbers_list)
print(result)