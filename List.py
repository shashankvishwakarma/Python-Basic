items = [1, 4, 9, 16, 25]
print('Items... ', items)
print('indexing returns the item... ', items[0])
print('indexing returns the item... ', items[-1])
print('slicing returns a new list... ', items[-3:])
print('slicing returns a new list... ', items[:])

items = items + [36, 49, 65, 81, 100]
print('List concatenation operation... ', items)
items[7] = 64
print('replace the wrong value... ', items)

items[7:-1] = [64, 81, 100, 111, 144]
print('replace the wrong value range ... ', items)

items.append(101);
print('add value at end of list... ', items)
print('built-in function len()... ', len(items))

a = [4, 5, 6, 7, 8]
b = [1, 2, 3, a]
print('nested list... ', b)
print('nested list 1st index... ', b[0])
print('nested list 3rd index... ', b[3])
print('nested list ... ', b[3][2:])
