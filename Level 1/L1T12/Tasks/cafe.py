# ==== Program to calculate stock worth of products in a cafe ====

# List with all item in cafe
menu = ['latte', 'capuccino', 'expresso', 'cortado', 'tea']

# Dictionary with current stock
stock = {'latte': 24, 
         'capuccino': 14,
         'expresso': 30,
         'cortado': 10,
         'tea': 50
        }

# Dictionary with item prices
price = {'latte': 3.40, 
         'capuccino': 3.50,
         'expresso': 2.50,
         'cortado': 2.90,
         'tea': 2.20
        }


total_stock = 0
print("CAFE CURRENT STOCK")

for items in menu:
    item_value = round((stock[items] * price[items])) # I had to Google how to make the result of the calculation show less than 2 decimal points. That is why I used 'round'
    total_stock += item_value   
    print(f"{items}: £{item_value}") # Prints stock per individual item
print()
print(f"The total stock worth in the cafe is: £{total_stock}")