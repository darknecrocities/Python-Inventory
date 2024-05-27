import time
import Functions

items_and_quantity = {"Onion":  20, "Garlic": 20, "Carrot": 20, "Potato": 20,  "Ginger": 20}

#User Input

user = input("Enter your Name: ")
time.sleep(1)
print(f"\nWelcome to the Inventory, {user}!")
time.sleep(1) 

#While Loop Iteration Program
#Main Program

while True:
    time.sleep(1)
    print('\n\tMain Menu')
    print("\n-------- Action --------\n")
    print('[1]   Display Inventory\n[2]   Add Item\n[3]   Remove Item\n[4]   Add to Stock\n[5]   Reduce Stock\n[6]   Quit')
    print("\n------------------------")
    Functions.action_choosing
    #var_action_choosing = Functions.action_choosing()
    match Functions.action_choosing(): 
        
#Display Process
        case 1:
            Functions.show_inventory(items_and_quantity)
            Functions.loading_main_menu()
            
#Add Item Process
        case 2:
            time.sleep(1)
            while True: #Loops in case input is below the minimum
                try: #Filters good input
                    quantity = int(input("\nAmount of items to add(0 to return): "))
            
                except: #Catches bad output
                    time.sleep(1)
                    print("\nInput invalid. Try again.")

                else: #Enters once try is successful
                    if quantity == 0: #Loads back to the main menu
                        time.sleep(1)
                        print("\nloading main menu...")
                        break
                    
                    else: #Enters here if input is valid
                        Functions.show_inventory(items_and_quantity)
                        for items_price in range(1, quantity+1): #Loops in how much there is to input
                            time.sleep(1)
                            print(f'\nItem {items_price}')
                            brand = input("Name of Item: ").capitalize()

                            if brand not in items_and_quantity: #Checks if the inputted item is not in the inventory
                                
                                while True: 
                                    try: #Filters out good input
                                        quantities = int(input("Quantity: "))
                                        Functions.add_item(items_and_quantity, brand, quantities) #Adds item
                                        break

                                    except: #Enters once quantities input is invalid 
                                        Functions.displays_invalid()
                                    
                                
                            else: #Enters here if item is already in the inventory
                                time.sleep(1)
                                print('\nThe item is already in the inventory.')
                        
                        case2_continue = input("\nDo you want to add more items(y/n)? ").lower()

                        if case2_continue == 'n': # If n, quits to the main menu
                            Functions.loading_inventory()
                            Functions.show_inventory(items_and_quantity)
                            Functions.loading_main_menu()
                            break
    
                        elif case2_continue != 'y': #If input is anything else other than y, input is invalid
                            Functions.displays_invalid()

                        else: #If input is y, loops back to adding items
                            time.sleep(1)

#Remove Item Process
        case 3:
            Functions.show_inventory(items_and_quantity)
            case3_flag = True
            while case3_flag == True: 
                delete_item = input("\nEnter an item that you want to remove(0 to return): ").capitalize()

                if delete_item == '0': #If 0, exits to main menu
                    time.sleep(1)
                    print('\nloading main menu...')
                    break

                elif delete_item not in items_and_quantity: #If input is not in inventory, loops to case3_flag
                        time.sleep(1)
                        print("\nThe item is not in the inventory. Try again")
                        time.sleep(1)

                else: #If input is valid, enters else
                    Functions.remove_item(items_and_quantity, delete_item) #Item removed
                    case3_else_flag = True
                    while case3_else_flag == True:
                        case3_decision = input("\nDo you want to remove more items(y/n)? ").lower()

                        if case3_decision == 'n': #If n, exits to main menu
                            Functions.loading_inventory()
                            Functions.show_inventory(items_and_quantity)
                            Functions.loading_main_menu()
                            case3_else_flag = False
                            case3_flag = False

                        elif case3_decision != 'y': #If input is anything else other than y, input is invalid
                            Functions.displays_invalid()
                            case3_else_flag == False

                        else: #If input is y, loops back to removing items
                            time.sleep(1)
                            break
