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