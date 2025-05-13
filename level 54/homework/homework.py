# 3


my_dict = {1 : "c", 7 : "l", 9 : "o"}
key = input("enter key")
try:
    print("value", my_dict[key])
except KeyError:
    print("wrong key")


# 4

try:
    input_one = input("write number:")
    number = int(input_one)
    print("value",number)
except ValueError:
    print("wrong it has to be an integer")



# 5

def greet_him():
    print("hi")

def greet(func):
    print("hi there how are you")
    func()
greet(greet_him)