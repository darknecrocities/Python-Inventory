import time

def action_choosing():
    while True:
        try: #Filters out good input
            action_input = int(input("\nEnter a number to select an action: "))
        except: #Catches bad input
            time.sleep(1)
            print("\nInvalid input. Try again.")
        else: #Enters if input is integer
            if action_input > 6 or action_input < 1: #Enters if input is not with the range of 1-6, loops back to while True
                time.sleep(1)
                print("\nInvalid input. Try again.")
            else: #Valid input, returns action_input for match case
                return action_input

def show_inventory(inventory):
    time.sleep(1)
    print("\n------- Inventory ------\n")
    for item, quantity in inventory.items(): #Loops to show inventory
        splitter = item.split() #Turns the item into a list
        if len(splitter) != 1: #Enters here when the item has more than 1 word

            for each_word in splitter: #Loops to print out each of the items in the list, splitter
                if each_word != splitter[-1]: #Enters here if the word is not equal to the last value of the list, splitter
                    print(f"{each_word}")

                else: #Enters if word is equal to the last value of splitter
                    print(f"{splitter[-1]}\t: {quantity}")
                    
        else: #Only prints 1 worded item
            print(f'{item}\t: {quantity}')
    print("\n------------------------")

def loading_main_menu():
    time.sleep(1)
    input("\npress enter to go back to main menu.")
    time.sleep(1)
    print('\nloading main menu...')

def going_back():
    time.sleep(1)
    print("\nloading main menu...")

def loading_inventory():
    time.sleep(1)
    input("\npress enter to load inventory.")
    time.sleep(1)
    print("\nloading inventory...")
    time.sleep(1)

def add_item(dictionary, item, quantity):
    dictionary[item] = quantity
    time.sleep(1)
    print(f"\n{item} with a quantity of {quantity} is added to the inventory.")

def remove_item(dictionary, key):
    removed_value = dictionary.pop(key)
    time.sleep(1)
    print(f"\nRemoved item: {key} with a quantity of {removed_value}")
    time.sleep(1)

def decrease_value(dictionary, key, number):
    if key in dictionary:
        dictionary[key] -= number

def increase_value(dictionary, key, number):
    if key in dictionary:
        dictionary[key] += number

def displays_invalid():
    time.sleep(1)
    print("\nInvalid input. Please try again.\n")
    time.sleep(1)

def notification_quantity(dictionary):
    time.sleep(1)
    lengths = {key: value for key, value in dictionary.items()} #Creates new dict, same items
    print("----- STOCK STATUS -----")

    unstable = [] #Collects all items that have a stock of 5 and below

    for key, value_length in lengths.items(): #Iterates through the inventory

        if value_length < 5: #Appends items to the list "unstable"
            unstable.append(key)

    time.sleep(1)
    if unstable: #Enters when items are unstable
        print("\nItem stocks are unstable!")
        print(", ".join(unstable), "stocks are low!\n")
    else: #Enters when items are stable
        print("\nAll stocks are stable.\n")