# საკლასო დავალება:

# Task: Division Calculator with Error Handling

# Ask the user to input two numbers: a numerator and a denominator.

# Attempt to divide the numerator by the denominator inside a try block.

# If the user inputs something that is not a number, catch the error and display a message using except.

# If the user attempts to divide by zero, raise a ValueError with a custom message.

# Regardless of what happens, use a finally block to print a message like “Operation complete.”


try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    if denominator == 0:
        print("Error: You cannot divide by zero.")
    else:
        result = numerator / denominator
        print("Result:", result)

except ValueError:
    print("Invalid input. Please enter a number.")

finally:
    print("Operation complete.")






def square(x):
    return x * x

def apply_to_list(func, values):
    return [func(value) for value in values]

values = [1, 2, 3, 4, 5]
result = apply_to_list(square, values)
print(result)