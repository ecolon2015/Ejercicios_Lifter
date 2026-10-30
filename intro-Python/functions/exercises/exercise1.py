
#Eduardo Colon
""" 
Cree dos funciones que impriman dos cosas distintas, 
y haga que la primera llame la segunda.

"""




def enter_your_name():
    name= (input("enter your name: "))
    print(f" Name:  {name } ")
    list_your_hobbies()
 

def list_your_hobbies():
    hobbies = ["play baseball","travel","reading"]
    print("hobbies: ", hobbies)

enter_your_name()
