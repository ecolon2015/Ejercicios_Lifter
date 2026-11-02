#Eduardo Colon
#Cree una calculadora por linea de comando. Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número:
#1. Suma
#2. Resta
#3. Multiplicación
#4. División
#5. Borrar resultado
#Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar, o dividir por el actual. El resultado debe pasar a ser el nuevo numero actual.
#Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, o si ingresa un número invalido a la hora de hacer la operación.




def show_menu(actual_number):
    print("--- Calculator ---")
    print("Actual Number:", actual_number)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Reset")
    print("6. Exit")


def choose_number():
    option = input("Choose an option: ")
    return option


def process_calculation(option, actual_number):
    try:
        new_number = int(input("Enter another number to calculate: "))
    except ValueError:
        print("You must enter a valid number")
        return actual_number

    if option == "1":
        actual_number = actual_number + new_number

    elif option == "2":
        actual_number = actual_number - new_number

    elif option == "3":
        actual_number = actual_number * new_number

    elif option == "4":
        if new_number == 0:
            print("Error, you can't divide by zero")
            return actual_number

        actual_number = actual_number / new_number

    print("Result:", actual_number)

    return actual_number


def main():
    actual_number = 0

    while True:
        show_menu(actual_number)

        option = choose_number()

        if option == "5":
            actual_number = 0
            print("Result erased. The actual number is now 0.")

        elif option == "6":
            print("Exiting Calculator")
            break

        elif option in ("1", "2", "3", "4"):
            actual_number = process_calculation(option, actual_number)

        else:
            print("Option is not valid")


if __name__ == '__main__':
    main()