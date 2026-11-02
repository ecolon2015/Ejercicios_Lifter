
#Eduardo Colon
#Cree un diccionario que guarde la siguiente información sobre un hotel:
#nombre,numero_de_estrellas, habitaciones
#El value del key de habitaciones debe ser una lista, y cada habitación debe tener la siguiente información:
#numero,,piso, precio_por_noche

hotel_information = {
    'name': 'Sheraton',
    'number_of_stars' :  5,
    'rooms':  [
        {
            'number' : 104,
            'floor': 4,
            'price_per_night' : 120.00,
        },
        {
            'number' : 105,
            'floor': 3,
            'price_per_night' : 100.00,
        },
    ],  
}
print(f" Price per night: {hotel_information['rooms'][0]['price_per_night']}")
print(hotel_information)
