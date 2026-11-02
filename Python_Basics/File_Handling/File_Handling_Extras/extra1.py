#Eduardo Colon
#1. Cree un programa que lea un archivo con texto línea por línea, quite los saltos de línea (\n) y escriba todo el contenido en un solo renglón en un nuevo archivo
#Ejemplo:
#Entrada:
#Hola
#mundo
#esto
#es
#Python
#Salida:
#"Hola mundo esto es Python"

def read_file_by_lines(path):
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        all_text = ""
        for line in lines:
            all_text = all_text + line.strip() + " "
            print(f"{line.strip()}")
        return all_text
    
def write_new_file(path,lines):
    with open(path, 'w', encoding='utf-8') as file:
        file.writelines(lines)
        



def main():
    text= read_file_by_lines('extra.txt')
    write_new_file('new_extra.txt',text)
if __name__ == '__main__':
    main() 