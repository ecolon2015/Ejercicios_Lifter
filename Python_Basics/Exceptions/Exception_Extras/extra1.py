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

def get_name():
    name = input("Enter your Name: ")
    return name 
        
def validate_name(name):
    if name.isdigit():
        raise ValueError("your name can not be a number ")
    return name

def get_age():
    age = input("Enter your Age: ")
    return age      

def validate_age(age):
    try:
        age = int(age)
    except ValueError:
        raise ValueError("Age must be a valid number")

    if age < 1 or age > 100:
        raise ValueError("Age must be between 1 and 100")
    return age

def show_result(name,age):
    print(f"Hello {name}, your age is {age}")               

def main():

    try:
        name = get_name()
        name = validate_name(name)
        age = get_age()
        age = validate_age(age)
        show_result(name,age)
        
    except ValueError as ex:
        print(ex)


if __name__ == '__main__':
    main()