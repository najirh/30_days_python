"""
2. Shopping Discount System:
- Ask user the product name, 
- ask the price and 
- quantity check 
if the total is more than certail threshold = 1000--25%, 500, 15%, if qty > 3 5%
offer x amount of on the total cart discount = 25%
and print discounted amount and net amount to be paid!"""



# collecting inputs
product_details = input("Please enter details separating by comma (product_name,price,qty :)").strip().split(",")

# data cleaning 
# price datatypes to int
price = int(product_details[1])

# converting qty datatypes to int
qty = int(product_details[-1])

# total cart value
t = price * qty
total_value = price * qty
# total_value = 1200

if total_value > 1000:
    total_value -= total_value * 0.25
    print(f"Thank you for providing the details your cart info \nProduct_name:{product_details[0]} \nQty:#{qty} \nTotal cart amt: ${t} \nDiscount amt:${t*0.25} \nNet Pay: ${total_value}")
    
elif total_value > 500:
    total_value -= total_value * 0.15
    print(f"Thank you for providing the details your cart info \nProduct_name:{product_details[0]} \nQty:#{qty} \nTotal cart amt: ${t} \nDiscount amt:${t*0.15} \nNet Pay: ${total_value}")

elif qty > 3:
    total_value -= total_value * 0.05
    print(f"Thank you for providing the details your cart info \nProduct_name:{product_details[0]} \nQty:#{qty} \nTotal cart amt: ${t} \nDiscount amt:${t*0.05} \nNet Pay: ${total_value}")

else:
    print(f"Thank you for providing the details your cart info \nProduct_name:{product_details[0]} \nQty:#{qty} \nTotal cart amt: ${t} \nDiscount amt:${0} \nNet Pay: ${total_value}")
