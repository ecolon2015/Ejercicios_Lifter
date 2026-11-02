
#Eduardo Colon
#Cree una función que imprima el número de mayúsculas y
#  el número de minúsculas en un string.
#“I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”

my_string = "I love Nacion Sushi"

def calculate_uppercase_and_lowercase(my_string):
    uppercase_string= 0
    lowercase_string= 0
    for char in my_string:
        if char.isupper():
            uppercase_string= uppercase_string + 1
        elif char.islower():
           lowercase_string=  lowercase_string+ 1
    print("There's ", uppercase_string,"upper cases and", lowercase_string,"lower cases")
    
calculate_uppercase_and_lowercase(my_string)