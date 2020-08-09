num = input("Enter a number: ")
num = int(num)
if num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

indian = ["samosa", "daal", "naan"]
chinese = ["egg role", "pot sticker", "fried rice"]
italian = ["pizza", "pasta", "risotto"]

dish = input("Enter a dish name: ")

if dish in indian:
    print("Its Indian dish.")
elif dish in chinese:
    print("Its Chinese dish.")
elif dish in italian:
    print("Its Italian dish.")
else:
    print("No Match.")

mark = input("Enter your marks: ")
mark = int(mark)

if mark >= 75 and mark <= 100:
    print('You got Distinction ...')
elif mark >= 60 and mark < 75:
    print('You got First class')
elif mark >= 35 and mark < 60:
    print("You are Just passed")
elif mark >= 0 and mark < 35:
    print('You are failed..')
else:
    print("Please enter valid mark..")

''' For Loop'''

expenses = [2340, 2350, 2500, 2100, 3100, 2980]
total = 0
for item in expenses:
    total = total + item
print("Total expenses is: ", total)

total = 0
for i in range(len(expenses)):
    print('Month:', (i+1), 'Expense:', expenses[i])
    total = total + expenses[i]
print("Total expenses is: ", total)

for i in range(1, 11):
    print(i*i)

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

for w in words[:]:
    print(w, len(w))

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, '\t', a[i])

# pass statement does nothing.. it can be used only when program require statement but does not require any action..
