#Eduardo Colon
#Pasa los Ejercicios de Pseudocódigo previamente creados a código:
#Cree un programa que le pida un precio de producto al usuario, calcule su descuento y muestre el precio final tomando en cuenta que:
#Si el precio es menor a 100, el descuento es del 2%.
#Si el precio es mayor o igual a 100, el descuento es del 10%.
#Ejemplos:
#120 → 108
#40 → 39.2

product_price=int(input("Enter the price for the product "))

if product_price < 100:
    discount=  product_price * 0.02
else:
    discount= product_price * 0.1
final_price= product_price- discount

print("the final price with discount is: ", final_price)