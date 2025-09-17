inventory = []
def add_item(item_name):
    inventory.append(item_name)

def count_items(item):
    if not item:
        return 0 
    return 1 + count_items(item[1:])

def main():
    add_item("dog food")
    add_item("cat toy")
    add_item("bird cage")
    add_item("fish tank")
    print(f'Total items = {count_items(inventory)}')
    for items in inventory:
        item_list = lambda x:print(f'items in stock {x}')
        item_list(items)

main()




