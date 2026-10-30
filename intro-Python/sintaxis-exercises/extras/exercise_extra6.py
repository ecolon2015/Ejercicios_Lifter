#Eduardo Colon
#Tabla de multiplicar personalizada
#Pida al usuario un número del 1 al 10
#Muestre su tabla de multiplicar del 1 al 12
#Ejemplo:
#Entrada:
#"Ingrese un número:"7
#Salida:
#7 x 1 = 7
#7 x 2 = 14
#...
#7 x 12 = 84
counter =1 
option_number = int(input("Enter a number from 1 to 10: "))

match option_number:
    case 1:
        while counter <= 12:
            multiplication_table_by_one = option_number * counter
            print(option_number , "x", counter, multiplication_table_by_one)
            counter = counter + 1
    case 2:
        while counter <= 12:
            multiplication_table_by_two = option_number * counter
            print(option_number , "x", counter, multiplication_table_by_two)
            counter = counter + 1
    case 3:
        while counter <= 12:
            multiplication_table_by_three = option_number * counter
            print(option_number , "x", counter, multiplication_table_by_three)
            counter = counter + 1

    case 4:
        while counter <= 12:
            multiplication_table_by_four = option_number * counter
            print(option_number , "x", counter, multiplication_table_by_four)
            counter = counter + 1
    case 5:
        while counter <= 12:
            multiplication_table_by_five = option_number * counter
            print(option_number , "x", counter, multiplication_table_by_five)
            counter = counter + 1
    case 6:
        while counter <= 12:
            multiplication_table_by_six = option_number * counter
            print(option_number , "x", counter, multiplication_table_by_six)
            counter = counter + 1
    case 7:
        while counter <= 12:
            multiplication_table_by_seven = option_number * counter
            print(option_number , "x", counter, multiplication_table_by_seven)
            counter = counter + 1
    case 8:
        while counter <= 12:
            multiplication_table_by_eight = option_number * counter
            print(option_number , "x", counter, multiplication_table_by_eight)
            counter = counter + 1
    case 9:
        while counter <= 12:
            multiplication_table_by_nine = option_number * counter
            print(option_number , "x", counter, multiplication_table_by_nine)
            counter = counter + 1
    case 10:
        while counter <= 12:
            multiplication_table_by_ten = option_number * counter
            print(option_number , "x", counter, multiplication_table_by_ten)
            counter = counter + 1
    case _:
        print("this option is not valid")
            