#Add to Stock Process
        case 4:
            time.sleep(1)
            Functions.show_inventory(items_and_quantity)
            case4_flag = True
            while case4_flag == True:     
                select = input("\nSelect an item to add to its stock(0 to return): ").capitalize()

                if select == '0': #If n, exits to main menu
                    time.sleep(1)
                    print("\nloading main menu...")
                    case4_flag = False

                elif select not in items_and_quantity: #If input is not in the inventory, loops back to case4_flag
                    time.sleep(1)
                    print("\nThe item is not in the inventory. Try again")

                else: #Enters if input is valid
                    case4_else_flag = True

                    while case4_operation_flag == True:
                        try: #Filters out good input
                            number_quantity = int(input("Enter the amount: "))

                        except: #Enters if input is invalid
                            Functions.displays_invalid()
                            
                        else: #Enters when input is valid
                            Functions.increase_value(items_and_quantity, select, number_quantity)
                            time.sleep(1)
                            print("\nAmount added.")
                            time.sleep(1)
                            case4_more = True
                            
                            while case4_more == True:
                                case4_reduce = input("\nDo you want to add more to the stocks(y/n)? ")

                                if case4_reduce == 'n': #If n, exits to main menu
                                    case4_more == False
                                    case4_operation_flag = False
                                    case4_else_flag = False
                                    case4_flag = False
                                    time.sleep(1)
                                    print("\nloading inventory...")
                                    Functions.show_inventory(items_and_quantity)
                                    Functions.loading_main_menu()

                                elif case4_reduce != 'y': #If input is anything other than y, loops back to case4_more
                                    Functions.displays_invalid()

                                else: #Loops back to case4_flag
                                    case4_more == False
                                    case4_operation_flag = False
                                    case4_else_flag = False
                                    Functions.show_inventory(items_and_quantity)

#Add to Stock Process
        case 5:
            time.sleep(1)
            Functions.show_inventory(items_and_quantity)
            case5_flag = True
            while case5_flag == True:      
                select5 = input("\nSelect an item to lessen its stock(0 to return): ").capitalize()

                if select5 == '0': #Filters out bad input
                    time.sleep(1)
                    print("\nloading main menu...")
                    case5_flag = False

                elif select5 not in items_and_quantity: #Catches bad input, loops back to case5_flag
                    time.sleep(1)
                    print("\nThe item is not in the inventory. Try again")

                else:
                    case5_else_flag = True

                    while case5_else_flag == True:

                        try: #Filters out bad input
                            number_amount = int(input("Enter the amount: "))

                        except: #Catches bad input, loops back to case5_else_flag
                            Functions.displays_invalid()
                            
                        else: #Enters when input is valid
                                if number_amount > items_and_quantity[select5] or number_amount <= 0: #Checks if the desired amount to reduce is greater than the stock of the item
                                    time.sleep(1)
                                    print(f"\nThere is not enough of {select5} to reduce. Please try again.\n")
                                
                                else: #Enters when the desired amount to reduce is equal to or lower than the stock of the item
                                    
                                    Functions.decrease_value(items_and_quantity, select5, number_amount)
                                    time.sleep(1)
                                    print("\nAmount reduced.")
                                    time.sleep(1)
                                    case5_more = True

                                    while case5_more == True:
                                        case5_reduce = input("\nDo you want to reduce more of the stocks(y/n)? ").lower()

                                        if case5_reduce == 'n': #If n, quits to main menu
                                            case5_more = False
                                            case5_else_flag = False
                                            case5_flag = False
                                            time.sleep(1)
                                            print("\nloading inventory...")
                                            Functions.show_inventory(items_and_quantity)
                                            Functions.loading_main_menu()

                                        elif case5_reduce != 'y': #If input is anything but y, loops to case5_more 
                                            Functions.displays_invalid()

                                        else: #If y, loops back to case5_flag
                                            case5_more = False
                                            case5_else_flag = False
                                            Functions.show_inventory(items_and_quantity)

#Quit Process
        case 6:
            print("\nThanks For using of our program!!!")
            time.sleep(1.5)
            print("\n------- Members --------")
            print("\nCanela, Sean")
            time.sleep(1)
            print("Marquez, Jian Kalel")
            time.sleep(1)
            print("Miranda, Josh")
            time.sleep(1)
            print("Parejas, Arron")
            time.sleep(1)
            print("Seiji, Luis\n")
            break

#Shows inventory status
Functions.notification_quantity(items_and_quantity)