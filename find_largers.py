# [2,1,5,4,3,6,7,8,2,12] find the third largest and third smallest number in the list
num = [2,1,5,4,3,6,7,8,2,12]

set_num = sorted(set(num))

third_smallest = set_num[2]

third_largest = set_num[-3]

print("Third smallest number is", third_smallest)

print("Third largest number is", third_largest)