# class Address:
#     """Hold all the fields for a mailing address."""
#
#     def __init__(self):
#         """Set up the address fields."""
#         self.name = ""
#         self.line1 = ""
#         self.line2 = ""
#         self.city = ""
#         self.state = ""
#         self.zip = ""
#
#
# def main():
#     # Create an address
#     home_address = Address()
#
#     # Set the fields in the address
#     home_address.name = "John Smith"
#     home_address.line1 = "701 N. C Street"
#     home_address.line2 = "Carver Science Building"
#     home_address.city = "Indianola"
#     home_address.state = "IA"
#     home_address.zip = "50125"
#
#     # Create another address
#     vacation_home_address = Address()
#
#     # Set the fields in the address
#     vacation_home_address.name = "John Smith"
#     vacation_home_address.line1 = "1122 Main Street"
#     vacation_home_address.line2 = ""
#     vacation_home_address.city = "Panama City Beach"
#     vacation_home_address.state = "FL"
#     vacation_home_address.zip = "32407"
#
#     print("The client's main home is in " + home_address.city)
#     print("His vacation home is in " + vacation_home_address.city)
#
#
# main()


# 16.4. Using Objects in Functions
# Passing in an object as a function parameter
# class Address:
#     """Hold all the fields for a mailing address."""
#
#     def __ini__(self):
#         """Set up the address fields."""
#         self.name = ""
#         self.line1 = ""
#         self.line2 = ""
#         self.city = ""
#         self.state = ""
#         self.zip = ""
#
#
# def print_address(address):
#     """Print an address to the screen."""
#
#     print(address.name)
#     # If there is a line1 in the address, print it
#     if len(address.line1) > 0:
#         print(address.line1)
#     # If there is a line2 in the address, print it
#     if len(address.line2) > 0:
#         print(address.line2)
#     print(address.city + ", " + address.state + " " + address.zip)
#
#
# def main():
#     # ... code for creating home_address and vacation_home_address
#     # goes here
#
#     # Create an address
#     home_address = Address()
#
#     # Set the fields in the address
#     home_address.name = "John Smith"
#     home_address.line1 = "701 N. C Street"
#     home_address.line2 = "Carver Science Building"
#     home_address.city = "Indianola"
#     home_address.state = "IA"
#     home_address.zip = "50125"
#
#     # Create another address
#     vacation_home_address = Address()
#
#     # Set the fields in the address
#     vacation_home_address.name = "John Smith"
#     vacation_home_address.line1 = "1122 Main Street"
#     vacation_home_address.line2 = ""
#     vacation_home_address.city = "Panama City Beach"
#     vacation_home_address.state = "FL"
#     vacation_home_address.zip = "32407"
#
#     print_address(home_address)
#     print()
#     print_address(vacation_home_address)
#
#
# main()


from dataclasses import dataclass


@dataclass
class Address:
    """Hold all the fields for a mailing address."""

    name: str
    city: str


a = Address("Alice", "Paris")
print(a)  # Output: Address(name='Alice', city='Paris')


# Exercises
# class Cat:
#     def __init__(self):
#         self.name = ""
#         self.color = ""
#         self.weight = 0
#
#     def meow(self):
#         print("meow")
#
#
# my_cat = Cat()
#
# my_cat.name = "Mexico"
# my_cat.color = "Black"
# my_cat.weight = 5
#
# my_cat.meow()


# class Monster:
#     def __init__(self):
#         self.name = ""
#         self.health = 100
#
#     def decrease_health(self, amount):
#         self.health -= amount
#
#         print("Current health:", self.health)
#         print("The animal dies if current health goes below zero")
#
#
# take_health = Monster()
# take_health.decrease_health(20)
# take_health.decrease_health(10)
