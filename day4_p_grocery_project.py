# Project 1: Grocery List Manager
"""
**Project 1: Grocery List Manager**

Objective:
Create a simple grocery list manager where users can add items, view the list, and remove duplicates (using set functionality).

Steps:
Ask the user to input grocery items (comma-separated).  
Store these items in a list.  
Convert the list to a set to remove duplicates.  
Display the updated grocery list.  
"""

# asking for items

intems = input("Please enter items name separating by commas :")

# item convered into list
intems_list = intems.strip().split(',')

# print(intems_list)
# # type casting
intems_unique = set(intems_list)

item_unique_list = list(intems_unique)

# # Show unique items list
print(f"Thank you for entering items here is your unique list of items {item_unique_list}")

# # end of function
# # patoto, tamato, chilli, sauces, bread, milk, milk, milk, sauces, sauces

