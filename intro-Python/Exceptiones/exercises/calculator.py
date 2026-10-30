#Eduardo Colon
#Cree una calculadora por linea de comando. Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número:
#1. Suma
#2. Resta
#3. Multiplicación
#4. División
#5. Borrar resultado
#Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar, o dividir por el actual. El resultado debe pasar a ser el nuevo numero actual.
#Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, o si ingresa un número invalido a la hora de hacer la operación.


def calculate_by_command_line():
    actual_number= 0
    
    while True:
        print("---Calculator---")
        print("Actual Number: ", actual_number)
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Reset")
        print("6. Exit")
        
        option=input("Choose an option: ")
        
        if option == "5":
            actual_number = 0
            print("Result erased.. the actual number now is 0: ")
            continue
        
        if option == "6":
            print("Exiting Calculator")
            break
        
        if option not in ("1","2","3","4"):
            print("option is not valid")
            continue
        
        try:
            new_number = int(input("Enter another number to calculate: "))
        except ValueError:
            print("you must enter a valid number")
            continue
        
        if option == "1":
            actual_number =actual_number + new_number
            
        elif option == "2":
            actual_number = actual_number - new_number
            
        elif option == "3":
            actual_number= actual_number * new_number
        
        elif option == "4":
            if new_number == 0:
               print("Error, you can't divide by zero")
               continue
            actual_number = actual_number / new_number
           
        print("Result: ",actual_number)
            
calculate_by_command_line()   
        

