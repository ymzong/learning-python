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
