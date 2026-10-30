def read_complete_file(path):
    # Usamos 'with' para un manejo seguro del archivo
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)

#read_complete_file('quijote.txt')


def main():

  # relative_file=open('quijote.txt')
   read_complete_file('quijote.txt')

if __name__ == '__main__':
    main()