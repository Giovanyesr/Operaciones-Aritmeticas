def mcd(a, b):
    """
    Función para calcular el máximo común divisor (MCD) de dos números.
    Hola Giovany
    Args:
    a (int): El primer número entero.
    b (int): El segundo número entero.

    Returns:
    int: El máximo común divisor de a y b.
    """
    while b != 0:
        a, b = b, a % b
    return a


def ingresar_entero_positivo(mensaje):
    """
    Función para solicitar al usuario que ingrese un número entero positivo.

    Args:
    mensaje (str): El mensaje que se mostrará al usuario.

    Returns:
    int: El número entero positivo ingresado por el usuario.
    """
    while True:
        try:
            numero = int(input(mensaje))
            if numero >= 0:
                return numero  # Salir del bucle si la entrada es un número entero válido y positivo
            else:
                print("Por favor, ingrese un número entero positivo.")
        except ValueError:
            print("Por favor, ingrese solo números enteros.")


# Solicitar al usuario ingresar el primer número entero positivo
numero1 = ingresar_entero_positivo("Ingrese el primer número entero positivo: ")

# Solicitar al usuario ingresar el segundo número entero
numero2 = ingresar_entero_positivo("Ingrese el segundo número entero positivo: ")

# Calcular el máximo común divisor
resultado = mcd(numero1, numero2)

# Mostrar el resultado
print("El máximo común divisor de", numero1, "y", numero2, "es:", resultado)

