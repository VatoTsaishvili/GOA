# საკლასო დავალება:

# შექმენით ფუნქცია სახელად generate_big_sentence, რომელსაც გადაეცემა 3 პარამეტრი - name, surname, age.

# ფუნქციამ უნდა გამოგვიტანოს წინადადება ზუსტად იგივე წყობით, როგორც მე დავწერე (გადახედეთ რესურებს), გამოიყენეთ format ფუნქცია.

# სანამ ფუნქციას გამოიძახებთ, მომხმარებელს შემოატანინეთ ტერმინალიდან სახელი, გვარი, ასაკი და შეინახეთ ისინი ცვლადებში.

# ფუნქციის გამოძახებისას, მას არგუმენტებად უნდა გადაეცეს ეს ცვლადები

name = input("enter your name: ")
surname = input("enter your surname: ")
age = input("enter your age: ")

def generate_big_sentence(name, surname, age):
    print(f"Hello, my name is {name}, my surname is {surname}, i am {age} years old.")

generate_big_sentence(name, surname, age)


# საკლასო დავალება:

# შექმენით ფუნქცია სახელად my_split, რომელსაც გადაეცემა ორი პარამეტრი - main_string და string_to_split.

# ფუნქციამ უნდა დაბეჭდოს სია - main_string გაიხლიჩოს string_to_split-ის მიხედვით.

# ფუნქციის გამოძახებამდე მომხარებელს შემოატანინეთ მთავარი და დასაყოფი სთრინგები, შეინახეთ ცვლადებში. შემდეგ გამოიძახეთ ფუნქცია და ეს ცვლადები გადაეცით არგუმენტებად

def my_split(main_string, string_to_split):
    print(main_string.split(string_to_split))

main = input("enter main string")
second = input("enter second string")

my_split(main, second)

# საკლასო დავალება:

# შექმენით ფუნქცია სახელად manual_append. ამ ფუნქციამ სიის ბოლოში უნდა ჩაამატოს ახალი ელემენტი.

# არ გამოიყენოთ append, გამოიყენეთ insert.

# ფუნქციას ექნება 2 პარამეტრი - main_list, item_to_insert.

def manual_append(main_list, item_to_insert):

    list_lenght= len(main_list)
    main_list.insert(list_lenght, item_to_insert)
    print(main_list)

manual_append([1, 2, 3], 5)

