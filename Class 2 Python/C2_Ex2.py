candy_list = [
    "Snickers",
    "Kit Kat",
    "Sour Patch Kids",
    "Juicy Fruit",
    "Swedish Fish",
    "Skittles",
    "Hershey Bar",
    "Starbursts",
    "M&Ms"
]
allowance=5
candy_cart= []

#reconoce cada dulce en la lista
for candy in candy_list:
    #print(candy)
    # el primer corchete, entrega el numero en que se encuentra posicionado el argumento el arreglo
    # el segundo corchete, entrega el dulce
    # el .index, entrega la posicion dentro del arreglo
    print(f"{str(candy_list.index(candy))} {candy}")

print("which candy would you like to bring home? ")
for x in range(allowance):
    selected=int(input("input the number of the candy that you want"))
    candy_cart.append(candy_list[selected])
    op=input("do you want more")
    if op =="n":
        break

print("I brought home with me...")
for x in candy_cart:
    print(x)