# 2) თქვენი სიტყვებით ახსენით რა არის elif და რაში ვიყენებთ მას

# elif არის მოცემული პირობის გადამოწმება რამდენიმეჯერ

# 3) Write a program that takes three numbers as input and prints the largest of the three.

num1 = float(input("Enter number: "))
num2 = float(input("Enter number: "))
num3 = float(input("Enter number: "))

if num1 > num2 and num1 > num3:
     print("Biggest number is", num1)
elif num2 > num1 and num2 > num3:
     print("Biggest number is", num2)
elif num3 > num1 and num3 > num2:
     print("Biggest number is", num3)


# 4) Write a program that takes a score (0-100) as input and outputs the grade based on the following rules:

    # 90-100: A
    # 80-89: B
    # 70-79: C
    # 60-69: D
    # Below 60: F

score = int(input("Enter number: "))
if score >= 90: print("A")
elif score >= 80: print("B")
elif score >= 70: print("C")
elif score >= 60: print("D")
else: print("F")


# 5) Write a program that takes a number as input and prints whether it is positive, negative, or zero.

num1 = float(input("Enter number: "))
if num1 > 0: print("Positive")
elif num1 < 0: print("Negative")
else: print("Zero")


# 6) Use a loop to calculate the sum of numbers between two given integers.

num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))
sum = 0

for i in range(num1, num2):
    sum += 1

print(sum)


# 7) Write a program that checks if a single given number is prime number

num1 = int(input("Enter number: "))
is_valid = True

if num1 < 0:
    is_valid = False

for i in range(2, num1):
    if num1 % i == 0:
       is_valid = False

if is_valid == True: print("Number is prime")
else: print("Number is not prime")

# 8) Create a list of five numbers and print the first, third, and last elements using indexing.

list1 = [1, 2, 3, 4, 5]
print(list1[0])
print(list1[2])
print(list1[4])



# 9) Create a list of 20 elements (any data type) and print all of the elements - use indexing

list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,"GOA best", True, False, "Vato", "Data"]

print(list2[0])
print(list2[1])
print(list2[2])
print(list2[3])
print(list2[4])
print(list2[5])
print(list2[7])
print(list2[8])
print(list2[9])
print(list2[10])
print(list2[11])
print(list2[12])
print(list2[13])
print(list2[14])
print(list2[15])
print(list2[16])
print(list2[17])
print(list2[18])
print(list2[19])



