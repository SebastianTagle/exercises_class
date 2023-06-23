print("(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee, " +
        " (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek, " +
        " (9) Tamale, (10) Steak ")
pie_list=["Pecan","Apple Crisp","Bean","Banoffee","Black Bun","Blueberry", "Buko", "Burek","Tamale","Steak"]
shopping="y"
pie_purchase= range(10)
while shopping=="y":
    choice= int(input("what do you want? "))
    choice_index= choice-1
    pie_purchase[choice_index]+=1
    print("Great! We'll have that " + pie_list[choice_index] + " right out for you.")


    

