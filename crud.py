#Temporary act as a DATABASE
items = ['banana', 'orange']

#Function for adding item to the ITEMS LIST / DATABASE
def add(item):
    items.append(item)

#Function for removing item
def remv(item):
    try:
        items.remove(item)
    except ValueError:
        print(f"'{item}' is not in the list")   

#Function for editing or updating item to the LIST
def edit(old_item, new_item):
  if old_item in items:
    index = items.index(old_item)
    items[index] = new_item
  else:
     print(f"'{old_item}' is not in the list")   

#Function for showing items in the LIST          
def show():
   print(items)


#Running the system until its True
while True:
 
#Choosing what type of function to hvae (e.i: create, delete, edit, clear)
 print("Options: create | delete | edit | show | clear")
 op = input("Choose: ").lower()

#Logic for each choose fucntion
 if op == 'create':
    text = input("Add item: ")
    add(text)
    show()
 elif op == 'delete':
    show()
    text = input("Delete: ")
    remv(text)
    show()
 elif op == 'edit':
    show()
    old = input("Enter item: ")
    new = input("Enter new item(edit): ")
    edit(old, new)
    show()
 elif op == 'show':
    show()
 elif op == 'clear':
    confirm = input("Are you sure want to delete?: ").lower()
    if confirm == 'yes':
     items.clear()
     show()
 else:
    print("Error")

#Deciding if want to continue to run this code
 con = input("Continue?").lower()
 if con == 'yes':
    continue
 else:
    break

