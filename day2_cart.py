"""
Cart mini project -2

Create a ecommerce cart that takes which items they wanna buy  
Ask for their name  
How many qty they wanna buy  
At what price they are buying  
Show the total cart including $ sign
"""

# taking name
usr_name = input("May i know your name :")

# taking items
item = input("Please enter product name :")

# taking price
price = float(input("What is the price :"))


# asking qty
qty = int(input("How many qty are you looking for "))

results = price * qty

#displaying outcome
print(f"Thank you {usr_name} for purchasing {item} your net price is {results}$")

