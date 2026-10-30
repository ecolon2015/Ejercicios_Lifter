
#Eduardo Colon
""" Cree una función sumar_valores(lista) que:
Reciba una lista de elementos (strings, enteros, flotantes mezclados)
Intente convertir cada elemento a tipo float
Si puede, sume el valor y muestre: "<valor> sumado correctamente"
Si no puede, muestre: "Elemento inválido: <valor>"
Al final, imprima la suma total
Ejemplo:
Entrada:
my_list = ['10', 'manzana', '5.5', '3', 'n/a']
Salida:
10.0 "sumado correctamente"
"Elemento inválido: manzana"
5.5 "sumado correctamente"
3.0 "sumado correctamente"
"Elemento inválido: n/a"
"Total de la suma:" 18.5 """

def add_values(mix_list):
    addition_of_float = 0.0
    for mix_values in mix_list:
        try: 
            float_number = float(mix_values)
            addition_of_float =  addition_of_float + float_number
            print(f'{float_number} "added correctly"')
            
        except ValueError:
            print(f'Invalid element: {mix_values}')

    print(f"The Total of the addition is: {addition_of_float}")




def main():
    my_list = ['10','apple','5.5','3','n/a' ]
    print("Result: ")
    add_values(my_list)


if __name__ == '__main__':
    main()
