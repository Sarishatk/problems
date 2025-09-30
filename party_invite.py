"""
ask for the name of somebody the user want to invite to a party.After this display meassage "[name]"has now been invited and add to the count 1 
.then ask if they want to invite  somebody else .
keep repaeting this until they no longer to invite anyone elset to the party and then display how many people they have coming to the party

"""

count = 0

while True:

 user1 = input("Enter your name : ")

 print(f"{user1} has now been invited")

 count +=1

 another_user = input("Do you want to invite somebody else? (yes/no)")

 if another_user!="yes":

    print("exit")

    break

print(f"total count of invited people is {count}")

