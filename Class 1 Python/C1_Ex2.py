name=input("what is your name? ")
place=input("where you live? ")
age= int(input("how old are you? "))
Salary_hour=int(input("how much you win per hour? "))
status=input("are you satisfied with your current salary? ")

Salary_day= Salary_hour*8

print(f"Hello! {name}")
print(f"You live in {place}")
print(f"you are {age} years old")
print(f"your salary per day is {str(Salary_day)} dolars")
print(f"Are you satisfied with your current salary: {str(status)}")
