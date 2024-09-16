# Dictionary for product information
ecommerce_store = {
    "Electronics": {
        101: {"name": "Smartphone", "price": 699.99, "stock": 50},
        102: {"name": "Laptop", "price": 999.99, "stock": 30}
    },
    "Clothing": {
        201: {"name": "T-shirt", "price": 19.99, "stock": 200},
        202: {"name": "Jeans", "price": 39.99, "stock": 150}
    }
}

# print(ecommerce_store["Electronics"][102])

# new_product = (105, "iPhone", 1299, "stock": 25)

prod_info = input("Enter product info sep (,) :").strip().split(",")

# data cleaning converting product id to int
prod_info[0]= int(prod_info[0])

# print(prod_info)
new_product = prod_info

# 102: {"name": "Laptop", "price": 999.99, "stock": 30}
# [105,'iPhone','1299','5']
# adding new product
ecommerce_store["Electronics"][new_product[0]] = {
                                                    "name":new_product[1],
                                                    "price": new_product[2],
                                                    "stock": new_product[3]}

# printing output
print(f"Product added {new_product[1]} successfully also stock updated {new_product[3]}")
print(ecommerce_store)


# List of available categories
# categories = ["Electronics", "Clothing"]

# Tuple containing product details for a new item to be added
# new_product = (301, "Book", 12.99, 500)

# task
"""Tasks:
Access a specific product by category and ID:
Manually access the Laptop in the Electronics category.

Add a new product to the store:
Use the new_product tuple to add the Book to the Clothing category.

Convert a product name to uppercase:
Change the name of the T-shirt product to uppercase using string functions.
# convert iPhone to upper case based on key

Check if a product exists in the store:
Use the get() method to check if Smartphone exists in the Electronics category.
"""