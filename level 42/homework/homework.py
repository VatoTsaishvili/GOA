# 2) თქვენი სიტყვებით ახსენით dictionary რითი განსხვავდება აქამდე ნასწავლი კოლექციებისგან, რა არის key, value, key-value pair

# directionary- არის მონაცემთა სტრუქტურა, რომელიც ინახავს წყვილებად შერწყმულ ღირებულებებს ამ წყვილებს ეწოდება key-value pairs (key  და value).

# 3) Create a dictionary with at least five key-value pairs and print all the keys using the keys() method.

dict1 = {
    'name': 'ვატო',
    'age': 15,
    'city': 'ზუგდიდი',
    'profession': 'პროგრამისტი',
    'hobby': 'ფეხბუღთი'
}

print(dict1.keys())


# 4) Create a dictionary and print all the values using the values() method.

print(dict1.values())

# 5) Create a dictionary and print all key-value pairs using the items() method.

print(dict1.items())

# 6) Iterate over a dictionary using the items() method and print each key with its corresponding value.

for key, value in dict1.items():
    print(f"Key: {key}, Value: {value}")

# 7) Create a dictionary and check if a specific key exists using the in operator.


# 8) Retrieve a value from a dictionary using the get() method and handle cases where the key does not exist.


age = dict1.get('age', 'Not Found')
print(age)

not_exist= dict1.get('name', 'Not Found')
print(not_exist) 

# 9) Add a new key-value pair to an existing dictionary and print the updated dictionary.

dict1['age'] = 15
print('This is new key-value and updated dictionary' , dict1)

