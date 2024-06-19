# Task 1: Write a function that lets the user add items to a list.
def make_shopping_list():
    shopping_list = []

    while True:
        shopping_items = input("What items would you like to add to your shopping list? If you are done type 'done' If you would like to remove an item type 'remove' ")
        if shopping_items == "done":
            break
        elif shopping_items == "remove":                                             # Task 2: Include a feature to remove items from the list.
            item_to_be_removed = (input("which item would you like to remove? "))
            if item_to_be_removed in shopping_list:
                shopping_list.remove(item_to_be_removed)
            else:
                print(f"{item_to_be_removed} is not in cart")
        else:    
            shopping_list.append(shopping_items)

    return shopping_list

def print_cart(shopping_list):            # Task 3: Add a function that prints out the entire list in a formatted way.
    print("\nItems in Cart")
    if not shopping_list:
        print("Your cart is empty")
    else:
        for item in shopping_list:
            print(item)

items = make_shopping_list()
print_cart(items)

 

