# como abrir un archivo CSV.
#siempre hay que llamar antes a estos dos modulos.
import os
import csv

#con esto, le digo donde esta el archivo.
csvpath = os.path.join("C:/Users/sebat/ClassRepository/exercises_class/Class 2 Python/contacts.csv")

with open(csvpath) as csvfile:
    #esto es para que python sepa que abrir y como viene el archivo.
    csvreader=csv.reader(csvfile, delimiter=",")
    #con esto se imprime 
    print(csvreader)
    for row in csvreader:
        print (row)
