print("(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee, " +
        " (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek, " +
        " (9) Tamale, (10) Steak ")
pie_list=["Pecan","Apple Crisp","Bean","Banoffee","Black Bun","Blueberry", "Buko", "Burek","Tamale","Steak"]
shopping="y"
pie_purchase = [0,0,0,0,0,0,0,0,0,0]
while shopping=="y":
    choice= int(input("what do you want? "))
    # hay que sacarle un numero porque parte desde 0
    choice_index= choice-1
    # Lo que hago aca es sumar un pie en el arreglo donde tengo el numero de pie que quiero.   
    pie_purchase[choice_index]+=1
    print("Great! We'll have that " + pie_list[choice_index] + " right out for you.")
    shopping=input("Would you like to buy more?: ")

#con este for busco la posición de cada pie en la lista.
for pie_index in range(len(pie_list)):
    pie_count=str(pie_purchase[pie_index])
    pie_name=str(pie_list[pie_index])
    1
    print(f"{pie_count} {pie_name}")


    

