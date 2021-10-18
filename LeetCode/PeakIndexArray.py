def PeakIndex(arr):
    temp = 0
    for index,num in enumerate(arr,start=0):
        if(num >= temp):
            temp = num
            continue
        else:
            return index - 1

arr = [0,1,0]
index = PeakIndex(arr)
print(index)