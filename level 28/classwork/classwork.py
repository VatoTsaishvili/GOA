# საკლასო დავალება: შექმენით ფუნქცია სახელად manual_index, რომელსაც ექნება 2 პარამეტრი - მთავარი სთრინგი და საძიებელი სთრინგი.

# თქვენი დავალებაა რომ დააბრუნოთ მთავარ სთრინგში საძიებელი სთრინგი მერამდენე ინდექსზეა

def manual_index(main_str, search_str):
    for i in range(main_str):
        if main_str == search_str:
            print(i)

manual_index("hello")

