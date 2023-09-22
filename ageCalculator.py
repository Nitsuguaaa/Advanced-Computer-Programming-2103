from datetime import date
currentYear = date.today().year

birthYear = eval(input("Enter your birth year: "))

print("You are currently", currentYear-birthYear, "years old!")