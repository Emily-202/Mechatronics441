## Go to **go.umd.edu/441** for detailed coding review


## LIBRARIES --------------------------------------------------------
import math
from email.mime import base
from torch import imag, long, real
import time


## NUMBERS ----------------------------------------------------------
size = 40       # integer (32 bit)
f1 = 5.6        # float (53 bit)
z = 3+1j        # complex

# Imaginary Functions
abs(z), z.real, z.imag

# Strings
'hello world', "bye world", 'it\'s hot', "that's nice"


## TYPE CONVERSIONS -------------------------------------------------
x = 5.6
s = 'hello world'

# Convert x to an integer:
int(x)

# Convert string s, written in given base, to an integer:
int(s, base) # try: int('101',2) or int('A',16)

# Convert x to a long integer:
long(x)

# Convert x to a floating-point value:
float(x)

# Create a complex number from real & imaginary parts:
complex(real, imag)

# Convert x to a string:
str(x)


## COMMENTS --------------------------------------------------------
# this is a single-line comment

"""
This is a multi-line
comment (placed
between triple full quotes)
"""


## ARITHMETIC OPERATORS --------------------------------------------
# Addition
5 + 2

# Subtraction
5 - 2

# Multiplication
5 * 2

# Division
5 / 2       # classic division (always returns a float)
5 // 2      # floor division (returns an integer)
5 % 2       # modulus (returns the remainder)

# Exponentiation
5 ** 2      # (returns 25)
math.pow(5,2) # (returns 25.0)

# Square Root
math.sqrt(25) # (returns 5.0)

# Order of Operations
5 + 2 * 3   # (returns 11)
(5 + 2) * 3 # (returns 21)


## COMPARISON OPERATORS ---------------------------------------------
5 == 2      # equal
5 != 2      # not equal
5 > 2       # greater than
5 < 2       # less than
5 >= 2      # greater than or equal to
5 <= 2      # less than or equal to
5 is 2      # identity
5 is not 2  # not identity


## ASSIGNMENT OPERATORS ---------------------------------------------
x = 5       # assign 5 to x
x += 2      # equivalent to: x = x + 2
x -= 2      # equivalent to: x = x - 2
x *= 2      # equivalent to: x = x * 2
x /= 2      # equivalent to: x = x / 2
x //= 2     # equivalent to: x = x // 2
x %= 2      # equivalent to: x = x % 2
x **= 2     # equivalent to: x = x ** 2


## STRING OPERATORS ------------------------------------------------
# Strings are "Immutable" (cannot be changed after creation)
# Concatenation
'hello' + ' ' + 'world'  # (returns 'hello world')

# Repetition
'hello' * 3                # (returns 'hellohellohello')

# Membership
'hello' in 'hello world'   # (returns True)
'bye' not in 'hello world' # (returns True)

# Indexing (starts at 0)
s = 'hello world'
s[0]    # (returns 'h')
s[4]    # (returns 'o')
s[-1]   # (returns 'd')

# Slicing
s[0:5]      # (returns 'hello')
s[6:11]     # (returns 'world')
s[:5]       # (returns 'hello')
s[6:]       # (returns 'world')
s[:]        # (returns 'hello world')
s[0:11:2]   # (returns 'hlowrd')
s[::2]      # (returns 'hlowrd')
s[::-1]     # (returns 'dlrow olleh')
s[5::-1]    # (returns 'olleh')
s[10:5:-1]  # (returns 'dlrow')


## STRING METHODS --------------------------------------------------
s = '  hello world  '
s.lower()
s.upper()
s.capitalize()
s.strip()
s.isalpha()
s.isdigit()
s.isspace()
s.startswith(s)
s.endswith(s)
s.count(s)
s.find(s)       # find first occurrence
s.rfind(s)      # find last occurrence
s.replace(s, s)
s.split(s)
s.join(s)

## STRING FORMATTING -----------------------------------------------
x = 2.5
y = 'half of'
z = 5

s = str(x) + ' is ' + y + ' ' + str(z)
s = '%2.1f is %s %d' % (x,y,z) # prints 
s = '{:2.1f} is {:s} {:d}'.format(x,y,z)

# f (float)
# s (string)
# d (integer)
# b (binary)
# e (exponent)
# x/X (hexadecimal) [lower/upper case]


## PRINTING --------------------------------------------------------
print(str(x) + ' is ' + y + ' ' + str(z))
    # no control over formatting

# Format Printing
print('{:2.1f} is {:s} {:d}'.format(x,y,z))
    # more formatting options than C-style format control
    # can simplify to print('{:2.1f} is {} {}'.format(x,y,z) since the string and integer values have fixed formats
    # can use leading numbers to specify argument order:
print('{2:2.1f} is {1:s} {0:d}'.format(z,y,x))

