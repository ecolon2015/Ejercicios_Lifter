#Eduardo Colon
""" Cree un programa que permita agregar un Pokémon nuevo al archivo de la lección de Manejo de JSON.
Debe leer el archivo para importar los Pokémones existentes.
Luego debe pedir la información del Pokémon a agregar.
Finalmente debe guardar el nuevo Pokémon en el archivo. """


import json

def get_file_name():
    file_name = input("Enter the file name eg. exercise_data.json ")
    return file_name
#except (FileNotFoundError, json.JSONDecodeError): belong to exercise #2 to be more precise if the json file is corrupted
#didnt add, so my code look for beginners. 

def get_data():
    pokemons_data_list = []
    name = input("Enter the Pokemon Name: ")
    type = input("Enter the Pokemon Type: ")
    level= int(input("Enter your pokemon level "))
    weight_kg = float(input("Enter the Pokemon weight in Kg: "))
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
    hp = int(input("Enter Pokemon HP: "))
    attack = int(input("Enter Pokemon attack: "))
    defense = int(input("Enter Pokemon defense: "))
    sp_attack = int(input("Enter Pokemon special attack: "))
    sp_defense = int(input("Enter Pokemon special defense: "))
    speed  = int(input("Enter Pokemon speed: "))
    pokemon_data = {
        "name" : name,
        "type" : type,
        "level" : level,
        "weight_kg" : weight_kg,
        "is_shiny"  : is_shiny,
        "held_item" : held_item,
        "skills": skills_list,
        "stats" :{
            "hp" : hp,
            "attack" : attack,
            "defense" : defense,
            "sp_attack" : sp_attack,
            "sp_defense" : sp_defense,
            "speed" : speed
        }

    }
    pokemons_data_list.append(pokemon_data)

    return pokemons_data_list

def append_pokemon_games(file_path,pokemon_data):
    with open(file_path,'r',encoding='utf-8',newline="") as file:
        data= json.load(file)
        data.extend(pokemon_data)

    with open(file_path,'w',encoding='utf-8',newline="") as file:
        json.dump(data,file, indent=4)
        #for emp in data['employees']:
            #print(emp)
    

def main():
    file_name = get_file_name()
    text =  get_data()
    append_pokemon_games(file_name,text)

if __name__ == '__main__':
    main()
