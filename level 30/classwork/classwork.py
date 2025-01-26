# საკლასო დავალება:

# მომხმარებელს შემოატანინეთ სახელი და შეინახეთ name ცვლადში.

# შემდეგ შემოატანინეთ არჩევანი (რომელიც იქნება "u" ან "l") და შეინახეთ ეს ინფორმაცია choice ცვლადში.

# თუ choice ტოლია "u"-სი, მაშინ მომხმარებლის სახელი გამოიტანეთ uppercase-ში.
# თუ choice ტოლია "l"-ის, მაშინ მომხმარებლის სახელი გამოიტანეთ lowercase-ში.
# სხვა შემთხვევაში, დაუბეჭდეთ wrong information.

name = input("enter your name: ")
choose = input("enter word u or l: ")

if choose == "u":
    print(name.upper())
elif choose == "l":
    print(name.lower())
else:  
    print(-1)

# ```შექმენით ფუნქცია, სახელად manual_find, რომელსაც გაწერილი ექნება 2 პარამეტრი: main_string და str_to_find.

# ამ ფუნქციის დავალებაა რომ main_string-ში იპოვოს str_to_find მერამდენე ინდექსზეა.

# თუ მთავარ სთრინგში საძიებელი სთრინგი უბრალოდ არ გვაქვს, დავბეჭდოთ -1```

def manual_find(main_string, str_to_find):

    for i in range(len(main_string)):
        if main_string[i] == str_to_find:
            result = i

    if result == i:
        print("string not found")
    else:
        print(result)

manual_find("hello vato", "h")


# # საკლასო დავალება:

# მომხმარებელს შემოატანინეთ მთავარი სთრინგი და შეინახეთ main_str ცვლადში.

# შემდეგ შემოატანინეთ დასათვლელი სთრინგი და შეინახეთ str_to_count ცვლადში.

# დაბეჭდეთ str_to_count რამდენჯერ შეგხვდება main_str ცვლადში

main_str = input("enter main string: ")
str_to_count = input("enter str to count: ")

print(main_str.count(str_to_count))

# საკლასო დავალება:

# შექმენით ფუნქცია სახელად manual_swapcase

def manual_swapcase(string):

    result = ""
    for char in string:
        if char.isupper():
            result += char.lower()
        elif char.islower():
            result += char.upper()
        else:
            result += char

    print(result)

manual_swapcase("hello, my name is vato")