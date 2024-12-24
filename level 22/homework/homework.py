# 3) შექმენით სია, რომელშიც იქნება 10 ელემენტი. გადაუარეთ სიას ციკლით და დაბეჭდეთ მისი ყველა ელემენტი

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in list1:
    print(i)


# 4) შექმენით სია, რომელშიც იქნება 10 ელემენტი. მომხმარებელს შემოატანინეთ ორი მთელი რიცხვი, num1 და num2.  
#   თუ num1 მეტია num2-ზე, slicing მოახდინეთ სიაზე num1 ინდექსიდან num2 ინდექსამდე და დაბეჭდეთ ახალი სია.
#   თუ num2 მეტია num1-ზე, slicing მოახდინეთ სიაზე num2 ინდექსიდან num1 ინდექსამდე და დაბეჭდეთ ახალი სია.
#   თუ ეს ორი რიცხვი ტოლია, დაბეჭდეთ ცარიელი სია.

num1 = int(input("enter number :"))
num2 = int(input("enter number :"))
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if num1 > num2:
    print(list2[num2:num1])
elif num2 > num1:
    print(list2[num1:num2])
else:
    print([])

# 5) Given a list of numbers, print the first, third, and last elements using indexing.

list3 = [1, 3, 5, 7, 9]

print(list3[0])
print(list3[2])
print(list3[4])

# 6) Given a list of strings, print the list in reverse order using slicing.

strings = ["a", "b", "c", "d", "e"]
#          -5   -4   -3   -2   -1
print(strings[::-1])


# 7) Given a list of words, print every second element starting from the first element. (ერთი ელემენტის გამოტოვებით)

words = ["book", "apple", "bike", "car", "note"]
list5 = words[0::2]
print(list5)


# 8) Given a list of numbers, replace the fourth element with the number 100 and print the modified list.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 , 17, 18, 19, 20]

numbers[3] = 100

print(numbers)

