def helloWorld():
    print("Hello World!")

helloWorld()


print('carpe')

print('diem')

print('carpe ', end='') # need to add space if desired
print('diem')   # same line, easy insertion w/ space for eg. if loop


print('carpe', 'diem')  # sameline print, separated with space

print()                 # blank line

# compute the hypotenuse of a right triangle
a = 3
b = 4
c = ((a**2) + (b**2))**0.5
print('side a =', a)
print('side b =', b)
print('hypotenuse c =', c)

#Basic console Input#
#Input a string
name = input('Enter your name: ')
print('Your name is:', name)

# Input a name
# Following gives an error
# x = input ('Enter a number: ')
# print('One hald of', x, '=', x/2)

# CORRECT -->Input a number w/ int()
x = int(input('Enter a number: '))
print('One half of', x, '=', x/2)


# Importing modules #
# Call w/o importing
# print(math.factorial(20)) # NameError

# Call with importing
import math 
print(math.factorial(20))

# List all the functions in the math module
import math
print(dir(math))

# Read online docs
import webbrowser
input('Hit enter to see the online docs for the math module.')
webbrowser.open('http://docs.python.org/3/library/math.html')
