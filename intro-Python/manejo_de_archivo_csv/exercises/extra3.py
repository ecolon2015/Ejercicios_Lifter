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
        reader = csv.reader(file)
        next(reader)

        genre_counts = {}

        for games in reader:
            genre = games[1]
            if genre in genre_counts: 
                genre_counts[genre]= genre_counts[genre]+ 1
            else:
                genre_counts[genre] = 1

        genres =sorted(genre_counts)
        print("Generos encontrados:")
        for genre in genres:
            print(f"{genre}: {genre_counts[genre]}")


def main():
    file_name = get_file_name()
    read_video_games(file_name)

if __name__ == '__main__':
    main()
