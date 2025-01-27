# 2) თქვენი სიტყვებით ახსენით რა განსხვავებაა format ფუნქციასა და f სთრინგს შორის, ასევე რა განსხვავებაა append-სა და insert-ს შორის

# f სთრინგი არის მეტად გამარტივებული Format ფუნქციასთან შედარებით, ხოლო apend ავტომატურად ამატებს სიის ბოლოში ახალ ელემენტს და insert - ით ჩვენ უნდა მინუთითოთ მერამდენე ინდექსე დაემატოს ახალი ელემენტი.


# 3) Write a function that takes a user's name and age, and returns a welcome message formatted with an f-string.

def user(name,age):

    print(f"My name is {name}, i am {age} years old.")

user("vato","15")


# 4) Write a function that takes a first name and last name, capitalizes them, and formats them into a single string.

def user(firstname,lastname):

    print(f"My firsname is {firstname.capitalize()} and lastname {lastname.capitalize()}")

user("vato","tsaishvili")


# 5) Create a function that takes a string, reverses it, and formats it within a sentence.

def reverse_sting(string):

    reversed_string = string[::-1]

    print(f"Reversed string is {reversed_string}")

reverse_sting("string")


# 6) Write a function that takes a sentence, a word, and an index, and inserts the word into the sentence at the given index.

def insert_word(sentence, word, index):

    sentence2 = sentence.split()
    sentence2.insert(index,word)
    print(" ".join(sentence2))

insert_word("hello my name is vato","word",0)


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
                                                
    print(sentences)

split_paragraph("hello my name is vato. i am 15 years old")


# ```10) Write a function that takes a list and an item, and appends the item to the list.```

def append_item_to_list(my_list, item):

    my_list.append(item)
    print(my_list)

append_item_to_list([1, 2, 3, 4, 5], "item")


# 11) Create a function that takes a list and a list of items, and appends each item to the original list.

def original_list(list1,list2):

    for i in list2:
        list1.append(i)

    print(list1)

original_list([1, 2, 3, 4, 5],[5, 4, 3, 2, 1])

# 12) Create a function that appends all elements of one list to another list.

def append_elements(list1,list2):

    for i in list2:
        list1.append(i)

    print(list1)

append_elements([1, 2, 3, 4, 5],[5, 4, 3, 2, 1])

# 13) Write a function that takes a list, an index, and an item, and inserts the item at the specified index.

def insert_items(list, index, item):

    list.insert(index,item)
    print(list)

insert_items([1, 2, 3, 4, 5], 2, "item")

# 14) Create a function that inserts an item at the beginning of a list.

def inserts(list,item):
    
    list.insert(0,item)
    print(list)

inserts([1, 2, 3, 4, 5], "item")


# 15) Create a function that inserts an item at the end of a list using the insert method.

def insert_at_the_end(list,item):
    
    list.insert(len(list),item)
    print(list)

insert_at_the_end([1, 2, 3, 4, 5], "item")