# What does this print? Why?
"""for i in range(3):
    print("a")
for j in range(3):
    print("b")"""


# What does this print? Why?
""" for i in range(3):
    print("a")
    for j in range(3):
        print("b")

print("Done") """


# Loop from 1:00 to 12:59
""" for hour in range(1, 13):
    for minute in range(60):
        print(hour, minute) """

# Review questions
# Print "Hi" 10 times
""" for i in range(10):
    print("Hi") """

# Print 'Hello' 5 times and 'There' once
""" for i in range(1, 6):
    print("Hello")
print("There") """

# Print 'Hello' and 'There' 5 times, on different lines
""" for i in range(1, 6):
    print("Hello")
    print("There") """

# Print the numbers 0 to 9
""" for i in range(10):
    print(i) """

# Two ways to print the numbers 1 to 10
""" for i in range(1, 11):
    print(i)

for i in range(10):
    print(i + 1) """

# Two ways to print the even numbers 2 to 10
""" for i in range(2, 11, 2):
    print(i)

for i in range(5):
    print((i + 1) * 2) """

# Count down from 10 to 1 (not zero)
""" for i in range(10, 0, -1):
    print(i) """

# Print numbers out of a list
""" lst_of_numbers = [10, 2, 5, 4, 6, 20]

for item in lst_of_numbers:
    print(item) """
