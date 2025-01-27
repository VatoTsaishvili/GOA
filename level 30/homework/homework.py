# # ```2) Convert a given sentence to uppercase and print the result.```

# word = "Banana"

# print(word.upper())

# 3) Take a user's name input and display it in uppercase letters.

name = input("enter your name: ")

print(name.upper())

# 4) Create a function that converts a list of lowercase strings to uppercase.\

def lower_to_upper(list):

    result = []
    for i in list:
        if i.islower():
            result.append(i.upper())
        else:
            result.append(i)
    
    print(result)

lower_to_upper(["Apple", "mangO", "cocnut"])


# 5) Convert all the characters of a given sentence to lowercase and print it.

word = "AppLE"

print(word.lower())

# 6) Ask the user for their email address and ensure it is stored in lowercase.

email = input("enter your email: ")

print(email.lower())

# 7) Write a function that takes a mixed-case string and returns it in all lowercase letters.

def lowercase(text):

    print(text.lower())

lowercase("apple cat dog BIG MY naME is VatO")


# 8) Capitalize the first letter of a sentence provided by the user.

word = "hello my name is vato"

print(word.capitalize())

# 9) Given a list of lowercase strings, capitalize the first letter of each string.

list1 = ["banana", "apple", "mango"]

for i in range(len(list1)):
    list1[i] = list1[i].capitalize()

print(list1)

# 10) Create a function that takes a string and returns it with the first letter capitalized.

def capitalized(string):

    print(string.capitalize())

capitalized("my name is vato")

# 11) Find the position of the first occurrence of the word "Python" in a sentence.

word = "the best Pyton"

print(word.find("Pyton"))

# 12) Search for a user-specified substring in a provided string and print its starting index.

string = "hello world"
user = input("enter word: ")

print(string.find(user))


# 13) Write a function to find and return the index of a specified character in a given string.

def find_char(string, char):

    print(string.find(char))

find_char("hello", "o")


# 14) Find and print the length of a user-provided string.

user_string = input("enter string: ")

print(len(user_string))


# 15) Write a function that takes a list of strings and returns their lengths.

def list_of_string(list):
    print(len(list))

list_of_string([1, 2, 3, 4 ,5])

# 16) Count the number of times the word "the" appears in a given paragraph.

paragraph = "the the the apple book"

print(paragraph.count("the"))

# 17) Ask the user to input a character and count its occurrences in a given string.

paragraph = "the the the apple book"
user = input("enter char: ")


print(paragraph.count(user))


# 18) Create a function that counts and returns the occurrences of a specified word in a text.

def count(text,word):
    print(text.count(word))

count("hello", "l")

# 19) Find and print the index of the first occurrence of the word "hello" in a given string.

string = "hello my name is vato"

print(string.find("hello"))

# 20) Write a function that returns the index of a character provided by the user in a string.

def index_of_character(string,symbol):

    print(string.find(symbol))

index_of_character("hello", "e")


# 21) Check if all characters in a given string are lowercase and print the result.

string = input("enter string: ")

if string.islower():
    print(string, "is lower")
else:
    print(string, "is upper")


# 22) Create a function that takes a string and returns True if it is completely in lowercase, otherwise False.

def t_or_f(string):
    print(string.islower())

t_or_f("hello")

# 23) Prompt the user to input a string and verify if it contains only lowercase letters.

string = input("enter string: ")

if string.islower():
    print(string, "is lower")
else:
    print(string, "is upper")


# 24) Verify if all the characters in a user-provided string are uppercase.

string = input("enter string: ")

if string.islupper():
    print(string, "is upper")
else:
    print(string, "is lower")

# 25) Write a function that checks if a string consists entirely of uppercase letters and returns a boolean result.\

def check(string):
        print(string.isupper())

check("HELLO")


# 26) Check and display whether a string input by the user is in uppercase.

string = input("enter string: ")

if string.islupper():
    print(string, "is upper")
else:
    print(string, "is lower")


# 27) Replace all occurrences of the word "dog" with "cat" in a given sentence.

word = "i love my dog"

print(word.replace("dog", "cat"))

# 28) Write a function that replaces all spaces in a string with underscores.

def replaces(string):
    print(string.replace(" ", "_"))

replaces("hello world")

# 29) Convert a string such that uppercase letters become lowercase and vice versa, then print the result.

string = input("enter string: ")

if string.isupper():
    print(string.lower())
else:
    print(string.upper())

# 30) Write a function that takes a sentence and returns it with swapped case for each letter.

def swap_cases(string):

    result = ""
    for i in string:
        if i.isupper():
            result += i.lower()
        else:
            result += i.upper()
    print(result)

swap_cases("HeLlO")

        