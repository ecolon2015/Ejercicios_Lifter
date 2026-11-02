
#Eduardo Colon
#Cree un programa que le pida al usuario ingresar 5 palabras. 
#Luego muestre una nueva lista con solo aquellas palabras que tengan más de 4 letras
#Ejemplo:
#Entrada ['sol', 'estrella', 'luz', 'planeta', 'roca']
#Salida: ['estrella', 'planeta']

my_words_list = []
my_new_words_list = []

for index in range(5): 
   word = str(input ("Enter 5 words  one by one "))
   my_words_list.append(word)
   
for word in my_words_list:
      if len(word) > 4:
        my_new_words_list.append(word)
   
print(f"these are the words that have more than 4 letters {my_new_words_list}")

