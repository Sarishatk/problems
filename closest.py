
arr = [-2, -3, -4, -1, 2, 3, 4, 5, 1]

closest = arr[0]   
for num in arr:
    if abs(num) < abs(closest):
        closest = num
        if closest < 0  and abs( closest) in arr:
            closest = abs(closest)

print("The closest number to zero is:", closest)



