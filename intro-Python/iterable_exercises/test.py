
my_favorite_records = [
    'dark side',
    'fear of blank',
    'signify',
]

#for index in  range(0,len(my_favorite_records)):
    #record = my_favorite_records[index]
    #print(f'Record {index}: {record}')
#for index, record in  enumerate(my_favorite_records):
 #   record = my_favorite_records[2],"hola","culo"
  #  print(f'Record {index}: {record}')

#my_string = "hola mundo"
#for character in my_string:
#    print(character)

#for index in  range(0,len(my_favorite_records)):
    #record = my_favorite_records[index]
   # my_favorite_records[index]= "hello"
    #print(f'Record {index}: {record}')
   # print(my_favorite_records)
  # words = ["apple", "banana", "cherry"]

# Loop through the list using the index and range
#for i in range(len(words)):
    # Modify the word at index 'i' (for example, making it uppercase)
   # words[i] = words[i].upper()

#print(words)
# Output: ['APPLE', 'BANANA', 'CHERRY']
words = ["apple", "banana", "cherry"]

# Loop through the list using the index and range
for index in range(len(words)):
    # Modify the word at index 'i' (for example, making it uppercase)
    if words[index] == "banana":  #i % 2 == 0:
        words[index] = "fuck"
print(words)


# Listas de ejemplo
first_list = ['Hay', 'en', 'que', 'iteracion', 'indices', 'muy']
second_list = ['casos', 'los', 'la', 'por', 'es', 'util']

# Iteración en paralelo
for palabra1, palabra2 in zip(first_list, second_list):
    print(palabra1, palabra2)

# Output: ['APPLE', 'BANANA', 'CHERRY']


#Below good for testing when to print or evaluate the content of the list 
# and evaluation of the index..

words=[1,2,3,4,5,6,7,8,9]
for index in range(len(words)):
     if words[index] % 2 == 0:
     #if index % 2 == 0:
        print(words[index])
#print(words)