import random
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""
text = "Hello World"
print (text)
prit (text)
"""

# Model
# Make a y variable.
# Make a x variable.
# Change y and x based on random numbers.
# Make a second set of y and xs, and make these change randomly as well.
# Work out the distance between the two sets of y and xs

# Make a y variable.
# Make a x variable.
# Change y and x based on random numbers.
y0 = 50
x0 = 50

if random.random() < 0.5:
        y0 += 1
else:
        y0 -= 1
if random.random() < 0.5:
        x0 += 1
else:
        x0 -= 1
print (y0, x0)

if random.random() < 0.5:
        y0 += 1
else:
        y0 -= 1
if random.random() < 0.5:
        x0 += 1
else:
        x0 -= 1
print (y0, x0)


# Make a second set of y and xs, and make these change randomly as well.
y1 = 50
x1 = 50

if random.random() < 0.5:
        y1 += 1
else:
        y1 -= 1
if random.random() < 0.5:
        x1 += 1
else:
        x1 -= 1
print (y1, x1)

if random.random() < 0.5:
        y1 += 1
else:
        y1 -= 1
if random.random() < 0.5:
        x1 += 1
else:
        x1 -= 1
print (y1, x1)


# Calculate the distance between the 2 sets of coordinates (y0, x0), and (y1, x1)
answer = (((y0 - y1)**2) + ((x0 - x1)**2))**0.5
print (answer)


# Make a y a random number - import random integer value 0-99
# Make a x variable number - import random integer value 0-99
# Change y and x based on random numbers.


random_number = random.randint(0,99)
y0 = random_number
random_number = random.randint(0,99)
x0 = random_number
print (y0, x0)




