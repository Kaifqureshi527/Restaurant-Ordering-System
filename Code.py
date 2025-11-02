# Restaurant Menu Ordering System

# Step 1: Define menu
menu = {
    "burger": 120,
    "pizza": 250,
    "pasta": 180,
    "sandwich": 90,
    "coffee": 70,
    "ice cream": 100
}

print("🍽️ Welcome to Python Café!")
print("Here is our menu:")
for item, price in menu.items():
    print(f"{item.title()} : ₹{price}")

total_bill = 0  # Initialize total

# Step 2: Start ordering loop
while True:
    order = input("\nEnter the item you want to order: ").lower()
    
    # Step 3: Check if item exists
    if order in menu:
        total_bill += menu[order]
        print(f"{order.title()} added to your order. Current total: ₹{total_bill}")
    else:
        print("❌ Sorry, that item is not on the menu.")

    # Step 4: Ask if user wants to continue
    another = input("Do you want to order another item? (yes/no): ").lower()
    if another != "yes":
        break

# Step 5: Display total bill
print(f"\n🧾 Your total bill is ₹{total_bill}. Thank you for dining with us! 🍴")
