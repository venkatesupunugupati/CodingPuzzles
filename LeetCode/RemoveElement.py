def RemoveElement(nums,val):
    if not( val in nums):
        return len(nums)
    j = 0
    for num in nums:
        if(num != val):
            nums[j] = num
            j += 1
    return j

nums = [0,1,2,2,3,0,4,2]
val = 2
l = RemoveElement(nums,val)
print(nums[0:l])

