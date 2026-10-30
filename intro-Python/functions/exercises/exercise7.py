
#Eduardo Colon
#Cree una función que acepte una lista de números y retorne 
# una lista con los números primos de la misma.
#[1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
#Tip 1: Investigue la lógica matemática para averiguar si un número es primo, y conviértala a código. No busque el código, eso no ayudaría.
#Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo, y agregarlo a otra lista). Así que lo mejor es agregar otra función 
# para revisar si el numero es primo o no.


possible_prime_numbers_list = [1,4,6, 7, 13,9, 67]

def print_prime_numbers (possible_prime_numbers_list):
   prime_number_list = []
   for prime_number in possible_prime_numbers_list:
        if check_prime_numbers(prime_number):
             prime_number_list.append(prime_number)
   return prime_number_list
   """  prime_result=check_prime_numbers(possible_prime_numbers_list)

    return(prime_result) """

def check_prime_numbers(possible_prime_numbers_list):
   if possible_prime_numbers_list < 2:
       return False
   for possible_prime_number in range(2,possible_prime_numbers_list):
            if possible_prime_numbers_list % possible_prime_number == 0:
                return False
   return True
   """  no_prime_number= []
    prime_number=[]
    for possible_prime_number in possible_prime_numbers_list:
        if possible_prime_number <= 1:
           no_prime_number.append(possible_prime_number)

        elif possible_prime_number == 2 or possible_prime_number ==3 or possible_prime_number==5:
            prime_number.append(possible_prime_number)

        elif possible_prime_number > 2  and possible_prime_number % 2 == 0:
            no_prime_number.append(possible_prime_number)

        elif possible_prime_number > 2  and possible_prime_number % 3 == 0:
            no_prime_number.append(possible_prime_number)

        elif possible_prime_number > 5  and possible_prime_number % 5 == 0:
            no_prime_number.append(possible_prime_number)

        else:
            prime_number.append(possible_prime_number)  """


   # return prime_number    
    
#result= check_prime_numbers(possible_prime_numbers_list)
result=print_prime_numbers(possible_prime_numbers_list)
print(result)