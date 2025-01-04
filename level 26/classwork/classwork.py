# # შექმენით ფუნქცია სახელად greet, რომელსაც ექნება 1 პარამეტრი. ფუნქციის გამოძახებისას არგუმენტად გადაეცით თქვენი სახელი და ფუნქციამ ასეთი რამ უნდა დაგიბეჭდოთ: "გამარჯობა, {აქ თქვენი სახელი}"
# def great(name):
#         print("hello" + " "+ name)






# # საკლასო დავალება: შექმენით ფუნქცია სახელად manual_range, რომელსაც გადაეცემა სამი პარამეტრი (start, end, step).
# # ფუნქციის დავალებაა რომ გადაცემული პარამეტრებით შეადგინოს დიაპაზონი, შემდეგ ამ დიაპაზონს გადავუაროთ ციკლით და დავბეჭდოთ მხოლოდ ლუწი რიცხვები.
# # ფუნქციის გამოძახებისას მას აუცილებლად უნდა გადაეცეს 3 არგუმენტი.
# # ფუნქცია გამოიძახეთ მინიმუმ 5-ჯერ სხვადასხვა არგუმენტებით


# def manual_range(start, end, step):
#     for i in range(start, end, step):
#         print(i)

# manual_range(2, 10 ,2)
# manual_range(2, 20 ,2)
# manual_range(2, 30 ,2)
# manual_range(2, 40 ,2)
# manual_range(2, 50 ,2)

# def manual_range(start, end, step):
#     for i in range(start, end, step):
#         if i % 2 == 0:
#              print(i)
        
# manual_range(2, 10 ,6)
# manual_range(2, 20 ,2)
# manual_range(2, 30 ,3)
# manual_range(2, 40 ,2)
# manual_range(2, 50 ,9)



# საკლასო დავალება: შექმენით ფუნქცია სახელად manual_len, რომელსაც ექნება გაწერილი 1 პარამეტრი.

# ფუნქციას გადაეცემა სია და მისი დავალებაა რომ დააბრუნოს სიის სიგრძე (len არ გამოიყენოთ). უნდა გამოიყენოთ for ან while ციკლი და ერთი ცვლადი. საბოლოოდ დაბეჭდეთ სიის სიგრძე.

# ფუნქციის გამოძახებისას გადაეცემა მას ერთი არგუმენტი - სია
# list = [1, 2, 3, 4, 5]
# def manual_len(list):
#      for i in range(list):
#           print(i)

# manual_len(list)


def manual_len(list):
    count = 0  
    for i in list:
        count += 1 
        print(i)

my_list = [1, 2, 3, 4, 5]
range = manual_len(my_list) 
print("range", range) 

# def manual_len(input_list):
    # count = 0  # Initialize a variable to keep track of the count
    # for item in input_list:  # Iterate through each item in the list
    #     count += 1  # Increment the count for each item
    # return count  # Return the final count

# Example usage
# my_list = [1, 2, 3, 4, 5]  # Define a list
# length_of_list = manual_len(my_list)  # Call the function with the list
# print("The length of the list is:", length_of_list)