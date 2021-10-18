def bestSumRecursive(targetSum:int,nums, mem):

    if(targetSum in mem): return mem[targetSum]
    if(targetSum == 0): return []
    if(targetSum < 0): return None

    shortestCombination = None

    for num in nums:
        remainder = targetSum - num
        remainderCombination = bestSumRecursive(remainder,nums, mem)
        if(remainderCombination != None):
            combination = remainderCombination + [num]
            if(shortestCombination == None or len(combination) < len(shortestCombination)):
                shortestCombination = combination
    mem[targetSum] = shortestCombination
    return mem[targetSum]

def bestSumIterative(targetSum:int, nums):

    temptable = [None] * (targetSum + 1)
    temptable[0] = []

    for i in range(len(temptable)):
        if(temptable[i] != None):
            for num in nums:
                if (i+num < len(temptable)):
                    combination = temptable[i] + [num]
                    if(temptable[i+num] == None or len(temptable[i+num]) > len(combination)):
                        temptable[i+num] = combination

    return temptable[targetSum]
    



print(bestSumRecursive(8,[1,4,5],{}))
print(bestSumRecursive(7,[5,3,4,7],{}))
print(bestSumRecursive(100,[2,5,10,25],{}))


print(bestSumIterative(8,[1,4,5]))
print(bestSumIterative(7,[5,3,4,7]))
print(bestSumIterative(100,[2,5,10,25]))