#hacer un programa que muestre el total de una compra de un solo 
#producto calculando el isv y dar un descuento solamente cuando el importe de la compra sea mayor a 10000, sera de un 25%

precio=int(input("Ingrese el precio del producto: "))
cantidad=int(input("Ingrese la cantidad de productos: "))

subtotal=precio*cantidad


if subtotal>=10000:  
    descuento=subtotal*0.25
    print(f"Ha obtenido un descuento del 25% por su compra [{descuento}], ¡¡muchas gracias!!")
    isv=(subtotal-descuento)*0.15
    

else:
    descuento=0

total=isv+subtotal-descuento
print(f"Su factura a pagar es de: {total}")