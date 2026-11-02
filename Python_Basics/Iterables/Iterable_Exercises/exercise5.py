
#Eduardo Colon

#Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.
#Ejemplos:
#86, 54, 23, 54, 67, 21, 2, 65, 10, 32 → [86, 54, 23, 54, 67, 21, 2, 65, 10, 32]. El más alto fue 86.





numbers=[]

for index in range(10): 
    number = int(input ("Enter 10 positive numbers one by one "))
    numbers.append(number)
    largest= numbers[0]

for num in (numbers):  
    if num > largest:
        largest = num
print(f"You entered the following values {numbers}")
print(f"The Largest value was {largest}")

