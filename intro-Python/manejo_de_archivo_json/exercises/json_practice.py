#Eduardo Colon
#this is a practice how to work with json data

import json

def read_json_file ( path):
    with open(path, 'r', encoding='utf-8') as file:
        data= json.load(file)
        print(data['employees'])

    for emp in data['employees']:
        print(emp)


def main():
    text= read_json_file('data.json')
if __name__ == '__main__':
    main() 