# Syntax
# f'text{expression}'
f'5 modulo 3 = {5%3}'
x = 2
y = 5
f'x + y = {x+y}'
x = 2.5
t = 12
f'{x} * cos({t}) = {x*math.cos(t)}'

f'5 / 3 = {10/3:5.3f}'   # 5 characters wide, 3 after decimal


## FLOW CONTROL ---------------------------------------------------
# Syntax (IF)
x = float(input("Enter a number greater than 5:"))
if x <= 5:
    print(f"{x:4.2f} is too small.")
    print("Maybe pay more attention next time?")
if x > 5:
    print(f"Your number is {x:4.2f}.")

# IF / ELSEIF / ELSE
x = int(input("Enter #:"))
if x < 0:
    x = 0
    print("Negative value entered, changed to zero")
elif x == 0:
    print("Zero")
elif x == 1:
    print("One")
else:
    print("More than one")

# AND / OR / NOT
if not ((x > 20 and y < 50) or z < 0):
    print("Condition met")
    # different from bitwise operators (&, |, ~)

# Operator Precedence
    #bitwise > numerical comparison > Boolean

# FOR
my_list = ['cat', 'window', 'defenestrate']
for x in my_list:
    print(x, len(x))

for item in [1, 2, 3]:          # list
    print(item)
for item in range(2,1000):      # range object
    print(item)
for item in (1, 2, 3):          # tuple(immutable list)
    print(item)
for key in {'one':1, 'two':2}:  # dictionary (dict)
    print(key)
for char in "123":              # string (str)
    print(char)
for line in open("myfile.txt"): # file (TextIOWrapper)
    print(line, end='')
for i in range(5): # [0, 1, 2, 3, 4]
    print(i)
for x in range(2, 15, 3): # [2, 5, 8, 11, 14]
    print(x)

# Break & Continue
for x in range(2,6): # outer loop, x=2,3,4,5
    for y in range(1,6): # nested loop, y=1,2,3,4,5
        if x == y:
            continue # go directly to next y value
        # keep going if 'continue' not called...
        print(f'{x}, {y}')
        if x + y > 5:
            break # exit inner loop, go to next x value

# Enumerate
theList = [4, -2, 98, 2.5, 6.02]
for value in theList:
    if value > 5:
        print(value) # No loop variable to print!!

for (i,value) in enumerate(theList):
    if value > 5:
        print(i)

# While
a = -10
while a <= 10:
    print(a)
    a += 1                  # same as a=a+1
# while True:                 # infinite loop
    print('.')
    time.sleep(0.25)        # pause for 1/4 second
while True:
    if int(input('enter number > 10 to end: ')) > 10:
        break

# Pass
    # does nothing, used as a placeholder "syntactic filler"
while 1:
    pass    # infinite loop doing nothing

## CUSTOM FUNCTIONS -----------------------------------------------
def function_name():
    # function code goes here
    # and ends when indents stop
    print("Hello from a function")

# Print a Fibonacci series up to n, and display the result:
def fib(n):
    a, b = 0, 1
    while b < n:
        print(b)
        a, b = b, a+b
    print(a)

# Passing and Returning Values
# find maximum of two values:
def maximum(x,y): # Pass multiple parameters
    if x>y:
        max = x
    else:
        max = y
    return max # Return the result
# call the function:
print(maximum(2,3)) # order matters
print(maximum(y=3, x=2)) # order doesn't matter

# More Compact Version
def maximum(x,y):
    if x>y:
        return(x)
    else:
        return(y)
    
# Super Compact Version
def maximum(x,y):
    if x>y: return(x)
    else: return(y)

# Recersive Function
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
# Default Parameter Values
def maximum(x, y=5):
    if x>y: return(x)
    else: return(y)
print(maximum(1)) # returns 5
print(maximum(6)) # returns 6
print(maximum(1,2)) # returns 2

# Variable Arguments
def my_sum(*vals):
    sum = 0
    for v in vals:
        sum += v
    return sum

def sum_prod(m, *vals):
    sum = 0
    for v in vals:
        sum += v
    return m*sum


## ITERATORS AND GENERATORS ---------------------------------------
# Iterators --> iterable objects that can be manually iterated over
# Generators --> functions that can be used as iterators (cannot be "reset")

# Define a generator function:
def fibonacci():
    n1=0
    n2=1
    while True:
        yield n1        # value to return for each iteration
        n1, n2 = n2, n1 + n2
f = fibonacci()         # declare an iterator
# Print the 1st 10 values in the Fibonacci sequence:
for _ in range(10):
    print(next(f))

# Multiple yield generators
def gen(x):
    yield x**2
    yield x**3
    yield x**4
x = gen()           # declare a generator
for _ in range(3):
    print(next(x))  # calling next() after iterating gives an error