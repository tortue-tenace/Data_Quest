import sys

def parse_inventory(args: list) -> dict:
    inventory = {}

    for arg in args:
        parts = arg.split(':')
        if len(parts) != 2 or not parts[0] or not parts[1]:
            print(f"Error - invalid parameter '{arg}'")
            continue

        name, qty_str = parts[0], parts[1]

        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue

        try:
            qty = int(qty_str)
        except ValueError as e:
            print(f"Quantity error for '{name}': {e}")
            continue

        inventory.update({name: qty})

    return inventory


def add_item(inventory, name, qty):
    inventory[name] = qty
    return inventory


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ft_inventory_system.py <item>:<qty> ...")
        sys.exit(1)

    print("=== Inventory System Analysis ===")

    inventory = parse_inventory(sys.argv[1:])

    if not inventory:
        print("No valid items in inventory.")
        sys.exit(1)

    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")

    total = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total}")

    for key, val in inventory.items():
        pct = round((val / total) * 100, 1)
        print(f"Item {key} represents {pct}%")

    most = max(inventory, key=inventory.get)
    least = min(inventory, key=inventory.get)
    print(f"Item most abundant: {most} with quantity {inventory[most]}")
    print(f"Item least abundant: {least} with quantity {inventory[least]}")

    inventory = add_item(inventory, "magic_item", 1)
    print(f"Updated inventory: {inventory}")
