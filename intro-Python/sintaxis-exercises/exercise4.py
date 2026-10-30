
#Eduardo Colon
#Cree un programa que le pida tres números al usuario y muestre el mayor

first_number = int(input('Enter 1st positive number: '))
second_number = int(input('Enter 2nd positive number: '))
third_number = int(input('Enter 3rd positive number: '))


if first_number>=second_number and first_number>=third_number:
    print("the largest number is",first_number)
elif second_number>=first_number and second_number>=third_number:
    print("the largest number is",second_number)
elif third_number>=first_number and third_number>=second_number:
    print("the largest number is",third_number)
