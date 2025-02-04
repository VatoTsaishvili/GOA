# 2) Function Basics: Write a function that takes no arguments and simply prints "Hello, World!"

def simply_print():
    print("Hello, World!")

simply_print()


# 3) Arguments and Parameters: Write a function that takes two numbers as arguments and prints their sum.

def sum(num1,num2):
    result = num1 + num2
    print("The sum of this number is", result)

sum(4, 5)


# 4) Return Statement: Create a function that takes a number as input, multiplies it by 10, and returns the result.


def multiply(num1):

    result = num1 * 10
    return result

num2 = multiply(5)
print(num2)


# 5) Default Arguments: Define a function that takes a name as input and prints a greeting. If no name is provided, it should use "Guest" as the default.

def greeting(name="Guest"):
    print(name)

greeting()


# 6) Boss level: Nested Functions: Define a function that contains another function inside it and calls the inner function.

def fun1():
    def fun2(a, b):
        print(a + b)

    fun2(2, 3)
fun1()


# 7) Write a function that takes a list of numbers and checks whether each number is even or odd using a loop and conditional statements. Print "Even" for even numbers and "Odd" for odd numbers.

def even_or_odd(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(f"{num} is Even")
        else:
            print(f"{num} is Odd")

even_or_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


# 8) Find the Maximum
# Create a function that takes a list of numbers and uses a loop to find and return the maximum number.

def find_maximum(numbers):

    max_number = numbers[0]

    for number in numbers:
        if number > max_number:
            max_number = number

    return max_number

number_list = [32, 5, 10, 2, 27, 17]
max_value = find_maximum(number_list)
print("The maximum number is:", max_value)


# 9) Define a function that takes a list of integers and returns a new list containing only the positive numbers. Use a loop and a conditional statement.

def fillter_positives(lst):
    list1 = []
    for i in lst:
        if i > 0:
            list1.append(i)

    return list1

print(fillter_positives([1, 2, -3, 4, -5]))


# 10) Write a function that iterates through a range of numbers (e.g., 1 to 100) and sums up all the numbers divisible by 3. Return the total sum.

def sum_of_numbers(num1, num2):
    restult = 0
    for i in range(num1, num2):
        if i % 3 == 0:
            restult += i

    return restult

print(sum_of_numbers(1, 7))