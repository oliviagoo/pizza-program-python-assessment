#pizza order program
#olivia goodman 23/6/20
#version 8 - error handling for the boundaries

#this function confirms the order and finishes the program with a final output
def confirm(order, stuff_crust, price, order_type, address, name):
    print("Thank you for your order! Please confirm that the following details are correct.")
    #confirming the pizza details
    while True:
        output_order(price, order, stuff_crust)
        correct = input("Is this what you would like to order? (Y or N) ").strip().lower()
        if correct == "n":
            reorder = input("Are you sure you want to redo your order? (Y or N) ")
            if reorder == "y":
                if order_type == "d":
                    price = 8
                else:
                    price = 0
                price, order, stuff_crust = order_input(price)
        else: break
    print()
    #confirming the delivery details
    while True:
        delivery_output(order_type, address, name)
        correct = input("Is this correct? (Y or N) ").strip().lower()
        if correct == "n":
            reorder = input("Are you sure you want to change your order details? (Y or N) ")
            if reorder == "y":
                if order_type == "d":
                    price -= 8
                order_type, address, price, name = delivery(price)
        else: break
    #final output and goodbye
    print()
    print("Final order:")
    delivery_output(order_type, address, name)
    output_order(price, order, stuff_crust)
    print("Thank you! See you soon, we hope you enjoy your meal!")

#this function outputs the delivery/pick up information 
def delivery_output(order_type, address, name):
    if order_type == "d":
        print("Order Delivery")
        print("Delivery address: {}".format(address))
        print("Delivered to: {}".format(name.title()))
    else:
        print("Order Pickup")
        print("Picked up by: {}".format(name.title()))

#this function asks the user whether they want delivery or pickup
def delivery(price):
    name = input("What is your name? ")
    answer = input("Would you like to get your pizza delivered (D), or pick it up? (P) ").lower().strip()
    if answer == "d":
        price += 8
        address = input("What is your delivery address? ")
        return answer, address, price, name
    else:
        return answer, "n/a", price, name

#this function outputs the menu
def output_menu():
    print("Regular Menu ($8 each):")
    print()
    for item in regular_menu:
        print("{} (ID: {}) - {}".format(item[0], item[2], item[1]))
    print()
    print("Gourmet Menu ($15 each):")
    print()
    for item in gourmet_menu:
        print("{} (ID: {}) - {}".format(item[0], item[2], item[1]))
    print()

#this function orders a pizza
def order_pizza(price, order, stuff_crust):
    #the restriction on how many pizzas they can order
    PIZZA_RESTRICTION = 3
    pizza_order = int(input("Enter the ID of the pizza you want to order: "))
    #if they've already ordered three pizzas
    if len(order) < PIZZA_RESTRICTION:
        #if they're ordering an id lower than one and higher than the highest value
        if pizza_order > 0 and pizza_order <= gourmet_menu[-1][2]:
            order.append(pizza_order)
            if pizza_order < gourmet_menu[0][2]:
                price += 8
            else:
                price += 15
            print()
            answer, price = stuffed_crust(price, stuff_crust)
            stuff_crust.append(answer)
        else:
            print("Please enter a pizza ID that exists.")
    else:
        print("Unfortunately, due to the Covid-19 pandemic, you can only order a maximum of three pizzas.")
    return price, order

#this function asks if the user wants stuffed crust
def stuffed_crust(price, stuff_crust):
    answer = input("Would you like to add stuffed crust for $3? (Y or N?) ").lower().strip()
    if answer == "y":
        price += 3
    print(answer)
    return answer, price
    
#this function outputs what the user has ordered so far, and the total price
def output_order(price, order, stuff_crust):
    print("Your order: ")
    for pizza in range(len(order)):
        if stuff_crust[pizza] == "y":
            if order[pizza] < gourmet_menu[0][2]:
                for option in regular_menu:
                    if option[2] == order[pizza]:
                        print("{}) {} with stuffed crust".format(pizza + 1, option[0]))
                        break
            else:
                for option in gourmet_menu:
                    if option[2] == order[pizza]:
                        print("{}) {} with stuffed crust".format(pizza + 1, option[0]))
                        break
        else:
            if order[pizza] < gourmet_menu[0][2]:  
                for option in regular_menu:
                    if option[2] == order[pizza]:
                        print("{}) {}".format(pizza + 1, option[0]))
                        break
            else:
                for option in gourmet_menu:   
                    if option[2] == order[pizza]:
                        print("{}) {}".format(pizza + 1, option[0]))
                        break
    print("Total price: ${:.2f}".format(price))
    print()

#this function runs the main menu for the input
def order_input(price):
    #everything the user orders will get added to this list
    order = []
    #keeps track of which pizzas have stuffed crust
    stuff_crust = []
    while True:
        selection = input("Enter M to see the menu, P to order a pizza, O to see your order so far, or Q to quit: ").lower().strip()
        print()
        if selection == "m":
            output_menu()
        elif selection == "p":
            price, order = order_pizza(price, order, stuff_crust)
        elif selection == "o":
            output_order(price, order, stuff_crust)
        else:
            if len(order) > 0:
                break
            else: print("You have to order at least one pizza")
    return price, order, stuff_crust
        
#main routine

#menu lists - storing the pizzas the user can choose from
regular_menu = [["Margherita", "Fresh tomato, mozzarella, fresh basil, parmesan", 1], ["Kiwi", "Bacon, egg, mozzarella", 2], ["Garlic", "Mozzarella, garlic", 3], ["Cheese", "Mozzarella, oregano", 4], ["Hawaiian", "Ham, pineapple, mozzarella", 5], ["Mediterranean (vegan)", "Lebanese herbs, olive oil, fresh tomatoes, olives, onion", 6]]
gourmet_menu = [["Meat", "Bacon, pancetta, ham, onion, pepperoni, mozzarella", 7], ["Chicken Cranberry", "Smoked chicken, cranberry, camembert mozzarella", 8], ["Satay Chicken", "Smoked chic, onions, capsicum, pine nuts, satay sauce, mozzarella Chilli flakes and dried basil", 9], ["Big BBQ Bacon", "Smoky Bacon served on our classic marinara tomato sauce, heaped with mozzarella, topped off with a sweet and tangy BBQ drizzle", 10], ["Veggie", "Sweet red onion, mushroom, red capsicum & melting mozzarella with drizzles of our tangy roast capsicum drizzle, finished with a dash of oregano", 11], ["Meatlovers", "Spicy pepperoni, Italian sausage, succulent ham, seasoned ground beef, and crispy bacon all piled onto classic marinara sauce and finished with cheesy mozzarella and a drizzle of BBQ sauce.", 12]]

#setting up price variable - will get added to as price increases
price = 0

order_type, address, price, name = delivery(price)
price, order, stuff_crust = order_input(price)
confirm(order, stuff_crust, price, order_type, address, name)
