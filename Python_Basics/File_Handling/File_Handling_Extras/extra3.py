#Eduardo Colon
"""  Cree un programa que:
Lea un archivo línea por línea
Convierta cada línea a mayúsculas
Escriba el contenido en un nuevo archivo
Ejemplo:
Entrada:
# archivo original:
hola mundo
esto es python
Salida:
# archivo nuevo:
HOLA MUNDO
ESTO ES PYTHON   """

def read_file_by_lines(path):
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        uppercase_conversion = ""
        
        for line in lines:
            uppercase_conversion = uppercase_conversion + line.upper() 
            print(f"{line.strip()}")
        return uppercase_conversion

def write_new_file(path,lines):
    with open(path, 'w', encoding='utf-8') as file:
        file.write(lines)
        



def main():
    text= read_file_by_lines('uppercase_conversion_file.txt')
    write_new_file('new_uppercase_file.txt',text)
if __name__ == '__main__':
    main() 