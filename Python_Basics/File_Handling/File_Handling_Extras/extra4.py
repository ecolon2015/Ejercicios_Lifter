#Eduardo Colon
""" Cree un programa que:
Pida al usuario una línea de texto
Agregue esa línea al final de un archivo existente
Si el archivo no existe, lo crea automáticamente
Ejemplo:
Entrada:
"Este es un nuevo registro"
Salida:
"El texto se agrega al final del archivo sin borrar lo anterior" """

def get_file_name():
    file_name = input("Enter the file name eg. append_file.txt ")
    return file_name

def get_data():
    line_of_text = input("Enter a line of text ")
    return line_of_text

def append_to_file(path, line_of_text):
    with open(path, 'a', encoding="utf-8") as file:
        file.write("\n " +  line_of_text)


def main():
    file_name = get_file_name()
    text= get_data()
    append_to_file(file_name,text)

if __name__ == '__main__':
    main() 