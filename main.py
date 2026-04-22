def main():
    inventory = {}  # Dictionary to store items and their quantities

    while True:
        print("\nWarehouse Inventory System")
        print("1. View Current Inventory")
        print("2. Increase Inventory")
        print("3. Reduce Inventory")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            view_inventory(inventory)
        elif choice == "2":
            increase_inventory(inventory)
        elif choice == "3":
            reduce_inventory(inventory)
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid option.")


def view_inventory(inventory):
    if not inventory:
        print("Inventory is empty.")
    else:
        print("Current Inventory:")
        for item, qty in inventory.items():
            print(f"{item}: {qty}")


def increase_inventory(inventory):
    item = input("Enter item name: ").strip()
    try:
        qty = int(input("Enter quantity to add: ").strip())
        if qty <= 0:
            print("Quantity must be positive.")
            return
        inventory[item] = inventory.get(item, 0) + qty
        print(f"Added {qty} of {item}.")
    except ValueError:
        print("Invalid quantity.")


def reduce_inventory(inventory):
    item = input("Enter item name: ").strip()
    if item not in inventory:
        print("Item not found in inventory.")
        return
    try:
        qty = int(input("Enter quantity to reduce: ").strip())
        if qty <= 0:
            print("Quantity must be positive.")
            return
        if qty > inventory[item]:
            print("Cannot reduce below zero.")
            return
        inventory[item] -= qty
        if inventory[item] == 0:
            del inventory[item]
        print(f"Reduced {qty} of {item}.")
    except ValueError:
        print("Invalid quantity.")


if __name__ == "__main__":
    main()