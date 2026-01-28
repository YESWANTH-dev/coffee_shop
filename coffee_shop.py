# Coffee Shop Management System
# Author: Yeswanth Sarma
# Description: A simple console-based coffee shop billing system using Python

# Coffee menu stored as a dictionary
# Key   -> Item name
# Value -> Price
menu = {
    "Espresso": 80,
    "Cappuccino": 120,
    "Latte": 140,
    "Mocha": 160
}

# Store available stock for each item
stock = {
    "Espresso": 10,
    "Cappuccino": 8,
    "Latte": 6,
    "Mocha": 5
}

def show_menu():
    """Display the coffee menu"""
    print("\n📋 Coffee Menu")
    print("-" * 25)
    for item, price in menu.items():
        print(f"{item:12} : ₹{price}")
    print("-" * 25)

def take_order():
    """Take customer order and calculate bill"""
    total_bill = 0
    order = {}

    while True:
        item = input("\nEnter coffee name (or 'done' to finish): ").title()

        if item == "Done":
            break

        if item not in menu:
            print("❌ Item not available. Please choose from menu.")
            continue

        if stock[item] <= 0:
            print("❌ Sorry, item out of stock.")
            continue

        try:
            quantity = int(input("Enter quantity: "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        if quantity > stock[item]:
            print("❌ Not enough stock available.")
            continue

        # Update order and stock
        order[item] = order.get(item, 0) + quantity
        stock[item] -= quantity
        total_bill += menu[item] * quantity

        print(f"✅ Added {quantity} {item}(s) to your order.")

    return order, total_bill

def show_bill(order, total_bill):
    """Display final bill"""
    print("\n🧾 Final Bill")
    print("-" * 30)
    for item, qty in order.items():
        print(f"{item:12} x {qty} = ₹{menu[item] * qty}")
    print("-" * 30)
    print(f"Total Amount : ₹{total_bill}")
    print("🙏 Thank you! Visit Again.")

def main():
    """Main program execution"""
    print("☕ Welcome to Python Coffee Shop ☕")

    show_menu()
    order, total_bill = take_order()

    if order:
        show_bill(order, total_bill)
    else:
        print("\n❌ No items ordered.")

# Run the program
if __name__ == "__main__":
    main()
