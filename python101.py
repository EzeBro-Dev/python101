print("Hello, World!")

a = 1
name = "Ezebro"

# Variables
a = 3
a = -3
name = "string"
b = 5.5
is_boy = True
name_of_student = ['ceejay', 'ezebro', 'john']
points = (1, 2, 3, 4)
num = {1, 2, 3, 4}






# Operators


a, b = 3, 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)

x, y = 5, 2
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

a, b = True, False
print(a and b)
print(a or b)
print(not a)
print(not b)

# functions
def name_of_function(parameter):
    print(parameter)
    return parameter


def greet():
    print("Welcome To Python Programming")

greet()


# CLASS ACTIVITY

# PART 1
a, b = 5, 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b)

# 2
area = 3.14 * 7*7
print ("area = ", area)

#  3
profit = 50 - 75
print("profit = ",profit)

profit_per = (50-75) * 100
print("profit_per = ",profit_per)

#  PART 2
# 4
x = 15
y = 25
print(x > y)
print(x == y)
print(y <= x)

# 5
marks = 75
if marks >= 40:
    print("pass")

if marks >= 70:
    print("distinction")


# PART 3
# 6
age = 20
has_id = True
if age >= 18 and has_id:
    print("allowed")
else:
    print("Not allowed")

# 7
num1 = 10
num2 = 50
print(num1 and num2)
print(num1 or num2)
print(not num1)
print(not num2)

# 8
is_raining = False
has_umbrella = False
if is_raining and has_umbrella == True:
    print("Stay Inside")
else:
    print("Go outside")