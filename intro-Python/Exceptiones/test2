def calculadora():
    numero_actual = 0.0

    while True:
        print("\n==============================")
        print(f"Número actual: {numero_actual}")
        print("==============================")
        print("Seleccione una operación:")
        print("1. Suma (+)")
        print("2. Resta (-)")
        print("3. Multiplicación (*)")
        print("4. División (/)")
        print("5. Borrar resultado (Reset)")
        print("6. Salir")
        
        opcion = input("Opción (1-6): ").strip()

        if opcion == '6':
            print("¡Gracias por usar la calculadora!")
            break

        if opcion == '5':
            numero_actual = 0.0
            print("Resultado borrado. El número actual ahora es 0.")
            continue

        if opcion in ['1', '2', '3', '4']:
            # Validar que el segundo número sea válido
            try:
                nuevo_numero = float(input("Ingrese el siguiente número: "))
            except ValueError:
                print("Error: Entrada inválida. Debe ingresar un número válido.")
                continue

            # Ejecutar la operación seleccionada
            if opcion == '1':
                numero_actual += nuevo_numero
            elif opcion == '2':
                numero_actual -= nuevo_numero
            elif opcion == '3':
                numero_actual *= nuevo_numero
            elif opcion == '4':
                if nuevo_numero == 0:
                    print("Error: No se puede dividir entre cero.")
                else:
                    numero_actual /= nuevo_numero
        else:
            print("Error: Opción inválida. Por favor, seleccione un número del 1 al 6.")

if __name__ == "__main__":
    calculadora()
