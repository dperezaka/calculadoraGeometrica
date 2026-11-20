# ----------------------------------------------------------
# Programa principal de calculadoraGeometrica.
# Presenta un menu, solicita las medidas y muestra el area.
# Los calculos se realizan en el modulo areas_geometricas.
# ----------------------------------------------------------
import areas_geometricas # Importamos nuestro modulo propio.
def mostrar_menu():
    """Muestra por pantalla las opciones disponibles."""
    print("\n===== CALCULADORA GEOMETRICA =====")
    print("1. Calcular area de un rectangulo")
    print("2. Calcular area de un cuadrado")
    print("3. Calcular area de un circulo")
    print("0. Salir")
def main():
    """Controla el flujo principal de la aplicacion."""
    # El menu se repite mientras no se elija la opcion 0.
    while True:
        mostrar_menu()
        # input() obtiene texto; int() lo convierte a entero.
        opcion = int(input("Selecciona una opcion: "))
        if opcion == 1:
            # Solicitamos las dos dimensiones del rectangulo.
            base = float(input("Introduce la base: "))
            altura = float(input("Introduce la altura: "))
            resultado = areas_geometricas.area_rectangulo(base, altura)
            print(f"El area del rectangulo es: {resultado:.2f}")
        elif opcion == 2:
            # Para el cuadrado solo necesitamos conocer el lado.
            lado = float(input("Introduce el lado: "))
            resultado = areas_geometricas.area_cuadrado(lado)
            print(f"El area del cuadrado es: {resultado:.2f}")
        elif opcion == 3:
            # Para el circulo solicitamos el radio.
            radio = float(input("Introduce el radio: "))
            resultado = areas_geometricas.area_circulo(radio)
            print(f"El area del circulo es: {resultado:.2f}")
        elif opcion == 0:
            print("Gracias por utilizar la calculadora. !Hasta pronto!")
            break # Finaliza el bucle while.
        else:
            print("Opcion no reconocida. Selecciona 0, 1, 2 o 3.")
# Este condicional comprueba como se esta ejecutando el archivo.
# Si se ejecuta directamente, se llama a main().
# Si se importa desde otro archivo, main() no se ejecuta solo.
if __name__ == "__main__":
    main()
# IMPORTANTE: esta version todavia no utiliza try/except.
# Una entrada no numerica provocara un error de conversion.
# La validacion de entradas y las excepciones se anyadiran
# en una version posterior del proyecto.