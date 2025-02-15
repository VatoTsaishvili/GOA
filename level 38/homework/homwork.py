# ```

# 2) Tuple Indexing & Slicing: Create a tuple with at least 5 elements and extract the second, last, and a slice of the middle three elements.

tup1 = (1, 2, 3, 4, 5)
print(tup1[0])
print(tup1[4])
print(tup1[1:4])


# 3) Tuple Immutability: Try to modify an element in a tuple and observe what happens.

tup2 = (1, 2, 3, 4, 5)
# tup2[1] = "t"
# print(tup2)

#  ეს არის error რადგან ტუფლში არ შეიძლება ელემენტის შეცვლა


# 4) Tuple Packing & Unpacking: Create a tuple with multiple values, unpack them into separate variables, and print each variable.

tup3 = (1, 2, 3)

a, b, c = tup3

print(a)
print(b)
print(c)


# 5) Tuple Methods: Use the .count() and .index() methods on a tuple containing repeated elements to count occurrences and find the first occurrence of a specific value.```

tup4 = (1, 2, 3, 2, 4, 2, 5)


count = tup4.count(2)
print(count)

first = tup4.index(2)
print(first)


# 6) Set Creation & Basic Operations: Create a set with at least five elements, add a new element, remove an existing one, and check if a specific value is present in the set.

set1 = {1, 2, 3, 4, 5}

set1.add(6)

set1.remove(3)

# 7) Set Union & Intersection: Create two sets with some common elements and perform union, intersection, and difference operations.

set_a = {1, 2, 3, 4, 5, 6}
set_b = {3, 4, 5, 6, 7, 8}

print(set_a.union(set_b))
print(set_a.intersection(set_b))
print(set_a.intersection(set_b))
print(set_b.difference(set_a))


# 8) Removing Duplicates: Convert a list with duplicate elements into a set to remove duplicates and then convert it back to a list.3

list1 = [1, 2, 2, 3, 4, 4, 5]

set1 = set(list1)

set_list = list(set1)

print(list1)
print(set_list)