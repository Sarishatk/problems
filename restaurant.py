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

menu = {
    "mandhi":540,
    "rice":60,
    "Dosa":15,
    "putt":30
}


print("Hello sir Welcome to Grocery")

name = input("enter your name :")

phone_no = input("enter your phone number :")

print(f"Hello {name}, welcome to our shop")

card = []

while True:

    print("available product in Grocery ")

    for item,price in menu.items():
     
     print(f"{item}-{price}")
    
    product = input("enter product : ")

    if product not in item.capitalize():
       
       print("Item not available")

    qty = int(input("enter quantity of the product"))

    card.append((product,qty,menu[product] * qty))

    more = print("do you want to add more product (yes/no)?")

    if more !=" yes" :
       
       break


    

    
       


