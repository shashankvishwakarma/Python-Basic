print('============ Number data type =================')
division = 8 / 5  # division always returns a floating point number
print('division always returns a floating point number', division);

division = 17 / 3  # classic division returns a float
print('classic division returns a float... ', division);

division = 17 // 3  # floor division discards the fractional part
print('floor division discards the fractional part... ', division);

division = 17 % 3  # the % operator returns the remainder of the division
print('the % operator returns the remainder of the division... ', division)

print('============ String data type =================')

text = 'spam eggs'  # single quotes
print('single quotes... ', text);

text = 'doesn\'t'  # use \' to escape the single quote...
print('Use of escape the single quote... ', text)

text = '"Yes," they said.'  # ...or use double quotes inside single quote
print('use double quotes inside single quote... ', text)

text = 'First line.\nSecond line.'  # \n means newline
print('newline ... ', text)

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

text = ('Put several strings within parentheses '
        'to have them joined together.')
print('string in several line with parentheses... ', text)

'''

 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1

'''
text = 'Python'
print('character in position 0... ', text[0])
# print('character in position 6... ',text[6])
print('last character ... ', text[-1])
print('second last character... ', text[-6])
print('characters from position 0 (included) to 2 (excluded)... ', text[0:2])
print('characters from position 0 (included) to 2 (excluded last 2 char)... ', text[0:-2])
print('character from the beginning to position 2 (excluded)... ', text[:2])
print('characters from position 4 (included) to the end... ', text[4:])
print('characters from the second-last (included) to the end... ', text[-2:])
