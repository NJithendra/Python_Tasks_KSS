#Shopping Cart System

cart = []
try:
    n = int(input("Enter number of items: "))
    for i in range(n):
        item = input("Enter item name: ")
        cart.append(item)
    cart = set(cart)
    total = 0
    for item in cart:
        price = float(input("Enter price of " + item + ": "))
        if price > 0:
            total += price
        else:
            print("Invalid price")
    print("Cart items:", cart)
    print("Total cost:", total)
except ValueError:
    print("Please enter valid numbers")
