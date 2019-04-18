import converters
import random
# or
from converters import lbs_to_kg
from utils import find_max

# import package
import ecommerce.shipping
# or
from ecommerce.shipping import calc_shipping
# or
from ecommerce import shipping

from pathlib import Path

path = Path()

for file in path.glob('*.py'):
    print(f"files in path is: {file}")

for i in range(3):
    print(random.randint(10, 20))

members = ["rizwan", "zaheer", "attique"]
print(random.choice(members))

ecommerce.shipping.calc_shipping()
# or
calc_shipping()
# or
shipping.calc_shipping()


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second  # returning touple


dice = Dice()
print(f"roll dice value is: {dice.roll()}")

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

# phone = input("Phone: ")
# digits_mapping = {
#     "1": "One",
#     "2": "Two",
#     "3": "Three "
# }
#
# output = ""
# for ch in phone:
#     output += digits_mapping.get(ch, "!") + " "
#
# print(output)

# functions
def greeting_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}, Welcome on board!")


# end
greeting_user(last_name='Zaheer', first_name='Rizwan')


# using try catch
# try:
#     age = int(input("Age: "))
#     income = 20000
#     risk = income / age
#     print(age)
# except ZeroDivisionError:
#     print("Age can't be zero!")
# except ValueError:
#     print('Invalid value')


# Using Classes

class Point:
    # constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


# point = Point();
#
# point.x = 10
# point.y = 20
# print(point.x)
# print(point.y)
# point.move()

# resolve problem in classes
point = Point(10, 20);

# point.x = 30
# point.y = 40
print(point.x)
print(point.y)
point.move()


# Inheritance
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    pass


class Cat(Mammal):
    pass


dog = Dog()
dog.walk()

lbs_to_kg(300)

numbers = [10, 332, 4, 3435, 4]
print(find_max(numbers))


