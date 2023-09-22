from datetime import date


today = date.today()
fName = input("Enter your father's name: ")
fBplace = input("Enter your father's birthplace: ")
fBday = input("Enter your father's birthday(23/12/1984): ")
fBdate = date(int(fBday[6:10]), int(fBday[3:5]), int(fBday[0:2]))
age = today.year - fBdate.year - ((today.month, today.day) < (fBdate.month, fBdate.day))


print("Your father's name is", fName, "from", fBplace, "and is currently", age, "years old")