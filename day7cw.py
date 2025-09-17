grocery_list = ["milk","bread","eggs"]

def add_item(item):
    grocery_list.insert(1,item)
    grocery_list.pop()

add_item("wheat")
print(grocery_list)

for items in grocery_list:
    list_item = lambda x:print(f"item {x}")
    list_item(items)

def count_characters(grocery):
    if not grocery:
        return 0
    
    return len(grocery[0]) + count_characters(grocery[1:])

char_count=count_characters(grocery_list)
print(char_count)

    


    