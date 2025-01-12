# 2) Sum of Two Numbers: Write a function that takes two numbers as input and returns their sum.

def sum_of_two_numbers(num1, num2):
    print("Sum of this numbers:", num1 + num2)

sum_of_two_numbers(20, 10)


# 3) Even or Odd: Create a function that determines whether a given integer is even or odd.

def even_or_odd(num3):
    if num3 % 2 == 0:
        print(num3, "number is even")
    else:
        print(num3, "is odd")

even_or_odd(11)


# 4) Reverse a String: Implement a function that takes a string and returns it reversed.

def string(string):
    print(string[::-1])

string("apple")


# 5) Find Maximum: Create a function that takes a list of numbers and returns the maximum value.

def maximum(numbers):
    max = numbers[0]
    for i in numbers:
        if i > max:
            max = i
    print(max)

result = maximum([2, 10, 15, 7, 4])


# 6) Factorial: Implement a function to calculate the factorial of a given number.

def factorial(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
        
    print(product)

factorial(3)