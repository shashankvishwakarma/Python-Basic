fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

print('Apple count ', fruits.count('apple'));

print('Banana Index ', fruits.index('banana'));
print('Banana index starting at index 4 is ', fruits.index('banana', 4))  # Find next banana starting a position 4

fruits.reverse()
print('In reverse order ', fruits)

fruits.append('grape')
print('Fruits after append method', fruits)

fruits.sort()
print('Sorted Fruits', fruits)

fruits.pop();
print('Fruits after pop', fruits)

# del statement

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print('del to delete index 0', a)

del a[2:4]
print('del to delete index range 2:4', a)

del a[:]
print('del to delete all with range', a)

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a  # del can also be used to delete entire variables
# print('del to delete list',a) # will throw error as it will defined variable itself - NameError: name 'b' is not defined

'''
Set -
Python also includes a data type for sets. A set is an unordered collection with no duplicate elements. 
Basic uses include membership testing and eliminating duplicate entries. 
Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.
Curly braces or the set() function can be used to create sets. Note: to create an empty set you have to use set(), not {}; 
'''

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print('set', basket)  # show that duplicates have been removed

print('is Orange in basket', 'orange' in basket)
print('is crabgrass in basket', 'crabgrass' in basket)

'''
Dictionaries - 
this is similar to map in java - A data structure with key / value pair
'''

tel = {'jack': 4098, 'sape': 4139}
print('Dictionaries', tel)

tel['guido'] = 4127
tel['sape'] = 4100
print('Dictionaries with modified value against key', tel)
print('Dictionaries value for jack', tel['jack'])

del tel['sape']
print('Dictionaries after del key for sape', tel)

print('Dictionaries to list, prints keys', list(tel))
sorted(tel)
print('Dictionaries sorted', tel)

print('Dictionaries is Guido in tel-', 'guido' in tel)

knights = {'Galahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, '\t', v)
