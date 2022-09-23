# Tema-1
<h1 align="center">	Evaluación tema 1</h1>

<h2>Repositorio:</h2>

Este es el link del [repositorio](https://github.com/crltsnch/Tema-1)

***
<h2>¿De qué trata esta tarea?</h2>
Debíamos resolver varios ejercicios.

```
1)
matriz = [
 [1, 1, 1, 3],
 [2, 2, 2, 7],
 [3, 3, 3, 9],
 [4, 4, 4, 13]
]

matriz[1][-1] = sum(matriz[1][:-1])
matriz[3][-1] = sum(matriz[3][:-1])
print(matriz)


2)
cadenaDeTexto = input("Escriba una cadena de texto: ")
if len(cadenaDeTexto) >= 3 and len(cadenaDeTexto)<10:
    print(True)
else:
    print(False)


3)
print(list(range(0, 11)))
print(list(range(-10, 0)))
print(list(range(0, 21, 2)))
print(list(range(-19, 0, 2)))
print(list(range(0, 51, 5)))


4)
import sys
from pyparsing import col

if len(sys.argv) == 3:
    filas = int(sys.argv[1])
    columnas = int(sys.argv[2])
    if filas<1 or filas>9 or columnas>9:
        print("Error")
    else:
        for i in range(filas):
            print(" ")
            for c in range(columnas):
                print(" * ", end='')
else:
    print("Error")


5)
<img width="1418" alt="Captura de pantalla 2022-09-23 a las 21 58 32" src="https://user-images.githubusercontent.com/91721777/192050028-76e98b5c-8762-47aa-b9ea-06b2d12a6c21.png">

