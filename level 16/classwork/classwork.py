num1 = int(input("enter number: "))
sum = 0
for i in range(num1):
    sum= sum + i 
    print(sum)

my_num = "1234"
user_num = input("Enter your num: ")
counter = 0

while user_num != my_num:
    user_num = int(input("Enter your num: "))
    counter += 1

print("succsesfull")
print("Your guess count:", str(counter))