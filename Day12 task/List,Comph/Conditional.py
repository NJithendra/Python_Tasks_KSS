#Conditional Discount System

prices = [100, 200, 300, 400]
new_prices = [i * 0.9 if i > 200 else i for i in prices]
print(new_prices)
