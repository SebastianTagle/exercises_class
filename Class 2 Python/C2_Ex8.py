import os
import csv

indexes = [1, 2, 3, 4]
employees = ["Michael", "Dwight", "Meredith", "Kelly"]
department = ["Boss", "Sales", "Sales", "HR"]

#lo que hace la funcion zip es que te junta varios arreglos y los une en uno, poniendo cada arreglo hacia abajo.
router= zip(indexes,employees,department)

#for employee in router:
#    print(employee)

output_path = os.path.join("C:/Users/sebat/ClassRepository/exercises_class/Class 2 Python/test_file2.csv")
with open(output_path,'w',newline='') as csvfile:
    csvwriter=csv.writer(csvfile,delimiter=",")
    csvwriter.writerow(["Indexes","Employees","Department"])
    #cuando quiero escribir un arreglo con datos (filas y columnas), se ocupa writerows y lo que va haciendo es que escribe cada fila en su fila.
    csvwriter.writerows(router)

with open(output_path) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    for row in csvreader:
        print(row)