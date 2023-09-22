from statistics import mean
subjects = ["English", "Filipino", "Science", "Math", "Araling Panlipunan", "Physical Education"]
for sub in range(len(subjects)):
    subjects[sub] = eval(input("Enter your grade in " + subjects[sub] + ": "))
print("Your average is:", round(mean(subjects), 2))