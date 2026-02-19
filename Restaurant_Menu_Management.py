def initial_menu(add_item,remove_item,check_item):
    menu = ["Pizza", "Burger", "Pasta", "Salad"]
    if add_item:
        menu.append(add_item)
    if remove_item in menu:
        menu.remove(remove_item)
    return menu
def add_item(menu, item):
    menu.append(item)
    return menu
def remove_item(menu, item):
    if item in menu:
        menu.remove(item)
    return menu
def check_item(menu, item):
    return item in menu
# Example usage:
initial_menu = initial_menu(add_item, remove_item, check_item)
print("Initial Menu:", initial_menu)
new_menu = add_item(initial_menu, "Tacos")
print("Menu after adding Tacos:", new_menu) 
updated_menu = remove_item(new_menu, "Salad")
print("Menu after removing Salad:", updated_menu)
item_check = check_item(updated_menu, "Pizza")
print("Is Pizza in the menu?", item_check)


