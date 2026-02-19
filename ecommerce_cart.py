def calculate_total_price(cart_items):
    # Handle empty cart
    if not cart_items:
        print("Cart is empty.")
        return 0
    
    # Calculate total price
    total = sum(cart_items.values())
    
    # Apply 10% discount if more than 5 items
    if len(cart_items) > 5:
        discount = total * 0.10
        total -= discount
        print(f"Discount applied: {discount}")
    
    return total


# Example input
cart_items = {
    'Laptop': 50000,
    'Headphones': 2000,
    'Mouse': 500,
    'Keyboard': 1500
}

# Call function
total_price = calculate_total_price(cart_items)

# Output
print(f"Total Price: {int(total_price)}")
