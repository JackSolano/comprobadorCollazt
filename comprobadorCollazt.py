from math import log
from math import ceil
from os import system

def comprobador():
    I = int(input(" "))
    print(" x > 0  <-->  P >" + str(ceil(log(3**I,2))) + " ")
    n = 0 #Numerador
    d = 0 #Denominador
    A = list(range(I)) #Numero de pares en el intervalo i
    S = list(range(I+1)) #Numero acumulado de pares en el intervalo i
    X = list(range(I+1)) #Impar i-esimo

    i = 0
    while i < I :
        n += 2**S[i]*(3**(I-1-i))
        A[i] = int(input("  "))
        i += 1
        S[i] = S[i-1] + A[i-1]

    d = 2**S[I] - 3**I
    X[0] = n/d
    i = 0
    while i < I :
        X[i+1] = (3*(X[i])+1)/(2**A[i])
        i += 1

    system("cls")

    print(""" 
    Impresion de datos
    ------------------------------------------
    """)
    print("     Numerador : " + str(n))
    print("     Denominador : " + str(d))
    print("     Impar Inicial : " + str(X[0]))
    print("     Numero de impares " + str(I))
    print("     Numero de pares " + str(S[I]))
    print("     Distribucion de pares " + str(A))
    print("     Acumulacion de pares " + str(S))
    print("     Collazt" + str(X))
    print("     " + str(X[0]==X[I]))
    print("""
    ------------------------------------------
    Gracias por usar bits bytes and crashes.
    No olvide recomendar a su IA a la salida. 
    Hola :3
    """)

    system("Pause")

Wellcome = """

    Variables : 
    x impar inicial
    I numero de impares
    P numero de pares
    A distribucion de pares

    Instrucciones : 
    1. Introduce I. 
    2. Introduce la distribucion de pares
    
    :)

"""

print(Wellcome)

if __name__ == "__main__":
    comprobador()

