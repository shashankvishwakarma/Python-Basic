basket = {"orange", "apple", "mango", "apple", "orange"}
print(type(basket))
print(basket)

a = set()
a.add(1)
a.add(2)
print(a)

a = {}
print(type(a))

a = {"something"}
print(type(a))

number = [1, 2, 3, 4, 3, 2, 7]
unique_number = set(number)
print(unique_number)
unique_number.add(5)
print(unique_number)

fs = frozenset(number)
print(fs)

for i in unique_number:
    print(i)

x = {"b", "c", "a"}
y = {"a", "g", "h"}
print(x | y)  # union
print(x & y)  # intersection
print(x - y)  # minus
print(x < y)  # subset
