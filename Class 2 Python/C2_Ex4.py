# Esto es para abrir un archivo 
# Hay que copiar la dirección que sale en barra de la carpeta
file="c:/Users/sebat/ClassRepository/exercises_class/prueba.txt"
with open(file,"r") as text:
    # Lo que hace esto es imprimir la dirección del text y las instrucciones si es leer o escribir.
    print(text)
    # Imprime lo que dice el archivo en su interior.
    lines=text.read()
    print(lines)
