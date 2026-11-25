pedido = [["Teclado", 2, 25.5], ["Ratón", 1, 12.0], ["Monitor", 1, 150.0]]

def resumen_pedido(productos : list, descuento : int = 0):
    # Devuelve: total de unidades
    # precio total con descuento aplicado 2 decimales
    # Nombre producto con mayor subtotal (unidades x precio) 

    totalUnidades = 0
    sumaPrecio = 0
    subTotal = productos[0][2] * productos[0][1]
    productoMayorSub = productos[0][0]

    for producto in productos:
        totalUnidades += producto[1]
        sumaPrecio += (producto[2] * producto[1])

        if subTotal < producto[2] * producto[1]:

            subTotal  = producto[2] * producto[1]
            productoMayorSub = producto[0]

    sumaPrecio *= ((100 - descuento) / 100)

    return totalUnidades,round(sumaPrecio,2),productoMayorSub


print(resumen_pedido(pedido, 10))

