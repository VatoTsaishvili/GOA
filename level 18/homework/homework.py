# 3) მომხმარებელს შემოატანინეთ 2 რიცხვი და დაბეჭდეთ მათ შორის უდიდესი.

num1 = int(input("enter number: "))
num2 = int(input("enter number: "))
if num1 > num2:
    num1 += 0
    print(num1)
else:
    num2 += 0
    print(num2)


# 4) Write a program that checks if a given number is even or odd.

num3 = int(input("Enter number: "))
if num3 %2 == 0:
    print(str(num1), "is even")
else:
    print(str(num1), "is odd")


# 5) Write a program to check if a number is positive or negative.

num4 = int(input("Enter number: "))
if num4 > 0:
    print(str(num4), "is positive")
else:
    print(str(num4), "is negative")


# 6) Write a program to check if a number is divisible by 5 - პროგრამა რომელიც ამოწმებს რიცხვი 5-ზე უნაშთოდ იყოფა თუ არა

num5 = int(input("Enter number: "))
if num5 % 5:
    print(str(num5), "isn't diviseble by 5")
else:
    print(str(num5), "is diviseble by 5")


# 7) Ask the user to enter a number multiple times and check if it's even or odd. Stop after 5 numbers.

for i in range(5):
    num6 = int(input("enter number: "))
    if num6 %2 == 0:
        print(str(num6), "is even")
    else:
        print(str(num6), "is odd")


# 8) Create a while loop that asks the user to enter a password. Keep asking until they enter the correct password "Goa best". Also print the count of incorrect passwords.

correct_password = "Goa best"
user_password = input("Enter password: ")
count = 0

while user_password != correct_password:
    print("Incorrect password")
    count += 1
    user_password = input("Enter password: ")
print("Correct password")
print(str(count), "st try")


# 9) Write a program that takes two numbers and an operator (+, -, *, /) as input and performs the calculation. Display the result and end the program.

num1 = int(input("enter number: "))
num2 = int(input("enter number: "))
operator = input("enter operator: ")

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)