import os
item_name = input("Enter name ")
if os.path.exists("items.txt"):
    with open("items.txt","a") as f:
        f.write(item_name + "\n")
else:
    with open("items.txt","w") as f:
        f.write(item_name + "\n")
   

with open("items.txt","r") as f:
    items = f.read()
    print(items)

