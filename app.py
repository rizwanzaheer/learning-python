print("hello Rizwan Zaheer")
price = 20
print(price)
price = 10
print(price)

# name = input('What is your name? \n')
#
# print('\n')
# print('Hi ' + name)
#
# birth_year = input('Birth year: ')
# print(type(birth_year))
# age = 2019 - int(birth_year)
#
# print('Your age is: ' + str(age))

email = '''
Hi Rizwan
this is a multiple line string  
'''

email = 'Python course'

print(email[-2])
print(email[:4])
print(email[2:4])
print(email[2:])
print(email[:])
print(email[1:-1])

fname = 'Rizwan'
lname = 'Zaheer'
# formatted string
msg = f'[{fname} {lname}] is a coder'
print(msg)
print(len(msg))

print(fname in msg)

is_hot = False

is_cold = True

if is_hot:
    print("It's a hot day!")
    print("Drink plenty of water!")
elif is_cold:
    print("It's a cold day!")
    print("Wear warm clothes!")
else:
    print("It's a lovely day!")
print("Enjoy your day!")







