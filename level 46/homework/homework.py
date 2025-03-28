# 1) 

n = [x for x in range(1, 11)]

# 2)
#  
s = [x**2 for x in range(1, 6)]

# 3)
#  
e = [x for x in range(1, 21) if x % 2 == 0]

# 4) 
words = ["Vato", "Nika", "Giorgi", "Luka"]
f = [word[0] for word in words]

# 5) 
upper = [word.upper() for word in words]

# 6) 
by_3 = [x for x in range(1, 51) if x % 3 == 0]

# 7) 
l = [word for word in words if len(word) > 4]

# 8)
cel  = [0, 10, 20, 30, 40]
us = [(temp * 9/5) + 32 for temp in cel]

# 9)
p = [i for i in range(2, 101) if all(i % d != 0 for d in range(2, int(i**0.5) + 1))]

# 10) 
s = "hello rati hello rati hello rati"
jigar = s.split()
filtered_words = [i for i in jigar if len(i) > 5 and any(vowel in i.lower() for vowel in "aeiou")]

# 11) 

b = [0, 1]
[b.append(b[-1] + b[-2]) for _ in range(18)]