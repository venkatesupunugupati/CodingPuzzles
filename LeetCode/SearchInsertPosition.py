def SerachInsertPosition(nums,target):
    if(target > nums[-1]):
            return len(nums)
    for i in range(len(nums)):
        if(nums[i] >= target):
            return i

nums = [1,3,5]
target = 2
index = SerachInsertPosition(nums,target)
print(index)