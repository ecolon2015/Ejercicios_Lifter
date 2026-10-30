
#Eduardo Colon
 #Cree una función que reciba una lista de palabras y 
 # un número n, y retorne una nueva lista con solo las palabras que tengan más de n letras
#Ejemplo:
#Entrada:
#["cielo", "sol", "maravilloso", "día"]
#"Ingrese el numero de letras minimas en la palabra: " 4
#Salida:
#["cielo", "maravilloso"]

word_list = ["cielo", "sol", "maravilloso", "día"]
minimal_word_number = int(input("Enter the minimum number of letters in the word: "))

def search_minimal_word(word_List,minimal_word_number):
    new_word_list = []
    for minimal_word in word_List:
        if len(minimal_word) > minimal_word_number:
            new_word_list.append(minimal_word)
           
    return new_word_list

new_result_list = search_minimal_word(word_list,minimal_word_number)
print(new_result_list)