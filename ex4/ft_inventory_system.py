import sys

def parse_inventory(args):
    inventory = {}
    seen_names = []

    for arg in args:
        parts = arg.split(':')
        if len(parts) != 2 or not parts[0] or not parts[1]:
            print(f"Error: invalid parameter '{arg}'")
            continue

        name, qty_str = parts[0], parts[1]

        if not qty_str.isdigit():
            print(f"Error: invalid quantity in '{arg}'")
            continue

        if name in seen_names:
            print(f"Error: redundant parameter '{name}'")
            continue

        seen_names.append(name)
        inventory[name] = int(qty_str)

    return inventory


def display_inventory(inventory):
    print("\n--- Inventory ---")
    for key in inventory.keys():
        print(f"  {key}: {inventory[key]}")


def display_item_list(inventory):
    items = list(inventory.keys())
    print(f"\n--- Item list ---")
    print(f"  {items}")


def display_total(inventory):
    total = sum(inventory.values())
    print(f"\n--- Total quantity ---")
    print(f"  {total}")
    return total


def display_percentages(inventory, total):
    print(f"\n--- Percentages ---")
    for key in inventory.keys():
        pct = round((inventory[key] / total) * 100, 2)
        print(f"  {key}: {pct}%")


def display_extremes(inventory):
    keys = list(inventory.keys())
    values = list(inventory.values())

    max_val = max(values)
    min_val = min(values)

    # Premier depuis la ligne de commande en cas d'égalité
    most = keys[values.index(max_val)]
    least = keys[values.index(min_val)]

    print(f"\n--- Extremes ---")
    print(f"  Most abundant : {most} ({max_val})")
    print(f"  Least abundant: {least} ({min_val})")


def add_item(inventory, name, qty):
    inventory.update({name: qty})
    return inventory


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python inventory.py <item>:<qty> ...")
        sys.exit(1)

    inventory = parse_inventory(sys.argv[1:])

    if not inventory:
        print("No valid items in inventory.")
        sys.exit(1)

    display_inventory(inventory)
    display_item_list(inventory)
    total = display_total(inventory)
    display_percentages(inventory, total)
    display_extremes(inventory)

    # Ajout d'un nouvel item
    new_name = "legendary_sword"
    new_qty = 1
    print(f"\n--- Adding '{new_name}:{new_qty}' ---")
    inventory = add_item(inventory, new_name, new_qty)
    display_inventory(inventory)