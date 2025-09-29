sum = 0

while True:

 num1 = int(input("Enter first number : "))

 num2 = int(input("Enter second number"))

 sum = num1+num2

 more =input("If you want to enter add another number enter (y)/(no)").lower()

 if more == "y":
    
    num3 = int(input("Enter third number : "))

    sum+=num3
    
 else:
   
   print("Break loop")


 print(sum)


 

  


