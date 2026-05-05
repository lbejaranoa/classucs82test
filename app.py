#edad mayor a 18 y menor a 69
def validad_edad(edad):
    if edad>18 and edad <69:
        return True
    else: 
        return False

'''
Regla
Monto > 0 
Cantidad entre 1 y 10 
Stock producto debe alcanzar a lo solicitado
Cliente activo
'''
def validar_pedido(monto,cantidad,stock,cliente_activo):
    if monto <=0:
        return False
    if cantidad <1 or cantidad>12: 
        return False
    if stock < cantidad: 
        return False
    if cliente_activo is not True: 
        return False

    return True