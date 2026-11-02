#Eduardo Colon
""" 4. Cree un programa que abra un archivo .csv con la información de videojuegos( en base al CSV que fue generado en el ejercicio 1) y:
Lea el archivo .csv con videojuegos
Pida al usuario ingresar el nombre de un desarrollador (ej. "Ubisoft")
Muestre todos los videojuegos desarrollados por esa empresa en formato legible:
Ejemplo:
Salida:
Videojuegos desarrollados por Ubisoft:
- Assassin's Creed II (Clasificación: M, Género: Aventura)
- Rayman Legends (Clasificación: E, Género: Plataforma) """

import csv

def get_file_name():
    file_name = input("Enter the file name to read the data from eg. video_games.csv ")
    return file_name


def get_data():
    developing_input = input("Enter the developer for the games e.g 'activision' ").lower()
    return developing_input


def read_video_games(file_path):
    with open(file_path,'r',encoding='utf-8') as file:
        video_games = csv.reader(file)
        next(video_games)

        list_to_keep_data_after_file_close = []
    
        for games in video_games:
            list_to_keep_data_after_file_close.append(games)

    return list_to_keep_data_after_file_close

    
def filter_video_games(video_games,developing_input):
    list_of_games=[]
    for games in video_games:   
        if games[2].lower() == developing_input:
            list_of_games.append(games)
            
    return list_of_games

        
def display_video_games (matching_games,developing_input):
    if len(matching_games) == 1:
        print(f"This is the game developed by {developing_input}:")
        
    elif len(matching_games) > 0:
        print(f"These are the games developed by {developing_input}:")

    else: 
        print(f"No games found")

    for games in matching_games:
        print(f"Name: {games[0]} (Rating: {games[3]},Genre: {games[1]} )")


def main():
    file_name = get_file_name()
    text = get_data()
    filter_games=read_video_games(file_name)
    matching_games= filter_video_games(filter_games,text)
    display_video_games (matching_games,text)

if __name__ == '__main__':
    main()
