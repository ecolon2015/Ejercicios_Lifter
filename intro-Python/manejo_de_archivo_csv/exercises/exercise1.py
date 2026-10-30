#Eduardo Colon
""" Cree un programa que me permita ingresar información de n cantidad de videojuegos y los guarde en un archivo csv.
Debe incluir:
Nombre
Género
Desarrollador
Clasificación ESRB
Ejemplo de archivo final:
nombre,genero,desarrollador,clasificacion
Grand Theft Auto IV,Accion,Rockstar Games,M
The Elder Scrolls IV: Oblivion,RPG,Bethesda,M
Tony Hawk's Pro Skater 2,Deportes,Activision,T """

import csv

def get_file_name():
    file_name = input("Enter the file name eg. video_games.csv ")
    return file_name

def get_data():
    video_games_data =  []
    while True:
        name = input("Enter the video game Name ")
        genre = input("Enter the Genre ")
        developer = input("Enter the Developer ")
        rating = input("Enter the ESRB Rating ")

        video_games = {
            "name" : name,
            "genre" : genre,
            "developer" : developer,
            "rating" : rating,
        }
        video_games_data.append(video_games)

        proceed = input("do you want to add another game Yes/No ")
        if proceed.lower() != "yes":
            break
        
    return video_games_data

def save_video_games(file_path,video_games_data):
    with open(file_path,'w',encoding='utf-8',newline="") as file:
        headers = ["name","genre","developer","rating"]
        writer = csv.DictWriter(file,fieldnames=headers)
        writer.writeheader()
        writer.writerows(video_games_data)



def main():
    file_name = get_file_name()
    text =  get_data()
    save_video_games(file_name,text)

if __name__ == '__main__':
    main()
