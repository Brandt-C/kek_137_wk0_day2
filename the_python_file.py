# this is comment!

# it doesn't 
# matter how many lines


print('hello Kekambas!') # This is a comment after code that executes!

#variable definition
# syntax -->  <variable> = <value>
x = 5
some_group_of_chars = 'string'

# Data types
    # Numbers
        # integer, float, (and complex)
    # string
    # list, range
    # (dictionary)
    # bool
    # Nonetype

# nums
# integer --> pretty much a whole number
num1 = 10
num2 = -33
num3 = 30
num4 = float(num1)
print(type(num1))
print(type(num4))
# floats   they have a decimal!
num5  = 5.0
print(type(num5))

# math operators

print('\n MATH OPERATORS:')

# add   +
print(num1 + num3)

#subtract  -
print(num3 - num1)
print(30 - 10)

# multiply  *
print(num1*num3)

# divide  /   Always results in a float!
print(type(num3/num1))

# floor division //  Always results in a integer!
print(27 // 5)
print(25 // 5)

# modulo     %   Always results in a integer!
print(27 % 5)
print(25 % 5)

#side-bar:  = vs ==
# = this is assigning a value  (MAKE this equal to)
# == this is checking for equality ( IS this equal to????)  checking for type AND value equality
#  will always result in a boolean
# ALSO comparison operators:
#   ==   equal
#   !=     NOT equal
#   <
#   >
#   <=      less than OR equal to 
#   >=

# THIS is an important one!
# even or odd?
print(26 % 2 == 0)
print(27 % 2 != 0)

print(27 % 2 == 1)


# exponents   **
print(5 ** 5)


#side-bar variable naming conventions:
# int('33')
# int = 56
# int('987435')
# don't use pre-defined character sets (functions, classes etc)

# strings
# indexed, iterable, immuteable
# it's a bunch of characters inside of quotes. . . 
st1 = 'This is a string'
st2 = "This too!"
st3 = "So's this"
# double or single quotes are fine just make sure that the other kind surrounds their use inside OR use an escape character
st4 = 'so\'s this'

print(type(st1))

print(st1[2])
print('string'[0])

# concatenation   a fancy way of saying adding strings together
print(st1 + '. ' + st2)

# interpolation   an even fancier word to say we're gonna add strings and python things together
#  f-string
f_string = f"This is an f-string that also has this from python --> .{num2 + 100}."
print(f_string)
f_name = 'steve'
print(f"Hello {f_name.title()}!")

print('arnold'.title())
# print(num3.title())

print(f_name.upper())
print(f_name.lower())

# methods vs functions
# methods and functions are the same thing. . . EXCEPT methods work on a specific data type
#  the syntax is what gives it away!   <data_type>.method(parameter)   vs function(parameter)


print('\nLISTS:')
# lists
#  also called array in other languages
# ordered/indexed, iterable, and muteable
# syntax <variablename> = []
# contains values separated by commas
# can store just about anything in a list
my_list = []
my_list2 = [1, 2, 3, 4, 5]
my_list3 = ['1', '2', '3', '4', '5']
confused = [1, '2', 'three', 4.0, True, None]

print(my_list2[3])
print(my_list2)

print(confused[-2])

#  list.append()  - adds an item to the end of the list
my_list.append('Steve')
my_list.append('Arnold')
print(my_list)
my_list.append('Valerie')
my_list.append('Jill')
print(my_list)
my_list.append('Javan')
print(my_list.append('Santeri'))
print(my_list)


# list.pop()   - removes the last item from the list
# BUT  you save the value from .pop()  aka it returns the value
# AND there's an optional parameter that you can specify the index!

popped = my_list.pop()
print(my_list)
print(popped)

r_exp = [1, 1, 1, 23, 45, 56]
# list.remove()   -removes a value from the list, but note that it's the first occurence!
#  list.remove(value)
r_exp.remove(1)
r_exp.remove(1)
r_exp.remove(1)
print(r_exp)


my_list.append('Jill')
print(my_list)

my_list.remove('Jill')
print(my_list)

# membership check -->  the word 
# in
print('Jill' in my_list)
print('Joe' in my_list)
print('n' in 'None')

# conditionals!  if, elif, else
# we can use as many if statements as we want, each one checks for a circumstance to be True
# if we want to check the same variable against other circumstances we would use elif, or else
# we will always have an if, we CAN have as many elifs after that as we want, and we CAN finish after that with an else


print('\n AGE and conditionals')
age = 54

if age > 64:
    print('Senior')
elif age > 17:
    print('Adult')
else:
    print('kid')

if age > 17 and age < 65:
    print('Target audience')
else:
    print('not our audience')


# truth tree

# T  and T  == T
# T and F   == F
# F and F   == F

# T or T   == T
# T or F   == T
# F or F   == F

# functions
# syntax  def func(parameter):
#               codeblock to execute
# def function_name(parameter1, parameter2. . .):
#         codeblock

def odd(num):
    if num % 2 == 0:
        print('EVEN')
    else:
        print('ODD')
odd(4)


print('\n return vs print example:')

def add(a, b):
    print(a + b)

def mult(a, b):
    return a * b

add(5, 5)
print((mult(5, 5)))
add(mult(5, 5), 25)
# mult(add(5, 5), 10)
print(mult(5, 5)==25)
print(add(345, 345)==None)

# this_str = input('What\'s your name?\t')
# print(this_str)
# print(type(this_str))
# print(this_str.upper())


# loops
# the basic for loop
# the index loop
# the while loop

print(my_list)

# basic for loop
for name in my_list:
    print(name)

for name in my_list:
    print(name.upper())

# index loop
# for i in range(len(iterable)):
print('\nindex-loop:')
for i in range(len(my_list)):
    print(i, my_list[i])


# while loop
# while <condition>:
while True:
    print('HHHEEEEELLLLLLOOOOOOOOOOOOOO * 100000000000000')
    break

print('\nrange funct')
#Range function:
# range(start(optional default 0), stop (required), step(optional default 1)):
for x in range(5):
    print(x)
for x in range(0, 5, 1):
    print(x)

for x in range(10, 21, 2):
    print(x)

for x in range(-100, -135, -5):
    print(x)










