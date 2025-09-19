num = [10,24,45,67,78,86,45]

closest = num[0]

for i in num:

    if abs(i)<abs(closest):

        closest = i

print(f"closest to zero is {closest}")
