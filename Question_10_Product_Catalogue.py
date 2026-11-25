
products = [
    ("P101", "Laptop", 50000, 5),
    ("P102", "Mouse", 500, 20),
    ("P103", "Keyboard", 1000, 3),
    ("P104", "Monitor", 12000, 0),
    ("P105", "Headphones", 1500, 10)
]

total_inventory_value = 0

print("----- PRODUCT CATALOGUE AUDIT -----")

for product in products:
    product_id, name, price, stock = product

    print("\nProduct ID:", product_id)
    print("Product Name:", name)
    print("Price: Rs.", price)
    print("Stock:", stock)

    if price <= 0 or stock < 0:
        print("Invalid Product Record")

    else:
        value = price * stock
        total_inventory_value += value

        print("Inventory Value: Rs.", value)

        if stock < 5:
            print("Restocking Required")

print("\nTotal Inventory Value: Rs.", total_inventory_value)
print("-----------------------------------")
