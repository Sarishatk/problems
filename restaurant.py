# You're designing a smart billing system for a grocery shop that supports:

# Showing a menu     >>>>>>>>>> dictionary for product and price
# ⦁	
# Taking multiple item orders >>>>>>>>>  if u need you can create a Cart (using a list )

# Generating a bill with, price, total, discount, and final amount

# Supporting coupon codes    >>>>>> if user enter "SAVE10"  10 % offer   | "save20" 20 % offer (only price above 1500)

# Repeated ordering until customer says "no"   >>>> if "yes" show menu again

# Asking for customer's phone number  >>> ask for customers name and phone number (greeting should be added)

# Saving the bill into a text file with customer details >>>> generate a bill in txt file showing (price name ,total)


# wlcome to Grocery billing system


# Menu (dictionary of products with prices)
menu = {
    "Rice": 50,

    "Sugar": 40,

    "Milk": 30,

    "Bread": 25,

    "Eggs": 6,

    "Oil": 120
}

print("🛒 Welcome to Smart Grocery Billing System")

# Get customer details

name = input("Enter your name: ")

phone = input("Enter your phone number: ")

print(f"\nHello {name}, let's start shopping!\n")

cart = []   # list to store items

while True:
    print("\nAvailable Items:")
    
    for item, price in menu.items():

        print(f"{item} - ₹{price}")

    choice = input("\nEnter the item you want to buy: ")
    
    if choice in menu:
        qty = int(input(f"Enter quantity of {choice}: "))
        cart.append((choice, qty, menu[choice] * qty))
        print(f"✅ {choice} added to cart.")
    else:

        print("❌ Item not found in menu!")

    repeat = input("Do you want to order more? (yes/no): ").lower()

    if repeat != "yes":

        break

    # generate bill
    
    total = sum(item[2] for item in cart)
    
    for item in cart:

        print(f"{item[0]} x{item[1]} = ₹{item[2]}")

        print(f"Total amount = ₹{total}")
