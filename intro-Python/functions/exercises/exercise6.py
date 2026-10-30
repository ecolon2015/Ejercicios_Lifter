
#Eduardo Colon
#Cree una función que acepte un string con palabras separadas por un guion y retorne un string igual pero ordenado alfabéticamente.
#Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
#“python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”

string_to_arrange = "python-variable-funcion-computadora-monitor"

def arrange_string_alphabetically (string_to_arrange):
    words = string_to_arrange.split("-")
    words.sort()
    result="-".join(words)
    return result

result= arrange_string_alphabetically(string_to_arrange)
print(result)

