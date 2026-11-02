#Eduardo  Colon
""" Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y::
Lea el archivo JSON de Pokémon
Pida al usuario un tipo de Pokémon
Muestre todos los Pokémon que sean de ese tipo
Ejemplo:
Entrada:
"Ingrese el tipo de pokemon desea buscar(agua,electrico,fuego,etc): " 
"Fuego"

Salida:
"Los pokemos que existen de ese tipo son: "
Charmander
Growlithe
Victini
"""


import json

def get_file_name():
    while True:
        file_name = input("Enter the file name to read data from eg. exercise_data.json  ")

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


def get_data():
    pokemon_type = input("Enter the Pokemon Type that you want to find(water,electric,fire): ").lower()
    return pokemon_type
    
    
def filter_pokemon(data,pokemon_type):
    list_of_pokemon = []
    for pokemon in data:
        if pokemon['type'].lower() == pokemon_type:
            list_of_pokemon.append(pokemon)

    return list_of_pokemon


def display_pokemon(matching_pokemon_type):
    if len(matching_pokemon_type) == 1:
        print("The Pokemon of this type is:")
        
    elif len(matching_pokemon_type) > 0:
        print("The Pokemon of this type are:")

    else:
        print("No Pokemon found")

    for pokemon in matching_pokemon_type:
        print(f"{pokemon['name']}")


def main():
    file_name = get_file_name()
    existing_pokemon= read_pokemon_file(file_name)
    pokemon_type_data =  get_data()
    matching_pokemon_type= filter_pokemon(existing_pokemon,pokemon_type_data)
    display_pokemon(matching_pokemon_type)

if __name__ == '__main__':
    main()
