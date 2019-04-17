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


if is_cold and is_hot:
    print("what the hell!")

if is_cold and not is_hot:
    print("what the hell!")

if is_cold or is_hot:
    print("what the hell is going on!")



# while also have a else block like
# while true:
# .....
# else
# .....

matrix = [
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
]

print(matrix[2][2])

# touple
numbers = (1, 3, 4)
print(numbers[2])


# unpacking with touple
coordinates = (3, 4, 5)
x, y, z = coordinates

print(x, y, z)


# dictionary

customer = {
    "name": "Rizwan",
    "age": 25,
    "is_verified": True
}

print(customer["name"])
print(customer.get('birthdate', "30 - Sep - 1993"))

phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three "
}

output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "

print(output)

# functions
def greeting_user():
    print("Hi there, welcome on board!")


# end
greeting_user()













