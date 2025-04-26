# Exercises

# Write a while loop that will run the same as the following code
"""for i in range(10):
print(i)"""

""" count = 0
while count < 10:
    count += 1
    print(count) """

# What will this code print and why?
""" i = 1
while i <= 2**32:
    print(i)
    i *= 2 """

# It will print 2 to the power of 32 by doubling each time through
# Why? Because of the condition, as long as i is less than or equal
# to 2 to the power of 32, print i = i * 2, or keep doubling.

# Write a simple loop that asks the user if they wants to keep looping.
#  Loop until they says “no”.
""" keep_looping = "y"

while keep_looping == "y":
    quit = input("Do you want to keep looping? ")
    if quit == "no":
        break """

# The programmer wants to count down from 10. What is wrong and how to fix it?
# Err
""" i = 10
while i == 0:
    print(i)
    i -= 1 """

# Fix
""" i = 10
while i > 0:
    print(i)
    i -= 1 """

# What is wrong with this loop that tries to count to 10? What will
#  happen when it is run?
""" i = 1
while i < 10:
    print(i) """

# It will loop forever, because i is always less than 10
