#Eduardo Colon
#Cree una función que le dé la vuelta a un string y lo retorne.
#A.Esto ya lo hicimos en iterables.
#B. “Hola mundo” → “odnum aloH”



my_string = "Hola Mundo"

def reverse_string (my_string):
    my_reverse_string = ""
    for index in  range(len(my_string)-1,-1,-1):
        #print(my_string[index])
        my_reverse_string = my_reverse_string + my_string[index]
    return my_reverse_string

my_reverse_string = reverse_string(my_string)
print(my_reverse_string)