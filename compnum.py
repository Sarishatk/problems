"""
create a variable called copnum and set the value to 50 ask the user to enter a number .while therir guess us is not the same as the comnum value
,tell them if their guess is too low or too high
and ask them to have another guess.
if they enter the same value as compnum,display
"""

copnum = 50

while True:

 num1 = int(input("Enter a number : "))

 if num1 == copnum:

    print("your guess is correct🎉")
    

    break

 elif num1<copnum:

    print("enter higher value ")

 elif num1>copnum:

    print("enter lower value ")





