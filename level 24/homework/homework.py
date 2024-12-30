from turtle import*

# 2) ახსენით რა არის ფუნქცია და რატომ ჯობია მისი გამოყენება/

# ფუნქცია არის კოდების ერთობლიობა, რომელიც სრულებს რაღაც კონკრეტულ დავალებას, ის კარგი მიდგომაა და ჩვენი კოდი არის უფრო მოკლე.


# 3) slicing და indexing დავალებები:

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get the first element from a list.

print(list[0])

# Get the last element from a list using negative indexing.

print(list[-1])

# Slice the first three elements of a list.

print(list[0:3])

# Extract the last five elements from a string.

word = "airplane"
print(word[3:])

# Reverse a string using slicing.

print(word[::-1])

# Get every third element from a list - ყოველი მესამე ელემენტი სიიდან

print(list[::3])

# Split a list into two halves using slicing. - ორ ნაწილად დაყავით სია (სიის სიგრძე აიღეთ ლუწი)

print(list[0:5])
print(list[5:10])