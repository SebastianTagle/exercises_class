import os
import csv

csvpath = os.path.join("C:/Users/sebat/ClassRepository/exercises_class/Class 2 Python/census_starter.csv")
outputpath = os.path.join("C:/Users/sebat/ClassRepository/exercises_class/Class 2 Python/test_file3.csv")

#para ir guardando la información del csv, tengo que ir guardandola en los distintos arreglos.
Place=[]
Population=[]
Per_Capita_Income =[]
Poverty_Count=[]
Poverty_rate=[]
County=[]
State=[]

first_line=["Place","Population","Per Capita Income","Poverty Count","Poverty Rate","County","State"]

#con esto voy juntando la data en los distintos grupos
data=zip(Place,Population,Per_Capita_Income,Poverty_Count,Poverty_rate,County,State)

#preguntar el lunes como sabemos el orden de las cosas en el archivo.
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    
    #siempre que se hace esto, la función sabe que en una fila hay varios datos, separados por comas.
    for row in csvreader:
        #print(row)
        
        # al decir esto, lo que hago es que en el arreglo Place, se vaya guardando la info que se encuentra en la primera columna del archivo.
        Place.append(row[0])
        Population.append(row[1])
        Per_Capita_Income.append(row[4])
        Poverty_Count.append(row[8])
        
        #esta funcion es para redondear, entonces, primero se indica el numero que se quiere redondear y despues el numero de decimales.
        Prate=round(int(row[8])/int(row[1])*100,2)
        Poverty_rate.append(str(Prate)+"%")
        
        #con esto, separo las celdas que tiene mas de una info (el county y el estado juntos, separados por una coma)
        split_place=row[0].split(",")
        County.append(split_place[0])
        State.append(split_place[1])

with open(outputpath,'w',newline='') as csvfile:
    csvwriter=csv.writer(csvfile,delimiter=",")
    csvwriter.writerow(first_line)
    csvwriter.writerows(data)






