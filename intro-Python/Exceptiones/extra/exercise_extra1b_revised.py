
# Eduardo Colon

def get_name():
    return input("Enter your Name: ")


def validate_name(name):
    if name.isdigit():
        raise ValueError("The name cannot be a number")
    return name


def get_age():
    return input("Enter your Age: ")


def validate_age(age):
    try:
        age = int(age)
    except ValueError:
        raise ValueError("Age must be a valid number")

    if age < 1 or age > 100:
        raise ValueError("Age must be between 1 and 100")

    return age


def show_result(name, age):
    print(f"Hello {name}, your age is {age}")


def main():
    try:
        name = get_name()
        name = validate_name(name)

        age = get_age()
        age = validate_age(age)

        show_result(name, age)

    except ValueError as error:
        print(error)


if __name__ == '__main__':
    main()