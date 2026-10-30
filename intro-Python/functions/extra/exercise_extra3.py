
#Eduardo Colon
#Cree una función que reciba un string y retorne cuántas vocales contiene
#Ejemplo:
#Entrada:
#"Hola mundo"
#Salida:
#4

my_string = "Hola mundo"

def count_vowels(my_string):
    number_of_vowel = 0
    for vowel in my_string:
        if vowel in "aeiouAEIOU":
            number_of_vowel=number_of_vowel + 1
    return number_of_vowel

vowel_result= count_vowels(my_string)
print("it has",vowel_result,"vowels")