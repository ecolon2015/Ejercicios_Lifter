#Eduardo Colon

#Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.
#Ejemplos:
#86, 54, 23, 54, 67, 21, 2, 65, 10, 32 → [86, 54, 23, 54, 67, 21, 2, 65, 10, 32]. El más alto fue 86.



#words=[4,5,6]
#for index in range(len(words)):
    # Modify the word at index 'i' (for example, making it uppercase)
    #if words[index] == "banana":  #i % 2 == 0:
        #words[index] = "fuck"
#print(words)
index = 1
#words=[1,2,3,4,5,6,7,8,9]
#for index in range(len(words)):
    # Modify the word at index 'i' (for example, making it uppercase)
    #if index % 2 == 0:
        #print("hello")
     #if words[index] % 2 == 0:
       # print(words[index])
#print(words)
""" words=[]
my_list= []
for index in range(0,11):
    words[index]=int(input("Enter a number "))
    # Modify the word at index 'i' (for example, making it uppercase)
    #if index % 2 == 0:
    my_list[index]= words[index]
    
        #print("hello")
     #if words[index] % 2 == 0:
    print(my_list) """
numbers=[]
#largest= numbers[0]

for index in range (10): 
    number = int(input ("Enter 10 positive numbers one by one "))
    #index = index + 1
    #largest= numbers[0]
    numbers.append(number)
    #print(words)
    largest= numbers[0]
    #greater = max(numbers)
    for num in (numbers):  #[1:]:
        if num > largest:
            largest = num
    #if words[index] >= words[index]
print(largest)
#print(greater) 
    # Inicializamos una lista vacía para guardar los números
""" numeros = []

# Pedimos al usuario que ingrese 10 números
for i in range(10):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)

# Encontramos el número más alto de la lista
mas_alto = max(numeros)

# Mostramos los resultados solicitados
print(f"\nNúmeros ingresados: {numeros}")
print(f"El más alto fue {mas_alto}.")
 """

# Example list
#numbers = [10, 6, 8, 2, 4, 15, 3]

# Initialize with the first element
""" largest = numbers[0]

# Loop through the rest of the list
for num in (numbers):  #[1:]:
    if num > largest:
        largest = num

print("Greatest value:", largest)
 """