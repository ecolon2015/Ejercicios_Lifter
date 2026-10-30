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
    developing_input = input("Enter the developer for the games e.g 'Activision' ").capitalize()
    return developing_input
    
def read_video_games(file_path,developing_input):
    with open(file_path,'r',encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)

        print(f"These are the games developed by {developing_input}:")
        for games in reader:
            if games[2].capitalize() == developing_input:
                print(f"Name: {games[0]} (Rating: {games[3]},Genre: {games[1]} )")


def main():
    file_name = get_file_name()
    text = get_data()
    read_video_games(file_name, text)

if __name__ == '__main__':
    main()
