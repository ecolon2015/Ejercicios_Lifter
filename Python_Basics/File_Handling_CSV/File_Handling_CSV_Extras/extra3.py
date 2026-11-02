#Eduardo Colon
""" Cree un programa que abra un archivo .csv con la información de videojuegos ( en base al CSV que fue generado en el ejercicio 1) y:
Lea el archivo .csv con videojuegos
Cuente cuántos videojuegos hay de cada género
Muestre el resultado de forma ordenada
Ejemplo:
Salida:
Géneros encontrados:
Acción: 5
Aventura: 3
Deportes: 4
...
 """

import csv

def get_file_name():
    file_name = input("Enter the file name to read the data from eg. video_games.csv ")
    return file_name

    
def read_video_games(file_path):
    with open(file_path,'r',encoding='utf-8') as file:
        video_games = csv.reader(file)
        next(video_games)

        list_to_keep_data_after_file_close = []

        for games in video_games:   
            list_to_keep_data_after_file_close.append(games)

    return list_to_keep_data_after_file_close


def count_games_by_genre(video_games):
    genre_counts = {}
    for games in video_games:  
        genre = games[1]
        if genre in genre_counts: 
                genre_counts[genre]= genre_counts[genre]+ 1
        else:
                genre_counts[genre] = 1

    return genre_counts


def display_video_games (matching_games):
    if len(matching_games) > 0:
        print("Generos encontrados:")

    else:
            print(f"No genre found")

    for games in sorted(matching_games):
        print(f"{games}: {matching_games[games]} ")

    

def main():
    file_name = get_file_name()
    filter_games= read_video_games(file_name)
    matching_games = count_games_by_genre(filter_games)
    display_video_games(matching_games)

if __name__ == '__main__':
    main()
