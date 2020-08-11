x = input("Please enter number 1: ")
y = input("Please enter number 2: ")
try:
    z = int(x) / int(y)
except ZeroDivisionError as e:
    print("Oops!  Division by Zero Exception has occurred.")
    z = None
except Exception as e:
    print("Exception type: ", type(e).__name__)
print("Division is: ", z)

try:
    x = int(input("Please enter a number: "))
except ValueError:
    print("Oops!  That is value error.  Try again...")
except TypeError:
    print("Oops!  That is type error.  Try again...")

finally:
    print('Finally called ...')
