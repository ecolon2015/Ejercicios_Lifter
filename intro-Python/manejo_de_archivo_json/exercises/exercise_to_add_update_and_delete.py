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

def get_integer(prompt):
    while True:
        try:
            good_value= int(input(prompt))
            return good_value
        except ValueError:
                print("Please enter a valid integer.")


def get_data():

    name = input("Enter the Pokemon Name: ")
    pokemon_type = input("Enter the Pokemon Type: ")

    level= get_integer("Enter your pokemon level ")

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
        "type" : pokemon_type,
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
    

    return pokemon_data

def add_pokemon(existing_pokemon,new_pokemon):
    existing_pokemon.append(new_pokemon)


def save_pokemon_file(file_path, data):
    with open(file_path,'w',encoding='utf-8') as file:
        json.dump(data,file, indent=4) 


def get_pokemon_name_to_update():
    update_pokemon_name = input("Which Pokemon's level would you like to update? ").lower()
    
    return update_pokemon_name

def find_pokemon(existing_pokemon,update_pokemon_name):
    pokemon_to_update_list= []
    for pokemon in existing_pokemon:
        if pokemon['name'].lower() == update_pokemon_name:
            pokemon_to_update_list.append(pokemon)

    if len(pokemon_to_update_list) == 0:      
        print("No Pokemon found")

    return pokemon_to_update_list

def update_pokemon(pokemon_to_update_list):
    for pokemon_update in pokemon_to_update_list:
        input_variable = get_integer("Enter a new level ")
        pokemon_update['level'] = input_variable

        
def get_pokemon_name_to_delete():
    pokemon_name_to_delete = input("which Pokemon name would you like to delete ").lower()
    return pokemon_name_to_delete


def delete_pokemon(existing_pokemon,deleted_pokemon):
    for pokemon_to_delete in deleted_pokemon:
        existing_pokemon.remove(pokemon_to_delete)

def get_new_pokemon_name():
    #new_pokemon_name = get_new_pokemon_name("Enter the new pokemon name: ")

    new_pokemon_name = input("Enter the new pokemon name:  ")

    return new_pokemon_name


def rename_pokemon(pokemon_name_for_editing,new_pokemon_name):
    for new_pokemon in pokemon_name_for_editing:
            #input_variable = get_integer("Enter a new pokemon name ")
            new_pokemon['name'] = new_pokemon_name



def main():

    file_name = get_file_name()
    existing_pokemon= read_pokemon_file(file_name)
    new_pokemon =  get_data()
    add_pokemon(existing_pokemon,new_pokemon)
    
    update_old_pokemon = get_pokemon_name_to_update()
    update_new_pokemon = find_pokemon(existing_pokemon,update_old_pokemon)
    update_pokemon(update_new_pokemon)
    save_pokemon_file(file_name,existing_pokemon)

    pokemon_to_delete= get_pokemon_name_to_delete()
    deleted_pokemon = find_pokemon(existing_pokemon,pokemon_to_delete)
    delete_pokemon(existing_pokemon,deleted_pokemon)
    save_pokemon_file(file_name,existing_pokemon)

    edit_old_pokemon_name= get_pokemon_name_to_update()
    pokemon_name_for_editing = find_pokemon(existing_pokemon,edit_old_pokemon_name)
    new_pokemon_name= get_new_pokemon_name()
    rename_pokemon(pokemon_name_for_editing,new_pokemon_name)
    save_pokemon_file(file_name,existing_pokemon)

if __name__ == '__main__':
    main()
