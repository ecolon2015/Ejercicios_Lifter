
#Eduardo Colon
# Cree una función que reciba un texto y un carácter, y retorne cuántas veces aparece ese carácter en el texto
#Ejemplo:
#Entrada:
#"programacion"
#"Ingrese el carácter que desea buscar:" "o"
#Salida:
#"Se ha encontrado 2 veces el carácter"

word= ("programacion ")
character_to_search = input("Enter a character you want to search for: ")

def find_the_character (word,character_to_search):
    character_found= 0
    for character in word:
        if character == character_to_search:
            character_found= character_found + 1
   
    return character_found
total_of_character= find_the_character(word,character_to_search)
print("it has been found",total_of_character,"times the character")
