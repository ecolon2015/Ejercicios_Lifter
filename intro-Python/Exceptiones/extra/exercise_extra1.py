
#Eduardo Colon
#Cree un programa que:
#Pida al usuario su nombre
#Si el nombre es numérico (isdigit()), haga raise ValueError("El nombre no puede ser un número")
#Ejemplo:
#"Ingrese su nombre: " 5
#"El nombre no puede ser un número"
#Luego pida su edad
#Si no es un número válido, capture el ValueError y muestre un mensaje
#Ejemplo:
#Entrada:
#"Ingrese su edad: " cinco
#Salida:
#"Número no valido"
#Si todo sale bien, imprima un mensaje: "Hola <nombre>, su edad es <edad>"
#Ejemplo:
#Entrada:
#grese su nombre: " "Jean Carlo"
#"Ingrese su edad: " 27
#Salida
#Hola Jean Carlo, su edad es 27

def ask_for_user_information():
    try:
        name = input("Enter your Name: ")
        if name.isdigit():
            raise ValueError("your name can not be a number ")
        
        try:
            age = int(input("Enter your Age: "))
            
        except ValueError:
            print("This number is not valid")
            return

        if age < 1 or age > 100:
            raise ValueError("this number is not valid")
        
        print(f"Hello {name}, your age is {age}")
        
    except ValueError as ex:
        print(ex)
  
    
    

def main():
    ask_for_user_information()


if __name__ == '__main__':
    main()