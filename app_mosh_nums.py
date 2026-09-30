# Types of numberrs: inteers, floats, complex number (a + bi)

## Operations

print(2 + 3)
print(2 - 3)
print(2 * 3)
print(2 / 3)
print(2 // 3) # to get integers
print(2**3) # to get power
print(2 % 3) # to get remainder

## some in-built functions
print(round(3.5))
print(abs(-2.6))
 
## math module functions  --- wiillcheck out python 3 math modules for more stuff
import math

print(math.ceil(3.6)) # to round up
print(math.floor(3.6)) # to round down
print(math.sqrt(64)) # to get square root

## random module functions
import random

print(random.randint(0, 100))

## type conversion
x = input("Enter a number: ")  # -- this gives a string
y = int(x) + 1    ## converting the string to an integer

## more on type casting

# x = 5
# y = str(x)  # to strin

# x ='5'
# y = int(x)
# y = float(x)
# y = complex(x)  
# y = bool(x)   # 

print(f" y: {y} , x: {int(x)}")   # concantinating str and numbers

 
