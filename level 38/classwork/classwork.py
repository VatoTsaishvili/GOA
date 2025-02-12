# საკლასო დავალება:

# შექმენით tuple სადაც შეინახება 10 ელემენტი.

# დაბეჭდეთ თითოუელი ელემენტი, ინდექსების გამოყენებით

tuple1 = (1, 2, 3, 4, 5, 6, "hello", "World", 7, 8)

print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
print(tuple1[3])
print(tuple1[4])
print(tuple1[5])
print(tuple1[6])
print(tuple1[7])
print(tuple1[8])
print(tuple1[9])


for i in range(len(tuple1)):
    print(tuple[i])



# საკლასო დავალება:

# შექმენით ფუნქცია სახელად no_duplicates, რომელსაც გადაეცემა ერთი პარამეტრი - user_list.

# user_list-ის მონაცემთა ტიპია სია, ხოლო თქვენი დავალებაა რომ ფუნქციამ დააბრუნოს ეს სია იმ სახით, რომ მასში დუპლიკატები არ გვქონდეს. 

# ფუნქცია გამოიძახეთ 3-ჯერ, განსხვავებული არგუმენტებით

def no_duplicates(user_list):
    return list(set(user_list))

res1 = no_duplicates([1, 2, 2, 3, 4, 5])
res2 = no_duplicates(['apple', 'banana', 'apple'])
res3 = no_duplicates([True, False, True, "apple", "banana"])

print(res1,res2,res3)
