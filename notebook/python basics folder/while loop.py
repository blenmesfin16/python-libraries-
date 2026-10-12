# Fixed data set representing items in a shopping cart
cart_items = {
    "Laptop Stand": 45.00,
    "Wireless Mouse": 25.50,
    "Mechanical Keyboard": 90.00
}

subtotal = 0
tax_rate = 0.08  # 8% tax

print("=== YOUR RECEIPT ===")
# Loop through the dictionary items automatically
for item, price in cart_items.items():
    print(f"{item}: ${price:.2f}")
    subtotal += price

print(f"\nSubtotal: ${subtotal:.2f}")

# Control Flow: Automatic discount tier
if subtotal > 100:
    discount = subtotal * 0.10  # 10% off
    print(f"Bulk Discount (10%): -${discount:.2f}")
    subtotal -= discount
else:
    print("Discount applied: None")

# Calculate final totals
total_tax = subtotal * tax_rate
final_total = subtotal + total_tax

print(f"Tax (${tax_rate * 100}%): ${total_tax:.2f}")
print(f"TOTAL AMOUNT DUE: ${final_total:.2f}")
