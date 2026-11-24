def calcular_precio_final(precio : float, descuento : int = 0, iva : int = 21):
    descuentoAplicar = (100 - descuento) / 100
    ivaAplicar = 1 + (iva / 100)
    precioFinal = precio * descuentoAplicar * ivaAplicar
    
    return round(precioFinal,2) 

print(calcular_precio_final(100,10))