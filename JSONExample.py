book = {}
book['tom'] = {
    'name': 'tom',
    'address': '1 red street, NY',
    'phone': '74185263'
}

book['bob'] = {
    'name': 'bob',
    'address': '1 green street, NY',
    'phone': '963852741'
}

import json

s = json.dumps(book)
print(s)
with open('book.json', 'w') as file:
    file.write(s)

with open("book.json", "r") as read_file:
    s = read_file.read()

print(s)
json_books = json.loads(s)
print(type(json_books))
print(book['bob'])
print(book['bob']['phone'])

for person in json_books:
    print(json_books[person])

