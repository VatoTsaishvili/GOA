# ```3) https://www.codewars.com/kata/55a2d7ebe362935a210000b2```

def find_smallest_int(arr):
    smallest = arr[0]
    
    for num in arr:
        if num < smallest:
            smallest = num

            
    return smallest


# 4) https://www.codewars.com/kata/544675c6f971f7399a000e79

def string_to_number(s):
    return int(s)


# 5) https://www.codewars.com/kata/55d24f55d7dd296eb9000030

def summation(num):
    res = 0
    for i in range(1, num + 1):
        res += i
    return res

