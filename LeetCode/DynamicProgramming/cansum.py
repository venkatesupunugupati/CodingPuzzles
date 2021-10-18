def canSumRecursive(targetSum:int,nums,mem = {}):
    if(targetSum in mem): return mem[targetSum]

    if(targetSum == 0):return True
    if(targetSum < 0):return False

    for num in nums:
        remainder = targetSum - num
        if(canSumRecursive(remainder,nums,mem) == True):
            mem[targetSum] = True
            return True
    
    mem[targetSum] = False
    return False

def canSumIterative(targetSum:int, nums):
    arr = [False]*(targetSum+1)
    arr[0] = True
    for i in range(len(arr)):
        if(arr[i] == True):
            for num in nums:
                if(i+num < len(arr)):
                    arr[i+num] = True
    return arr[targetSum]

print(canSumRecursive(7, [5,3,4,7]))
print(canSumRecursive(7, [2,3]))
print(canSumRecursive(300, [7,14]))

print(canSumIterative(7, [5,3,4,7]))
print(canSumIterative(7, [2,3]))
print(canSumIterative(300, [7,14]))