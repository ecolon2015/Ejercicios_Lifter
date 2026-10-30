#Eduardo Colon
""" Cree un programa que permita agregar un Pokémon nuevo al archivo de la lección de Manejo de JSON.
Debe leer el archivo para importar los Pokémones existentes.
Luego debe pedir la información del Pokémon a agregar.
Finalmente debe guardar el nuevo Pokémon en el archivo. """


import json

def get_file_name():
    while True:
        file_name = input("Enter the file name eg. exercise_data.json ")

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

""" def get_integer(prompt):
    while True:
        try:
            good_value= int(input(prompt))
            return good_value
        except ValueError:
                print("Please enter a valid integer.")
"""

""" def get_data():

    name = input("Enter the Pokemon Name: ")
    type = input("Enter the Pokemon Type: ")
    while True:
        try:
            level= int(input("Enter your pokemon level "))
            break
        except ValueError:
            print("Please enter a valid integer.")

    while True:
        try:
            weight_kg = float(input("Enter the Pokemon weight in Kg: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    
    is_shiny = input("is the Pokemon shiny yes/no: ")
    if is_shiny.lower() == "yes":
        is_shiny = True
    else:
        is_shiny = False

    held_item = input("Enter the Pokemon held item or blank for none ")
    if held_item == "":
        held_item = None
    user_entries_list = 1
    
    skills_list = []
    while user_entries_list <= 4 :
        user_input = input(f"Enter skill #{user_entries_list}: ")
        skills_list.append(user_input)
        user_entries_list +=1

    
    hp = get_integer("Enter Pokemon HP: ")
    attack = get_integer("Enter Pokemon attack: ")
    defense = get_integer("Enter Pokemon defense: ")
    sp_attack = get_integer("Enter Pokemon special attack: ")
    sp_defense = get_integer("Enter Pokemon special defense: ")
    speed = get_integer("Enter Pokemon speed: ")
    
    pokemon_data = {
        "name" : name,
        "type" : type,
        "level" : level,
        "weight_kg" : weight_kg,
        "is_shiny"  : is_shiny,
        "held_item" : held_item,
        "skills": skills_list,
        "stats" : {
            "hp" : hp,
            "attack" : attack,
            "defense" : defense,
            "sp_attack" : sp_attack,
            "sp_defense" : sp_defense,
            "speed" :  speed
        }
    
    } 
    

    return pokemon_data """

def add_pokemon(existing_pokemon,new_pokemon):
    existing_pokemon.append(new_pokemon)


def save_pokemon_file(file_path, data):
    with open(file_path,'w',encoding='utf-8') as file:
        json.dump(data,file, indent=4) 



def main():
    file_name = get_file_name()
    existing_pokemon= read_pokemon_file(file_name)
    new_pokemon =  get_data()
    add_pokemon(existing_pokemon,new_pokemon)
    save_pokemon_file(file_name,existing_pokemon)

if __name__ == '__main__':
    main()
