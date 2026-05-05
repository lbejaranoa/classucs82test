import pytest
from app import validad_edad,validar_pedido
'''
#particion
def test_edad_valida():
    assert validad_edad(30) == True

def test_edad_invalida_menor():
    assert validad_edad(10) == False

def test_edad_invalida_mayor():
    assert validad_edad(70)== False

#limite
def test_limite_inferior_invalido():
    assert validad_edad(18)== False

def test_limite_inferior_valido(): 
    assert validad_edad(19)==True

def test_limite_superior_invalido():
    assert validad_edad(69)==False

def test_limite_superior_valido(): 
    assert validad_edad(68)==True
'''
'''
@pytest.mark.parametrize("edad, esperado",[
    (30,True),
    (10,False),
    (70,False),
    (18,False),
    (19,True),
    (69,False),
    (68,True)
])

def test_edades(edad,esperado):
    assert validad_edad(edad)==esperado

'''
def test_pedido_valido():
    assert validar_pedido(monto=100, cantidad=5,stock=10,cliente_activo=True)==True

def test_monto_valido(): 
    assert validar_pedido(monto=10, cantidad=5,stock=10,cliente_activo=True)==True

def test_monto_invalido(): 
    assert validar_pedido(monto=-10, cantidad=5,stock=10,cliente_activo=True)==False

def test_cantidad_valido(): 
    assert validar_pedido(monto=10, cantidad=5,stock=10,cliente_activo=True)==True

def test_cantidad_invalido(): 
    assert validar_pedido(monto=10, cantidad=15,stock=11,cliente_activo=True)==False

def test_stock_valido(): 
    assert validar_pedido(monto=10, cantidad=10,stock=16,cliente_activo=True)==True

def test_stock_invalido(): 
    assert validar_pedido(monto=10, cantidad=10,stock=6,cliente_activo=True)==False

def test_cliente_inactivo():
    assert validar_pedido(monto=10, cantidad=10,stock=16,cliente_activo=False)==False


@pytest.mark.parametrize("cantidad,esperado",[
    (0,False),
    (1,True),
    (10,True),
    (11,False)
])
def test_limites_cantidad(cantidad,esperado):
    assert validar_pedido(monto=100,cantidad=cantidad,stock=20,cliente_activo=True)==esperado