
arr = [2,3,1,4,5]
target = 7
new_list = []
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] + arr[j] == target:
            new_list.append((arr[i],arr[j]))
print(new_list)
  
   

    
    