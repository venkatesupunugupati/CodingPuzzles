def RemoveDuplicates(arr):
    n = len(arr)
    if n == 0 or n == 1: 
        return n  
    j = 0
    for i in range(0, n-1): 
        if arr[i] != arr[i+1]: 
            arr[j] = arr[i] 
            j += 1
  
    arr[j] = arr[n-1] 
    j += 1
    return j

arr = [0,0,1,1,1,2,2,3,3,4]
l = RemoveDuplicates(arr)
print(arr[0:l])