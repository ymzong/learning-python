# 1. Some Builtin Types:
import math     # No () should be used
def f():
    print('This is a user defined function')
    return 'hello'  # can be number, no () needed
    
a = f()
print(a)

print('some basic types in Python')
print(type(2))       # int
print(type(2.2))     # float
print(type('2.2'))   # str
print(type(2 < 2.2)) # Boolean (true or false)
print(type(math))    # module
print(type(math.tan))# built in function or method
print(type(f))       # user defined function
print(type(type(42)))# type

print('Some other types further down the road')
print(type(Exception()))    # Exception
print(type(range(5)))       # RANGE*
print(type([1,2,3]))        # list
print(type((1,2,3)))        # TUPLE*
print(type({1,2}))          # SET*
print(type({1:42}))         # Dict
print(type(2+3j))           # Complex number

#example for how dict works
airport_name = {
    'SFO': 'San Francisco Intl Airport',
    'PEK': 'Beijing Intl Airport'
}
print(airport_name['SFO'])


# 2. Some Builtin Cosntants
print('Some builtin constants')
print(True)
print(False)
print(None)

print('Add some more constants in the math module')
import math
print(math.pi)
print(math.e)


# 3. Some Builtin Functions
print('Type conversion function')
print(bool(0))      # 0 & '' & () & [] falsey
print(float(24))    
print(int(2.8))

print('Add some basic math functions')
print(abs(-5))
print(max(2,3))
print(min(2,3))
print(pow(2,3))
print(round(2.345,1))   # Round with the given number of digits
 

# 4. Some Builtin Operators
print(-7 // 4)    # // truncating to the next smallest int
print(5 % 9)      # modulus
print(1 == 2)     # diffent from =
print(1 != 2)     # not equal
x = 2
x += 1            # x = x + 1
print(x)
x %= 10           # x = x % 10
print(x)


# 5. Types Affect Semantics
print(3 * 2)
print(3 * 'abc')
print(3 + 2)
print('abc' + 'def')
# print(3 + 'def')    # Error, cannot combine number with str


# 6. Integer Division
print("The / operator does 'normal' float division:")   # use "" when '' inside
print('5 / 3 =', (5 / 3))

print('The // operator does integer division')
print('5 // 3 =', (5 // 3))
print('-4 // 3 =', (-4 // 3))


# 7.The Modulus or Remainder Operator (%)
print('-4 % 3 =', (-4 % 3))     # cannot do division by 0
# Verify that (a % b) is the same as (a - (a // b) * b):
def mod(a,b):
    return a - (a // b) * b
print(41 % 14, mod(41,14))
print(-32 % 9, mod(-32,9))  # 4
print(32 % -9, mod(32,-9))  # -4

# 8. Operator Order (Precedence and Associativity)
print('Precedence')
print(2 + 3 * 4)
print(5 + 4 % 3)        # % has higher precedence as *,/, and //
print(2**3*4)           # ** has higher precedence than *,/,//,and %

print('Associativity')
print(5 - 4 -3)         # Associate left to right
print(4 ** 3 ** 2)      # Associates right to the left


# 9. Approximate Values of Floating-Point Numbers
print(0.1 + 0.1 == 0.2)
print(0.1 + 0.1 + 0.1 == 0.3)   # False!!
print(0.1 + 0.1 + 0.1)          # 0.30000000000000004
print((0.1 + 0.1 + 0.1) - 0.3)  # 5.551115123125783e-17

#Equality Testing with almostEqual 
print('The Problem')
d1 = 0.1 + 0.1 + 0.1
d2 = 0.3
print(d1 == d2)                 # False! Never use  == for floats

print('The Solution')
epsilon = 10 ** -10
print(abs(d2 - d1) < epsilon)   # True!

print('Once again, using a useful helper function, almostEqual:')
def almostEqual(d1,d2):
    epsilon = 10 ** -10
    return(abs(d2 -d1) < epsilon)

d1 = 0.1 + 0.1 + 0.1
d2 = 0.3
print(d1 == d2)
print(almostEqual(d1,d2))       # True, and now in a resusable function


# 10. Short-Circuit Evaluation 
def yes():
    return True
def no():
    return False
def crash():
    return 1 / 0 #crashes

print(no() and crash())       # Worked, False!
# print(crash() and no())     # Crashed
# print(yes() and crash())    # Never runs

# Once again use the 'or' operator
print(yes() or crash())     # Worked, True!
# print(crash() or yes())     # Crashed
# print(no() or crash())      # Never runs

def isPositive(n):
    result = (n > 0)
    print("isPositive(",n,") =", result)    # Use "" not ''
    return result
def isEven(n):
    result = (n % 2 == 0)
    print("isEven(",n,") =", result)
    return result
    
print('Test 1: isEven(-4) and isPositive(-4))')
print(isEven(-4) and isPositive(-4))
print('------------------')
print('Test 2: isEven(-3) and isPositive(-3)')
print(isEven(-3) and isPositive(-3))