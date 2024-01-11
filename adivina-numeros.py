def retornar_numero():
    """Genera y retorna un número random entre 1 y 5.
    """
    return rn(1, 5)

def quizz():
    """Pide al usuario que adivine el número generado y valida si es correcto.
    """
    numero = retornar_numero()
    while True:
        # Pide al usuario que ingrese un número
        pide_al_usuario = input("Adivina el número entre 1 y 5: ")
        try:
            # Verifica si el número ingresado es correcto
            if pide_al_usuario.isnumeric and int(pide_al_usuario)  == numero:
                print("¡¡¡congratulations!!! Has adivinado el número.")
                return
            else:
                print("Numero incorrecto")
            
        except Exception as Error:
            print(f"Por favor, ingresa un número. {Error}")
            
from random import randint as rn
if __name__ == '__main__':
    quizz()

