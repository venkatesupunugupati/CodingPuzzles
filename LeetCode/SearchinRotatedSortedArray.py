def SearchInRotatedSortedArray(nums,target):
    lastFlag = False
    n = len(nums)
    if(n > 0):
        if (nums[0] > target ):
            lastFlag = True
    if(lastFlag):
        while(n >= 0 and nums[n-1] != target):
            n = n - 1
        if(n < 0):
            return -1
        else:
            return n - 1
    else:
        for i,num in enumerate(nums):
            if(num == target):
                return i
        return -1

nums = [4,5,6,7,0,1,2]
target = 0
index = SearchInRotatedSortedArray(nums,target)
print(index)
