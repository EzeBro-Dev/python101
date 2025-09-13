# CLASS ACTIVITY
# 1
score = int(input("Enter your score: "))
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    elif score >= 50:
        return "E"
    else:
        return "F"

print(get_grade(score))

# 2

integer = int(input("Enter an integer: "))
def check_number(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"

print(check_number(integer))

# 3
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter an operator (+, -, *, /): ")

def calculate(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"
    
print(calculate(a, b, operator))

# 4

def can_vote(age):
    if age >= 18:
        return "You are eligible to vote."
    else:
        return "You are not eligible to vote."

print(can_vote(int(input("Enter your age: "))))

# 5

def classify_number(n):
    if n % 2 == 0 and n > 0:
        return "Positive even"
    elif n % 2 == 1 and n > 0:
        return "Positive odd"
    elif n < 0:
        return "Negative"
    else:
        return "zero"

print(classify_number(int(input("Enter a number: "))))