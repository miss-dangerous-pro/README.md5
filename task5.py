# Python Data Types
#  Python | Sets 
numbers = [1, 3 , 5 , 7]
first = set(numbers)
second = {2 , 3}
#union 
print(first | second)
#intersection 
print(first & second)
#Difference
print(first - second)
#symmetric differeence 
print(first ^ second)

# Python | Dictionary
employee = {'name': 'vusqa', 'age': 23, 'skills': ['Python', 'Data Analysis']}
print(employee['name'])       # Access and print the name
print(employee['age'])        # Access and print the age
print(employee.get('email'))  # Attempt to access a non-existent key
print(employee['skills'])     # Access and print the skills list

# Python | Arrays
from array import *
numbers = array('d', [10.5, 3.7, 6.2, 1.9, 7.8])
print(numbers)          # Print the array
print(numbers.typecode) # Print the type code of the array
print(numbers.reverse()) 

# Python Variables
# Variables, expression, condition and function
  # Variables
a = 5
b = 10 
print(a,b)
  # Expression
a = 5
b = 10 
print(a*b)
print(a/b)
print(a+b)
print(a-b)

 # Condition
b = 7
if b % 2 == 0:
    print("b is even")
elif b % 2 != 0:
    print("b is odd")
    #function 
    def check_odd_or_even(b):
       if b % 2 == 0:
        print("b is even")
       elif b % 2 != 0:
        print("b is odd")

check_odd_or_even(7)

# Maximum possible value of an integer in python?
x = 10000000000000000000000000000000000000000000
x = x + 1
print(x)

# Global and local variables in python
  #Global example
x = 10

def display_message(message):
    y = 20
    print(x, y)
    print(message, "is a great day")

display_message("Today")
 # local exampla
def display_message(message):
    x = 10  # Local variable
    y = 20  # Local variable
    print(x, y)
    print(message, "is a great day")

display_message("Today")
# Packing and unpacking arguments in python
# Packing
fruits = ['Apple', 'Banana', 'Cherry']
print(fruits)

# Unpacking
fruit1, fruit2, fruit3 = fruits
print(fruit1)
print(fruit2)
print(fruit3)

# Type conversion in python
value = input("Enter the value :")
print(value)
print(type(value))

  #convert value to int
n1 = int(value)
print(n1)
print(type(n1))

  #convert value to float
f1 = float(value)
print(f1)
print(type(f1))

  #convert value to str
value = input("Enter your name:")
print(value)
list1 = list(value)
print(list1)
print(type(list1))

#Byte object Vs  string object
# Byte object
b = b'Python is powerful!'
print(type(b))            
# String object
a = 'Python is powerful!'  
print(type(a)) 

#Print single and Multiple variable
 # Print single variable
city = 'Paris'
temperature = '20°C'
items = 'Bread : 2', 'Milk : 1', 'Eggs : 12'

print('The city is', city)
print('The current temperature is', temperature)
print('The shopping list contains', items)

# Print multiple variables
x = 5
y = 10
z = 15
print(x, y, z)

total = x + y + z
print('The total is', total)           

# Swap variable
x = 10
y = 25
x, y = y, x
print(x)
print(y)

# Private variables name(A special variable) in python 
def multiply():
    print("Multiplication function executed.")

def divide():
    print("Division function executed.")

def main():
    print("Executing math operations")
    multiply()
    divide()

# Special variable `__name__`
if __name__ == "__main__":
    main()
