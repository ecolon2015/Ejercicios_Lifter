#Eduardo  Colon
""" Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:
Lea el archivo JSON de Pokémon
Recorra la lista de Pokémon y muestre en consola su nombre, tipo y nivel (o cualquier otro atributo definido) """




import json


def get_file_name():
    while True:
        file_name = input("Enter the file name to read data from eg. exercise_data.json ")

        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                json.load(file)
            return file_name

        except FileNotFoundError:
            print("File not found. Please check the filename.")


def read_pokemon_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def display_pokemon(existing_pokemon):
    if len(existing_pokemon) == 1:
            print("The following Pokemon was found:")

    elif  len(existing_pokemon) > 0:
        print("The following Pokemon were found")
    else:
        print("No Pokemon found")

    for pokemon in existing_pokemon:
        print(f"Name: {pokemon['name']}")
        print(f"Type: {pokemon['type']}")
        print(f"Level: {pokemon['level']}")


def main():
    file_name = get_file_name()
    existing_pokemon= read_pokemon_file(file_name)
    display_pokemon(existing_pokemon)
    
if __name__ == '__main__':
    main()
