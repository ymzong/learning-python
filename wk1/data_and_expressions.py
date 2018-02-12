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
print(3 *2)
print(3 * 'abc')
print(3 +2)
print('abc' + 'def')
print(3 + 'def')    # Error
'fewf' + 'efw'

