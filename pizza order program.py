#pizza order program
#olivia goodman 16/6/20
#version 4 - trying a menu based input method

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
def order_pizza(price):
    pizza_order = int(input("Enter the ID of the pizza you want to order: "))
    order.append(pizza_order)
    if pizza_order < gourmet_menu[0][2]:
        price += 8
    else:
        price += 15
    print()
    return price

#this function outputs what the user has ordered so far, and the total price
def output_order(price):
    print("Your order: ")
    for pizza in order:
        if pizza < gourmet_menu[0][2]:
            for option in regular_menu:
                if option[2] == pizza:
                    print("{}) {}".format(order.index(pizza) + 1, option[0]))
                    break
        else:
            for option in gourmet_menu:
                if option[2] == pizza:
                    print("{}) {}".format(order.index(pizza) + 1, option[0]))
                    break
    print("Total price: ${:.2f}".format(price))
    print()

#this function runs the main menu for the input
def order_input(price):
    while True:
        selection = input("Enter M to see the menu, P to order a pizza, O to see your order so far, or Q to quit: ").lower().strip()
        print()
        if selection == "m":
            output_menu()
        elif selection == "p":
            price = order_pizza(price)
        elif selection == "o":
            output_order(price)
        else:
            break
    return price
        
#main routine
#menu lists - storing the pizzas the user can choose from
regular_menu = [["Margherita", "Fresh tomato, mozzarella, fresh basil, parmesan", 1], ["Kiwi", "Bacon, egg, mozzarella", 2], ["Garlic", "Mozzarella, garlic", 3], ["Cheese", "Mozzarella, oregano", 4], ["Hawaiian", "Ham, pineapple, mozzarella", 5], ["Mediterranean (vegan)", "Lebanese herbs, olive oil, fresh tomatoes, olives, onion", 6]]
gourmet_menu = [["Meat", "Bacon, pancetta, ham, onion, pepperoni, mozzarella", 7], ["Chicken Cranberry", "Smoked chicken, cranberry, camembert mozzarella", 8], ["Satay Chicken", "Smoked chic, onions, capsicum, pine nuts, satay sauce, mozzarella Chilli flakes and dried basil", 9], ["Big BBQ Bacon", "Smoky Bacon served on our classic marinara tomato sauce, heaped with mozzarella, topped off with a sweet and tangy BBQ drizzle", 10], ["Veggie", "Sweet red onion, mushroom, red capsicum & melting mozzarella with drizzles of our tangy roast capsicum drizzle, finished with a dash of oregano", 11], ["Meatlovers", "Spicy pepperoni, Italian sausage, succulent ham, seasoned ground beef, and crispy bacon all piled onto classic marinara sauce and finished with cheesy mozzarella and a drizzle of BBQ sauce.", 12]]
#setting up price variable - will get added to as price increases
price = 0
#everything the user orders will get added to this list
order = []

price = order_input(price)
output_order(price)
