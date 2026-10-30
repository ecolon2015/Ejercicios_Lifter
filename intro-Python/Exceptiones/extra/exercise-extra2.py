
#Eduardo Colon
""" Cree una función convertir_a_entero(lista) que:
Reciba una lista de strings
Intente convertir cada elemento a entero usando int()
Use try-except para atrapar los errores ValueError
Si algún elemento no puede convertirse, mostrar "No se pudo convertir el elemento: <valor>" y continuar con los demás
Ejemplo:
Entrada:
my_list = ['4', 'hola', '10', '5.2']
Salida:
"Resultado:"
"4" "convertido a" 4
"No se pudo convertir el elemento: hola"
"10" "convertido a" 10
"No se pudo convertir el elemento: 5.2" """

def convert_to_integers(list):
    for integer_number in list:
            try:
                 integers=int(integer_number)
                 print(f' "{integer_number}" converted to {integers}')
            
            except ValueError:
                print(f"we can\'t convert the element: {integer_number}")




def main():
    my_list = ['4','hello','10','5.2']
    print("Result:")
    convert_to_integers(my_list)


if __name__ == '__main__':
    main()