#Escribir un programa en phyton que permita clasificar triangulos (isoseles, escaleno, equilateroo rectangulo ) a partir de tres valores flotantes ingresados desde el teclado.
definir y utilizar al menos una referencia de herencia que incluya encasuplamiet, el programa debe repetirse continuamente hasta que uno de los supuestos triangulos no lo sea
Erick Romo

# aquí esta Encapsulamiento 
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__lado3 = lado3

    def get_lados(self):
        return self.__lado1, self.__lado2, self.__lado3

    def clasificar(self):
        lados = sorted(self.get_lados())
        a, b, c = lados

        # Verificar si es un triángulo válido
        if a + b <= c:
            return None  # No es un triángulo

        # Clasificación
        if a == b == c:
            return "Triángulo equilátero"
        elif a == b or b == c or a == c:
            return "Triángulo isósceles"
        else:
            return "Triángulo escaleno"

#Aquí esta la herencia
class TrianguloRectangulo(Triangulo):
    def es_rectangulo(self):
        lados = sorted(self.get_lados())
        a, b, c = lados
        return a**2 + b**2 == c**2


def main():
    while True:
        print("Ingrese las longitudes de los lados del triángulo (o ingrese -1 para salir):")
        lado1 = float(input("Lado 1: "))
        if lado1 == -1:
            break
        lado2 = float(input("Lado 2: "))
        if lado2 == -1:
            break
        lado3 = float(input("Lado 3: "))
        if lado3 == -1:
            break

        triangulo = Triangulo(lado1, lado2, lado3)
        clasificacion = triangulo.clasificar()

        if clasificacion is None:
            print("Los valores ingresados no forman un triángulo.")
            break

        print(clasificacion)

        # Comprobar si es un triángulo rectángulo
        triangulo_rectangulo = TrianguloRectangulo(lado1, lado2, lado3)
        if triangulo_rectangulo.es_rectangulo():
            print("Además, es un triángulo rectángulo.")

if __name__ == "__main__":
    main()
