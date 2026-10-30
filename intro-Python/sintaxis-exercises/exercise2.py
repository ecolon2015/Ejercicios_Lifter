
#Eduardo Colon
#Cree un programa que le pida al usuario su nombre, apellido, y edad, Y
 #muestre si es un bebé, niño, preadolescente, adolescente,
#adulto joven, adulto, o adulto mayor.

name = input("Enter your name: ")
last_name = input("Enter your last name: ")
age = int(input( "Enter your age "))

if age <= 2:
    message = "tu eres un bebe"
elif age <= 9:
    message = "tu eres un nino"
elif age <= 12:
    message = "tu eres un preadolescente"
elif age <= 17:
    message = "tu eres un adolescente"
elif age <= 29:
    message = "tu eres un adulto joven"
elif age <= 59:
    message = "tu eres un adulto"    
else:
    message = "tu eres un adulto mayor"   
print(message)
