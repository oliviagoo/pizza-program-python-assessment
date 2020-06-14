#pizza order program
#olivia goodman 13/6/20
#version 1 - setting up and outputting the menu

regular_menu = [["Margherita", "Fresh tomato, mozzarella, fresh basil, parmesan", 1], ["Kiwi", "Bacon, egg, mozzarella", 2], ["Garlic", "Mozzarella, garlic", 3], ["Cheese", "Mozzarella, oregano", 4], ["Hawaiian", "Ham, pineapple, mozzarella", 5], ["Mediterranean (vegan)", "Lebanese herbs, olive oil, fresh tomatoes, olives, onion", 6]]
gourmet_menu = [["Meat", "Bacon, pancetta, ham, onion, pepperoni, mozzarella", 7], ["Chicken Cranberry", "Smoked chicken, cranberry, camembert mozzarella", 8], ["Satay Chicken", "Smoked chic, onions, capsicum, pine nuts, satay sauce, mozzarella Chilli flakes and dried basil", 9], ["Big BBQ Bacon", "Smoky Bacon served on our classic marinara tomato sauce, heaped with mozzarella, topped off with a sweet and tangy BBQ drizzle", 10], ["Veggie", "Sweet red onion, mushroom, red capsicum & melting mozzarella with drizzles of our tangy roast capsicum drizzle, finished with a dash of oregano", 11], ["Meatlovers", "Spicy pepperoni, Italian sausage, succulent ham, seasoned ground beef, and crispy bacon all piled onto classic marinara sauce and finished with cheesy mozzarella and a drizzle of BBQ sauce.", 12]]

print("Regular Menu ($8 each):")
for item in regular_menu:
    print("{} (ID: {}) - {}".format(item[0], item[2], item[1]))
print()
print("Gourmet Menu ($15 each):")
for item in gourmet_menu:
    print("{} (ID: {}) - {}".format(item[0], item[2], item[1]))
