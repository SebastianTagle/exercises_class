import os
import csv

csvpath = os.path.join("C:/Users/sebat/ClassRepository/exercises_class/Class 2 Python/comic_books.csv")

#abrir un archivo pero que tiene un codigo distinto (UTF-8) *pregunta como saber cuando los archivos tiene algun encoding especial
#la funcion open por default asume que estas leyendo (read)
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    #hasta esta fila, siempre es lo mismo para abrir un archivo, salvo cuando tengo que agregar si tiene algun codigo en particular.
    book=input("what book are you looking for? ")
    found = False
    #busco en cada fila del texto
    for row in csvreader:
        #si la primera palabra de cada fila es igual al libro que estoy buscando
        if row[0]==book:
            print(f"your book {book} was published in {str(row[9])} by {row[8]} in {row[7]}")
            found =True
    if found ==True:
        print("your book was found")
    if found ==False:
        print("we dont have your book")

        #print(row)