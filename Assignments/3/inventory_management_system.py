"""
Inventory Management System
Features:
- Add new item
- Update item details (name, quantity, price)
- Remove item by ID
- View inventory (Name, ID, Quantity, Price, Total Value)
- Check total inventory value
- Find items with low stock
- Exit program
"""

inventory = {}
# inventory = { # Used for testing
#     1001: {"name": "Laptop",  "quantity": 10, "price": 800.50},
#     1002: {"name": "Monitor", "quantity": 5,  "price": 200.00},
# }


def input_int(prompt, min_value):
    """Check for valid integer when adding new item"""
    while True:
        try:
            val = int(input(prompt).strip())
            if min_value is not None and val < min_value:
                print(f"Please enter an integer >= {min_value}.")
                continue
            return val
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def input_float(prompt, min_value):
    """Check for valid float when setting price"""
    while True:
        try:
            val = float(input(prompt).strip())
            if min_value is not None and val < min_value:
                print(f"Please enter a number >= {min_value}.")
                continue
            return val
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def add_item():
    """Add a new item to inventory"""
    while True:
        item_id = input_int("Enter unique Item ID (integer): ", min_value=0)
        if item_id in inventory:
            print(f"ID {item_id} already exists. Please choose a different ID.")
            continue
        break
    name = input("Enter Item Name: ").strip()
    while not name:
        print("Name cannot be empty.")
        name = input("Enter Item Name: ").strip()
    quantity = input_int("Enter Quantity (integer): ", min_value=0)
    price = input_float("Enter Price per Unit (e.g., 12.50): ", min_value=0.0)

    inventory[item_id] = {"name": name, "quantity": quantity, "price": price}
    print(f"Item {name} (ID: {item_id}) added successfully.")


def update_item():
    """Change the specifics of an existing item"""
    if not inventory:
        print("Inventory is empty.")
        return
    item_id = input_int("Enter Item ID to update: ", min_value=0)
    item = inventory.get(item_id)
    if item is None:
        print(f"No item found with ID {item_id}.")
        return

    print(f"Current: Name='{item['name']}', Quantity={item['quantity']}, Price={item['price']}")
    new_name = input("Enter new name (leave blank to keep current): ").strip()
    if new_name:
        item["name"] = new_name
    new_q_input = input("Enter new quantity (leave blank to keep current): ").strip()
    if new_q_input != "":
        try:
            new_q = int(new_q_input)
            if new_q < 0:
                print("Quantity not updated: must be >= 0.")
            else:
                item["quantity"] = new_q
        except ValueError:
            print("Quantity not updated: invalid integer.")
    new_p_input = input("Enter new price (leave blank to keep current): ").strip()
    if new_p_input != "":
        try:
            new_p = float(new_p_input)
            if new_p < 0:
                print("Price not updated: must be >= 0.")
            else:
                item["price"] = new_p
        except ValueError:
            print("Price not updated: invalid number.")
    print("Update complete.")


def remove_item():
    """Used to remove an item that is in the inventory. Chosen by Item ID"""
    if not inventory:
        print("Inventory is empty.")
        return
    item_id = input_int("Enter Item ID to remove: ", min_value=0)
    if item_id in inventory:
        removed = inventory.pop(item_id)
        print(f"Removed item {removed['name']} (ID: {item_id}).")
    else:
        print(f"No item found with ID {item_id}.")


def view_inventory():
    """Lists the current inventory"""
    if not inventory:
        print("Inventory is empty.")
        return
    print("Inventory:")
    total = 0.0
    for item_id, item in sorted(inventory.items()):
        name = str(item["name"])
        qty = int(item["quantity"])
        price = float(item["price"])
        total = float(item["quantity"]) * float(item["price"])
        print(f"{item_id:<8}{name:<20}{qty:<10}{price:<12.1f}{total:<12.1f}")


def check_total_value():
    """See the total value of the entire inventory"""
    total = 0.0
    for item in inventory.values():
        total += float(item["quantity"]) * float(item["price"])
    print(f"\nTotal inventory value: {total:.2f}")  # Note that this differs from description by one decimal point


def find_low_stock():
    """Find which items are low in stock after choosing lowest amount wanted"""
    if not inventory:
        print("Inventory is empty.")
        return
    threshold = input_int("Enter stock threshold (integer): ", min_value=0)
    low_items = [(iid, it) for iid, it in inventory.items() if int(it["quantity"]) < threshold]
    if not low_items:
        print(f"No items with quantity below {threshold}.")
        return
    print(f"Items with quantity below {threshold}:")
    for iid, it in sorted(low_items):
        print(f"Name: {it['name']}, ID: {iid}, Quantity: {it['quantity']})")


def main():
    """Prints the main menu and let's you choose which functionality to perform"""
    menu = """
1. Add a New Item
2. Update Item Details
3. Remove an Item
4. View Inventory
5. Check Inventory Value
6. Find Items with Low Stock
7. Exit
"""
    while True:
        print(menu)
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_item()
        elif choice == "2":
            update_item()
        elif choice == "3":
            remove_item()
        elif choice == "4":
            view_inventory()
        elif choice == "5":
            check_total_value()
        elif choice == "6":
            find_low_stock()
        elif choice == "7":
            print("Exiting program. Goodbye.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting.")
