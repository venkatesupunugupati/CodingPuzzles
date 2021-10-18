def SingleNummber(nums):
    nums.sort()
    for index in range(0,len(nums)-1,2):
        if(nums[index] != nums[index+1]):
            return nums[index]
    return nums[-1]

nums = [4,1,2,1,2]
res = SingleNummber(nums)
print(res)