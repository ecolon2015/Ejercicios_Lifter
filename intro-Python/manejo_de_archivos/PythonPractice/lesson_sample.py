def read_file_by_lines(path):
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        for number, line in enumerate(lines, start=1):
            print(f"Line {number}: {line.strip()}")
        return lines

def write_new_file(path,lines):
    lines.sort()
    with open(path, 'w', encoding='utf-8') as file:
        file.writelines(lines)
        



def main():
    text= read_file_by_lines('canciones.txt')
    write_new_file('new_canciones.txt',text)
if __name__ == '__main__':
    main() 