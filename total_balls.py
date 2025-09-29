total_count = 10

while(total_count>0):

  print(f"there are {total_count} bottles are there, and if 1 green bottle should accidentally fall")

  answer = int(input("how many will be remaining"))


  if answer == total_count -1 :

    print(f"there will ba {answer} bottle")

    total_count = total_count-1

  else:

    print("try again")

print("no more")
