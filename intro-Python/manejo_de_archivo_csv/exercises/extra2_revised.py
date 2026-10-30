#Eduardo Colon
""" Cree un programa que abra un archivo .csv con la información de videojuegos ( en base al CSV que fue generado en el ejercicio 1) y:
Lea el archivo CSV de videojuegos
Pida al usuario una clasificación ESRB (por ejemplo: "T")
Muestre todos los videojuegos que tengan esa clasificación """

import csv

def get_file_name():
    file_name = input("Enter the file name to read the data from eg. video_games.csv ")
    return file_name


def get_data():
    rating_input = input("Enter the rating for the games e.g 'T' ").upper()
    return rating_input
    

def read_video_games(file_path):
    with open(file_path,'r',encoding='utf-8') as file:
        video_games = csv.reader(file)
        next(video_games)

        list_to_keep_data_after_file_close = []

        for games in video_games:
            list_to_keep_data_after_file_close.append(games)

    return list_to_keep_data_after_file_close

    
def filter_video_games(video_games,rating_input):
    list_of_games=[]
    for games in video_games:   
        if games[3].upper() == rating_input:
            list_of_games.append(games)
            
    return list_of_games
        

def display_video_games (matching_games,rating_input):
    if len(matching_games) == 1:
        print(f"There is {len(matching_games)} game that has the rating {rating_input}")

    elif len(matching_games) > 0:
        print(f"There are {len(matching_games)} games that have the rating {rating_input}")

    else: 
        print(f"No games found")

    for games in matching_games:
        print(f"name: {games[0]}")


def main():
    file_name = get_file_name()
    text = get_data()
    filter_games= read_video_games(file_name)
    matching_games = filter_video_games(filter_games,text)
    display_video_games(matching_games,text)

if __name__ == '__main__':
    main()
