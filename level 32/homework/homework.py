# 2) თქვენი სიტყვებით ახსენით რა განსხვავებაა format ფუნქციასა და f სთრინგს შორის, ასევე რა განსხვავებაა append-სა და insert-ს შორის

# f სთრინგი არის მეტად გამარტივებული Format ფუნქციასთან შედარებით, ხოლო apend ავტომატურად ამატებს სიის ბოლოში ახალ ელემენტს და insert - ით ჩვენ უნდა მინუთითოთ მერამდენე ინდექსე დაემატოს ახალი ელემენტი.


# 3) Write a function that takes a user's name and age, and returns a welcome message formatted with an f-string.

def user(name,age):

    name = input("enter your name: ")
    age = input("enter your age: ")

    print(f"My name is {name}, i am {age} years old.")

user("name","age")


# 4) Write a function that takes a first name and last name, capitalizes them, and formats them into a single string.

def user(firstname,lastname):


    firstname = input("enter your firstname: ")
    lastname = input("enter your lastname: ")

    print(f"My firsname is {firstname.capitalize()} and lastname {lastname.capitalize()}")

user("firstname","lastname")


# 5) Create a function that takes a string, reverses it, and formats it within a sentence.

def reverse_sting(string):

    string = input("enter string: ")
    reversed_string = string[::-1]

    print(f"Reversed string is {reversed_string}")

reverse_sting("string")


# 6) Write a function that takes a sentence, a word, and an index, and inserts the word into the sentence at the given index.

# def insert_word(sentence, word, index):

#     sentence = input("enter sentence: ")
#     word = input("enter word: ")
#     index = input("enter index: ")



# insert_word("sentence","word","index")


# 7) Write a function that takes a sentence and returns a list of words.

def sentence(sentence):

    words = sentence.split()
    print(words)

sentence("hallo world, my name is vato")


# 8) Create a function that takes a string of comma-separated values (CSV) and returns a list of individual items.

def csv_list(csv_string):

    item = csv_string.split(',')
    item = [item.strip() for item in item]
    
    print(item)

csv_list("apple, banana, mango, coconut") 


# 9) Write a function that takes a paragraph and splits it into sentences based on periods.

def split_paragraph(paragraph):

    sentences = paragraph.split('.')
                                                # ?
    print(sentences)

split_paragraph("hello")


# ```10) Write a function that takes a list and an item, and appends the item to the list.```

# def append_item_to_list(my_list, item):

#     my_list = input("enter list: ")
#     item = input("enter append itme: ")

#     my_list.append(item)
#     print(my_list)

# append_item_to_list("my_list", "item")