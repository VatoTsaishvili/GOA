# 1)

def count_sheeps(sheep):
    return sheep.count(True)


# 2)

def no_space(x):
    return x.replace(" ", "")

# 3)

def double_integer(i):
    return i*2


# 4)

def greet(name):
    return f"Hello, {name} how are you doing today?"

# 5)

def boolean_to_string(b):
    return str(b)


# 6)

def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    else:
        return value1 / value2
    

# 7)

def litres(time):
    return time // 2


# 8)

def century(year): 
    return (year + 99) // 100


# 9)

def digitize(n):
    starting_str = str(n)
    reversed_str = starting_str[::-1]

    res_list = []

    for i in reversed_str:
        res_list.append(int(i))

    return res_list


# 10)

def digitize(n):
    starting_str = str(n)
    reversed_str = starting_str[::-1]

    res_list = []

    for i in reversed_str:
        res_list.append(int(i))

    return res_list

# 11)

def maps(a):
    saver=[]
    for i in a:
        saver.append(i*2)
    return saver

# 12)

def lovefunc( flower1, flower2 ):
    return (flower1 + flower2)%2 == 1