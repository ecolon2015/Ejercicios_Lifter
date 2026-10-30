
#Eduardo Colon
#Cree un programa que use una lista para eliminar keys de un diccionario.
#Ejemplos:
#list_of_keys = [’access_level’, ‘age’]
#employee = {’name’: ‘John’, ‘email’: ‘john@ecorp.com’, ‘access_level’: 5, ‘age’: 28}
#→ {’name’: ‘John’, 'email’: ‘john@ecorp.com’}

list_of_keys = ['access_level','age']
deleted_keys ={}

employee = {
    'name': 'John',
    'email':'john@corp.com',
    'access_level': 5,
    'age': 28
}
for key in list_of_keys:
  deleted_keys[key]=employee.pop(key)

print(employee)
print(deleted_keys)