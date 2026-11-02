
#Eduardo Colon
#Cree un programa que cree un diccionario usando dos listas del mismo tamaño, 
# usando una para sus keys, y la otra para sus values.
#Ejemplos:
#list_a = [’first_name’, ‘last_name’, ‘role’]
#list_b = [’Alek’, ‘Castillo’, ‘Software Engineer’]
# → {’first_name’: ‘Alek’, ‘last_name’: ‘Castillo’, ‘role’: ‘Software Engineer’}

my_list_of_member_heading = ['first_name','last_name','role']
my_list_of_member_values = ['Alek', 'Castillo','Software Engineer']

team_members = {}

for index in range(len(my_list_of_member_heading)):
    team_members[my_list_of_member_heading[index]]= my_list_of_member_values[index]
print(team_members) 
