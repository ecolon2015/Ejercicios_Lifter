#Eduardo colon
#Cree un programa que abra un archivo de texto y cuente cuántas palabras contiene en total.
#(Considere que las palabras están separadas por espacios y/o saltos de línea)
#Ejemplo:
#Salida:
#"Este archivo contiene " 123 "palabras"


def count_words(path):
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.read()
        words= lines.split()
        return len(words)
        



def main():
    word_count_result=count_words('count_file.txt')
    print(f"this file contains {word_count_result} words")
if __name__ == '__main__':
    main() 