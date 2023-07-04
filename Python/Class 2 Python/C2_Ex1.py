import random

x=random.choice(range(10))

print("Hello! User")
name=input("What is your name? ")
print(f"Hi {name}!")
number=int(input("What is your favorate number? "))
if number < x:
    print(f"you number is lower {x}")
if number>x:
    print(f"your number is higher than {x}")
if number==x:
    print(f"your number is equal to {x}")
