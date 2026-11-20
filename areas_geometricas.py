# ----------------------------------------------------------
# Este modulo reune las funciones para calcular areas.
# Cada funcion recibe las medidas necesarias y devuelve
# el area calculada. No muestra mensajes por pantalla.
# ----------------------------------------------------------
import math # Modulo estandar: permite utilizar math.pi.

def area_rectangulo(base, altura):
    """Devuelve el area de un rectangulo."""
    return base * altura

def area_cuadrado(lado):
    """Devuelve el area de un cuadrado."""
    return lado * lado

def area_circulo(radio):
    """Devuelve el area de un circulo."""
    return math.pi * radio ** 2

# En esta version no se gestionan excepciones ni se validan
# valores negativos. Esa mejora se anyadira posteriormente.