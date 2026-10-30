#Eduardo Colon
""" Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:
Lea el archivo JSON
Agrupe los Pokémon por tipo (por ejemplo, "agua", "fuego", etc.)
Calcule y muestre el promedio de nivel para cada tipo:
Ejemplo:
Salida
Tipo: Agua → Promedio de nivel: 42.6
Tipo: Fuego → Promedio de nivel: 37.2
Tipo: Planta → Promedio de nivel: 30.4 """



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

    
def filter_pokemon(data):
    pokemon_by_type = {}
    
    for pokemon in data:
        pokemon_type = pokemon['type']

        if pokemon_type not in pokemon_by_type:
                pokemon_by_type[pokemon_type] = []
                
        pokemon_by_type[pokemon_type].append(pokemon)

    return pokemon_by_type


def get_average (pokemon_by_type):
    pokemon_average = {}

    for pokemon_type,pokemon_list in pokemon_by_type.items():
        total_level= 0

        for  pokemon in pokemon_list:
            total_level += pokemon['level']

        average = total_level / len(pokemon_list)
        pokemon_average[pokemon_type] = average

    return pokemon_average  


def display_pokemon(pokemon_average):
    for pokemon_type, average in pokemon_average.items():
            print(f"Type: {pokemon_type} →  Promedio de Nivel: {average}")


def main():
    file_name = get_file_name()
    existing_pokemon= read_pokemon_file(file_name)
    pokemon_by_type= filter_pokemon(existing_pokemon)
    pokemon_average =  get_average(pokemon_by_type)
    display_pokemon(pokemon_average)

if __name__ == '__main__':
    main()
