import pytest
from areas_geometricas import area_rectangulo, area_cuadrado, area_circulo
 

def test_area_rectangulo_25():
    assert area_rectangulo(2,5) == 10
def test_area_rectangulo_20():
    assert area_rectangulo(0,5) == 0
def test_area_rectangulo_Type():
    area_rectangulo(-10, 0) == None
def test_area_rectangulo_Value():
    area_rectangulo("r", 0) == None


def test_area_cuadrado_5():
    assert area_cuadrado(5) == 25
def test_area_cuadrado0():
    assert area_cuadrado(0) == 0
def test_area_cuadrado_Type():
    area_cuadrado(-10) == None
def test_area_cuadrado_Value():
    with pytest.raises(TypeError):
        area_cuadrado("p")
    

def test_area_circulo_2():
    assert area_circulo(2) == 12.566370614359172
def test_area_circulo_0():
    assert area_circulo(0) == 0
def test_area_circulo_Type():
    area_circulo(-10) == None
def test_area_circulo_Value():
    with pytest.raises(TypeError):
        area_circulo("p")