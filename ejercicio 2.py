#Utilizando operadores lógicos, determina si una cadena de texto introducida por el usuario tiene 
# una longitud mayor o igual que 3 y a su vez es menor que 10 (es suficiene con mostrar True o False).

cadenaDeTexto = input("Escriba una cadena de texto: ")
if len(cadenaDeTexto) >= 3 and len(cadenaDeTexto)<10:
    print(True)
else:
    print(False)
    
