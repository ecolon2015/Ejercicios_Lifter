#Eduardo Colon
#Cree un programa que le pida un numero al usuario, 
#y realice una suma de cada numero del 1 hasta ese número ingresado.
#Luego muestre el resultado de la suma.
#5 → 15 (1 + 2 + 3 + 4 + 5)
#3 → 6 (1 + 2 + 3)
#12 → 78 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12)

counter = 1
total_sum = 0
comulative_number = int(input ("Enter a positive number "))

while counter <= comulative_number:
    total_sum = total_sum + counter
    counter = counter + 1
    
print("the result of the sum ", total_sum )
