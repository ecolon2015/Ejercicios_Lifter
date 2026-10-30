#Eduardo Colon
#Cree un programa que reciba una lista de números y calcule el promedio de los valores, 
#luego cree una nueva lista con solo los valores mayores al promedio
#Ejemplo: 
#Entrada: my_list = [10, 20, 30, 40, 50]
#Salida: "Promedio:" 30
#Nueva lista: [40, 50]

my_grade_list = [10,20,30,40,50]
total_grade=0
my_new_list = []

for grade in my_grade_list:
    total_grade = total_grade + grade
    
total_average = total_grade / len(my_grade_list)
for number in my_grade_list:
    if number > total_average:
        my_new_list.append(number)

print(f"The total average is: {total_average}")
print(f"The new list is: {my_new_list}")