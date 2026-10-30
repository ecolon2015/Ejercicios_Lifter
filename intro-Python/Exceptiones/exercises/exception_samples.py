try:
    name = input("Ingrese su nombre: ")
    if name.isdigit():
      raise ValueError()
except Exception as error:
	  # unhappy path
    print("Su nombre no puede ser un numero!")

# happy path
edad = input(f"Gracias {name}! Ahora ingrese su edad: ")
empleo = input(f"Gracias {name}! Ahora ingrese su empleo: ")