# 1. Vocabulary
x = 5                       # x,y,z are parameters
def f(y,z):                 # Function definition
    result = x + y +z       # assign statement
    return result           # return type can be anything

print(f(1,2))               # Function call
print(f(3,4))               # 1,2,3,4 are argument values
# Global varibales-- only referenced inside a function
# Local variables-- assigned a value anywhere within the function's body
# Statement-- used to compute, write a value, or call a procedure
# Expression-- An expression is an instruction that combines values and 
#              operators and always evaluates down to a single value

# 2. Return Statement
def isPositive(x):
    return (x > 0)

print(isPositive(5))
print(isPositive(-5))
print(isPositive(0))

# Return ends the function immediately
def isPositive(x):
    print('Hello!')         # Runs
    return (x > 0)
    print('Goodbye!')       # Doesn't run ("dead code")
    
print(isPositive(5))        # Prints Hello! then True

# No return statement--> return None

# 3. Print vs. Return
# Common mistake at the beginning
def cubed(x):
    print(x ** 3)
#   return None   # When you don't have return statement, python adds it for you
cubed(2)                   # Sort of worked
print(cubed(3))            # Worked but prints None
# print(2 * cubed(4))      # Error!

def cubed(x):
    return (x ** 3)
    
cubed(2)                   # Computed but not printed 
print(cubed(3))            # Works
print(2 * cubed(4))        # Works


# 4. Different Parameter and Return types
def hypotenuse(a,b):
    return ((a ** 2) + (b ** 2)) ** 0.5
    
print(hypotenuse(3,4))      # 5.0 not 5
print("---------------")

def xor(b1,b2):
    return((b1 and (not b2)) or (b2 and (not b1)))  # same as (b1 != b2)
    
print(xor(True, True))      # F
print(xor(True, False))     # T
print(xor(False, True))     # T
print(xor(False, False))    # F
print("---------------")

def isPositive(n):
    return (n > 0)
    
print(isPositive(10))
print(isPositive(-1.234))


# 5. Function Composition
def f(w):
    return 10 * w
    
def g(x,y):
    return f(3 * x) + y

def h(z):
    return f(g(z, f(z+1)))
    
print(h(1))


# 6. Helper functions
def onesDigit(n):
    return n % 10
    
def largerOnesDigit(x,y):
    return max(onesDigit(x),onesDigit(y))
    
print(largerOnesDigit(134,672))     # 4
print(largerOnesDigit(132,674))     # still 4


# 7. Test Functions
# a broken test function
def onesDigit(n):
    return n % 10
    
def testOnesDigit():
    print('Testing onesDigit()...', end='')
    assert(onesDigit(5) == 5)
    assert(onesDigit(123) == 3)
    assert(onesDigit(100) == 0)
    assert(onesDigit(999) == 9)
    print('Passed!')
    
testOnesDigit()         # Passed!--> test function did not work

# A better version
def onesDigit(n):
    return n % 10
    
# def testOnesDigit():
#    print('Testing onesDigit()...', end='')
#    assert(onesDigit(5) == 5)
#    assert(onesDigit(123) == 3)
#    assert(onesDigit(100) == 0)
#    assert(onesDigit(999) == 9)
#    assert(onesDigit(-123) == 3)    # This line added
#    print('Passed!')
    
# testOnesDigit()         # Crashed! worked!


# 8. Local Variable Scope
def f(x):
    print('In f, x =', x)           # In f, x = 4
    x += 5                          # In f, x = 6
    return x                        # 20
    
def g(x):
    return f(x * 2) + f(x * 3)
    
print(g(2))

# Another example
def f(x):
    print('In f, x =', x)           # In f, x = 1
    x += 7                          # In f, x = 10
    return round(x / 3)             # In f, x = 60 
    # round = rounding; int() = the next smallest int
def g(x):
    x *= 10
    return 2 * f(x)

def h(x):
    x += 3
    return f(x+4) + g(x)            
    
print(h(f(1)))                      # 50


# 9. Global Variable Scope
# In general should avoid using global variables.
# Still understand how they work, since others may use them
# There may also be some very few occasions they should be used too!

g = 100

def f(x):
    return x + g

print(f(5)) # 105
print(f(6)) # 106
print(g)    # 100

# Another Example:
g = 100

def f(x):
    # If we modify a global variable, we must declare it as global.
    # Otherwise, Python will assume it is a local variable.
    global g
    g += 1
    return x + g

print(f(5)) # 106
print(f(6)) # 108
print(g)    # 102