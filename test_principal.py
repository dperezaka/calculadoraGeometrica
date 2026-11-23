import pytest
from principal import leer, mostrar_menu, main

def test_leer_int(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda texto: "5")
    assert leer("Número: ", int) == 5

def test_leer_float(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda texto: "5.9")
    assert leer("Número: ", float) == 5.9

def test_leer_int_0(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda texto: "0")
    assert leer("Número: ", int) == 0

def test_leer_float_0(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda texto: "0")
    assert leer("Número: ", float) == 0

def test_leer_int_mal(monkeypatch):
    respuestas = iter(["p", "7"])
    monkeypatch.setattr("builtins.input", lambda texto: next(respuestas))
    assert leer("Número: ", int) == 7

def test_leer_float_mal(monkeypatch):
    respuestas = iter(["p", "7.5"])
    monkeypatch.setattr("builtins.input", lambda texto: next(respuestas))
    assert leer("Número: ", float) == 7.5

def test_leer_int_negativo(monkeypatch):
    respuestas = iter(["-5", "3"])
    monkeypatch.setattr("builtins.input", lambda texto: next(respuestas))
    assert leer("Número: ", int) == 3

def test_leer_float_negativo(monkeypatch):
    respuestas = iter(["-5.5", "3.2"])
    monkeypatch.setattr("builtins.input", lambda texto: next(respuestas))
    assert leer("Número: ", float) == 3.2
    
############################################################################

def test_mostrar_menu_salida_exacta(capsys):
    mostrar_menu()
    salida = capsys.readouterr().out

    esperado = (
        "===== CALCULADORA GEOMETRICA =====\n"
        "1. Calcular area de un rectangulo\n"
        "2. Calcular area de un cuadrado\n"
        "3. Calcular area de un circulo\n"
        "0. Salir\n"
    )
    assert salida == esperado
    
def test_mostrar_menu_contiene_opciones(capsys):
    mostrar_menu()
    salida = capsys.readouterr().out
    assert "CALCULADORA GEOMETRICA" in salida
    assert "1. Calcular area de un rectangulo" in salida
    assert "2. Calcular area de un cuadrado" in salida
    assert "3. Calcular area de un circulo" in salida
    assert "0. Salir" in salida    

###########################################################################

def simular_entradas(monkeypatch, *respuestas):
    """Hace que input() devuelva las respuestas en orden, una por llamada."""
    entradas = iter(respuestas)
    monkeypatch.setattr("builtins.input", lambda mensaje: next(entradas))


def test_rectangulo(monkeypatch, capsys):
    # opcion 1, base 4, altura 5, y luego 0 para salir
    simular_entradas(monkeypatch, "1", "4", "5", "0")
    main()
    salida = capsys.readouterr().out
    assert "El area del rectangulo es: 20.00" in salida


def test_cuadrado(monkeypatch, capsys):
    simular_entradas(monkeypatch, "2", "3", "0")
    main()
    salida = capsys.readouterr().out
    assert "El area del cuadrado es: 9.00" in salida


def test_circulo(monkeypatch, capsys):
    simular_entradas(monkeypatch, "3", "1", "0")
    main()
    salida = capsys.readouterr().out
    assert "El area del circulo es: 3.14" in salida


def test_opcion_no_valida(monkeypatch, capsys):
    simular_entradas(monkeypatch, "7", "0")
    main()
    salida = capsys.readouterr().out
    assert "Opcion no reconocida" in salida


def test_salir(monkeypatch, capsys):
    simular_entradas(monkeypatch, "0")
    main()
    salida = capsys.readouterr().out
    assert "Hasta pronto" in salida
