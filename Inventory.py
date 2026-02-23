import json

#Task 1 — Read the inventory
with open("inventory.json","r") as inv:
     inventory = json.load(inv)
     print(f"Total length is:{len(inventory)}")

#Task 2 — Update and save 
new_book = {"title": "Atomic Habits", "author": "James Clear", "price": 14.99, "in_stock": True}
with open("inventory.json","r") as inv:
     inventory = json.load(inv)

inventory.append(new_book)

with open("inventory.json","w") as invent:
     json.dump(inventory,invent,indent=4)

print(inventory) 

# Task 3 — Display the inventory 
with open("inventory.json","r") as inv:
     inventory = json.load(inv)
for booklist in inventory:
   print(f"Title: {booklist["title"]} | Author:{booklist["author"]} | Price: {booklist["price"]}")