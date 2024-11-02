#2) თქვენი სიტყვებით ახსენით რა არის input და output, რამდენი ნაკადი გვაქვს და თითოეულისთვის რა ბრძანებას ვიყენებთ პითონში

#input - არის ის მაგალითად ღილაკზე მაუსის დაჭერა. #name = input("enter your name: ")
#output - ის რაც გამოდის მონიტორზე ღილაკის დაჭერის შემდეგ. 

#4) მომხმარებელს შემოატანინეთ სახელი და გვარი, შეინახეთ ისინი ცვლადებში. შემდეგ დაუბეჭდეთ: "გამარჯობა {სახელი აქ} {გვარი აქ}."

#name = input("enter your name: ")
#surname = input("enter your surname: ")

#print("hello" + " " + (name) + " " + (surname))

#5) შექმენით 5 ცვლადი და მათში შეინახეთ რიცხვები. შემდეგი 6 ოპერატორის გამოყენებით: +, -, *, /, **, %  ჩამოწერეთ მათ შორის მათემატიკური ოპერაციები. ჩამოწერეთ ასეთი 10 მაგალითი.
#მაგალითად: print((num1 + num2) / num3 - num4*num5 + num1**num3 % num2)

num1 = 15
num2 = 2
num3 = 10
num4 = 5
num5 = 20

print((num1 + num2) / num3 - num4*num5 + num1**num3 % num2)
print((num2 + num3) / num5 - num3*num1 + num1**num4 % num5)
print((num3 + num4) / num4 - num1*num5 + num3**num2 % num1)
print((num5 + num2) / num1 - num4*num2 + num4**num3 % num1)
print((num4 + num2) / num3 - num1*num5 + num3**num4 % num2)