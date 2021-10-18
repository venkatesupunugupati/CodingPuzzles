def MoveZeros(nums) -> None:
    pos = 0        
    for i in range(len(nums)):
        el = nums[i]
        if el != 0:
            nums[pos], nums[i] = nums[i], nums[pos]
            pos += 1

def MoveSpecificNumber(nums,x) -> None:
    pos = 0        
    for i in range(len(nums)):
        if nums[i] != x:
            nums[pos], nums[i] = nums[i], nums[pos]
            pos += 1

nums = [1,2,3,4,3,5,6]
#MoveZeros(nums)
MoveSpecificNumber(nums,3)
print(nums)