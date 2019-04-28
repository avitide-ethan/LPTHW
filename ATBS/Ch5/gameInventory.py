d = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def displayInventory(inventory):
    total = 0
    print("Inventory:")
    for k in inventory.keys():
        print(f"{d[k]} {k}")
        total += d[k]
    print("Total numbers of items: " + str(total))

def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory.keys():
            inventory[item] += 1
        else:
            inventory.setdefault(item, 1)
    return inventory



displayInventory(d)
addToInventory(d, dragonLoot)
displayInventory(d)


