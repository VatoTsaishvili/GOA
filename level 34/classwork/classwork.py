# საკლასო დავალება:

# შექმენით ფუნქცია რომელიც მიიღებს ორ პარამეტრს - main_list, indexes_list.

# # თქვენი დავალებაა, რომ indexes_list სიაში რა ინდექსებიც იქნება მოცემული, მთავარ სიაში, მაგ ინდექსებზე წაშალოთ ელემენტები

# def list(main_list, indexes_list):
#     for index in indexes_list:
#         if 0 <= index < len(main_list):
#             main_list.pop(index)
    
#         print(main_list)

# list([1, 2, 3], [1])
# [1, 3]


# შექმენით ფუნქცია სახელად remove_one_element, რომელსაც გადაეცემა სია და ინდექსი.

# სიიდან მაგ ინდექსზე მყოფი ელემენტი ამოშალეთ და დაბეჭდეთ სია.

def remove_one_element(list, index):
    list.pop(index)

    print(list)

remove_one_element([1, 2, 3], 1)