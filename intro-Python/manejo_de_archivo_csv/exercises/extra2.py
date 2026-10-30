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
    
def read_video_games(file_path,rating_input):
    with open(file_path,'r',encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)

        print(f"These are the games that have the rating {rating_input}")
        for games in reader:
            if games[3].upper() == rating_input:
                print(f"Name: {games[0]}")


def main():
    file_name = get_file_name()
    text = get_data()
    read_video_games(file_name, text)

if __name__ == '__main__':
    main()
