import os
import csv
#con esto le digo donde quiero que se guarde y como quiero que se llame
output_path = os.path.join("C:/Users/sebat/ClassRepository/exercises_class/Class 2 Python/test_file.csv")

#le digo que abra el archivo en el cual vamos a escribir, por eso va con "w". *pregunta que significa newline
with open(output_path,'w',newline='') as csvfile:
    csvwriter=csv.writer(csvfile,delimiter=",")
    #asume que siempre parte en la primera fila y va bajando.
    csvwriter.writerow(["Name","Age","number"])
    csvwriter.writerow(["Sebastian","35","358-508-9965"])
    csvwriter.writerow(["Paula","35","358-529-3199"])
    csvwriter.writerow(["Blanca","7","n/a"])
    csvwriter.writerow(["Sara","3","n/a"])

#con esto, lo que hago es que me muestre que es lo que esta escribiendo en el archivo que cree anteriormente.
with open(output_path) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    for row in csvreader:
        print(row)
    