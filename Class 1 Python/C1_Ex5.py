import random

alternative = ["r","p","s"]

pc=random.choice(alternative)
print("Let's play Rock Paper or Scissor!")
choice=input("Make your Choice: ")
if choice==pc:    
    print("both are equal")
if choice=="r" and pc=="s":
    print(f"you win, pc is {pc}")
if choice=="r" and pc=="p":
    print(f"you loose, pc is {pc}")
if choice=="p" and pc=="r":
    print(f"you win, pc is {pc}")
if choice=="p" and pc=="s":
    print(f"you loose, pc is {pc}")
if choice=="s" and pc=="r":
    print(f"you loose, pc is {pc}")
if choice=="s" and pc=="p":
    print(f"you win, pc is {pc}")