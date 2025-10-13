attendance = float(input("Enter your attendance percentage: "))

if attendance >= 75:
    print("You are eligible to write the exam.")
elif attendance < 75:
    print("You are NOT eligible to write the exam.")
elif attendance > 100:
    print("Enter your attendance between a number from 1 to 100 only.")
else:
    print("Enter your attendance please.")
