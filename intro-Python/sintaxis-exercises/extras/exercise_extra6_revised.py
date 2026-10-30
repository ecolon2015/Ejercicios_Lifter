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
multiplication_number = int(input("Enter a number from 1 to 10: "))


while counter <= 12:
            multiplication_total = multiplication_number * counter
            print(multiplication_number, "x", counter, multiplication_total)
            counter = counter + 1
    
           
    
    
        #print("this option is not valid")
            
