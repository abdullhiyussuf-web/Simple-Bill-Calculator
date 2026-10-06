# Simple price calculator

price = float(input("500$: "))
quantity = int(input("40$: "))
total = price * quantity
print(f"{quantity} items at {price:.2f} each = {total:.2f}")