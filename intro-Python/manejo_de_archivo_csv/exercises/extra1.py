#Eduardo Colon
"""  Cree un programa que abra un archivo .csv con la información de videojuegos (el que fue generado en el ejercicio 1) y:
Lea cada línea usando csv.reader()
Muestre el contenido en pantalla de forma legible, línea por línea
Ejemplo:
Salida:
Nombre: Grand Theft Auto IV
Género: Accion
Desarrollador: Rockstar Games
Clasificación: M """

import csv

def get_file_name():
    file_name = input("Enter the file name to read the data from eg. video_games.csv ")
    return file_name

def read_video_games(file_path):
    with open(file_path,'r',encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for games in reader:
            print(f"Name: {games[0]}")
            print(f"Genre: {games[1]}")
            print(f"Developer: {games[2]}")
            print(f"Rating: {games[3]}") 


def main():
    file_name = get_file_name()
    read_video_games(file_name)

if __name__ == '__main__':
    main()
