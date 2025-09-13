x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")

score = 85
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
elif score >= 50:
    print("Grade E")
elif score >= 40:
    print("Grade F")

age = int(input("Enter your age: "))
if age >= 18:
    if age < 21:
        print("you can enter but cannot drink alcohol")
    else:
        print("you can enter and drink alcohol")
else:
    print("you cannot enter")