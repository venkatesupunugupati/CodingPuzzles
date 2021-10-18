def howSumRecursive(targetSum:int,nums, mem):

    if(targetSum in mem): return mem[targetSum]
    if(targetSum == 0):return []
    if(targetSum < 0):return None

    for num in nums:
        remainder = targetSum - num
        remainderResults = howSumRecursive(remainder,nums,mem)
        if(remainderResults != None):   
           mem[targetSum] = remainderResults + [num]
           return mem[targetSum] 
    mem[targetSum] = None
    return None

def howSumIterative(targetSum:int,nums):
    temptable = [None] * (targetSum + 1)
    temptable[0] = []

    for i in range(len(temptable)):
        if(temptable[i] != None):
            for num in nums:
                if (i+num < len(temptable)):
                    temptable[i+num] = temptable[i] + [num]

    return temptable[targetSum]

print(howSumRecursive(7, [5,3,4,7],{}))
print(howSumRecursive(7, [2,3],{}))
print(howSumRecursive(300, [7,14],{}))

print(howSumIterative(7, [5,3,4,7]))
print(howSumIterative(7, [2,3]))
print(howSumIterative(300, [7,14]))

