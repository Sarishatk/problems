num = int(input("Enter a positive integer"))
n = num
digit_sum = 0
while num!=0:
    digit = num %10
    digit_sum+=digit
    num = num//10

if n%digit_sum==0:
    print("harshad number")
else:
    print("not harshad number")