# defining A function
def show_grade(mark, message='Hello'):
    if mark >= 75 and mark <= 100:
        print('You got Distinction ...')
    elif mark >= 60 and mark < 75:
        print('You got First classs')
    elif mark >= 35 and mark < 60:
        print("You are Just passed")
    elif mark >= 0 and mark < 35:
        print('You are failed..')
    else:
        print("Please enter valid mark..")
    return message


def calculate_total(exp):
    total = 0
    for item in exp:
        total = total + item
    return total


def cal_sum(a, b=0):
    print("a :", a)
    print("b: ", b)
    return a + b


tom_exp_list = [2100, 3400, 3500]
joe_exp_list = [200, 500, 700]
toms_total = calculate_total(tom_exp_list)
joes_total = calculate_total(joe_exp_list)

print("Tom's total expense: ", toms_total)
print("Joe's total expense: ", joes_total)

print(show_grade(65))  # with default args
print(show_grade(81, "Hello Joe"))  # with positional arguments
print(show_grade(message="Hello Tom", mark=50))  # with keyword arguments

print("Total is:", cal_sum(5, 6))
print("Total is:", cal_sum(b=5, a=6))
print("Total is:", cal_sum(a=5))
