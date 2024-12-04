# 3) თქვენი სიტყვებით ახსენით განსხვავება while და for  ციკლებს შორის

# while ციკლით ჩვენ შეგვიძლია ნებისმიერი ტექსტი დავპრინტოთ უსასრულოდ ,ხოლო for ციკლში კი უნდა შევქმნათ დიაპაზონი, მაგალითად  range(20) ამ შემთხვევაში წინადადება დაიპრინტება 20-ჯერ.


# 4) დაბეჭდეთ "GOA BEST!!!" 50-ჯერ, ორივე ციკლით შეასრულეთ ეს დავალება

for i in range(50):
    print("GOA IS THE BEST")

num = 50
while num > 0:
    print("GOA IS THE BEST")
    num -= 1

# 8) Prompt the user to enter a password. Keep asking until they enter the correct password.

correct_password = "1234"
user_password = input("Enter password: ")

while user_password != correct_password:
    print("Incorrect password")
    user_password = input("Enter password: ")
print("Correct password")

# 9) Create a program that keeps asking for a username and password until both are correct.
correct_username = "Vato"
correct_password = "vato1234"

user_input1 = input("Enter username: ")
user_password = input("Enter password: ")

while (user_input1 != correct_username) or (user_password != correct_password):
    print("Incorrect info")
    user_input1 = input("Enter username: ")
    user_password = input("Enter password: ")
print("Correct username and correct password. logged in")


# 10
user_number = int(input("Enter natural number: "))
factorial, starting_number = 1, 1

while starting_number <= user_number:
    factorial *= starting_number
    starting_number += 1

    print("Starting number:", str(starting_number))
    print("Factorial:", str(factorial))

print("Factorial of", str(user_number), "is:", str(factorial))