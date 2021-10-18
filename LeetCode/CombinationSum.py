# def CombinationSum(candidates,target):
#     res = []       
#     for i in range(len(candidates)):
#         if candidates[i] == target:
#             res += [[candidates[i]]]
#         elif candidates[i] < target:
#             res += [[candidates[i]]+j for j in CombinationSum(candidates[i:], target-candidates[i])]
#     return res

def CombinationSum(candidates, target):
    results = []
    def backtrack(remain, comb, start):
        if remain == 0:
            # make a deep copy of the current combination
            results.append(list(comb))
            return
        elif remain < 0:
            # exceed the scope, stop exploration.
            return

        for i in range(start, len(candidates)):
            # add the number into the combination
            comb.append(candidates[i])
            # give the current number another chance, rather than moving on
            backtrack(remain - candidates[i], comb, i)
            # backtrack, remove the number from the combination
            comb.pop()
    
    backtrack(target, [], 0)
    
    return results

def CombinationSum2(candidates, target):
    results = []
    def backtrack(remain, comb, start):
        if remain == 0:
            # make a deep copy of the current combination
            results.append(list(comb))
            return
        elif remain < 0:
            # exceed the scope, stop exploration.
            return

        for i in range(start, len(candidates)):
            if (i != start and candidates[i] == candidates[i - 1]):
                continue
            
            if (candidates[i] > target):
                break   
            # add the number into the combination
            comb.append(candidates[i])
            # give the current number another chance, rather than moving on
            backtrack(remain - candidates[i], comb, i+1)
            # backtrack, remove the number from the combination
            comb.pop()
    
    backtrack(target, [], 0)
    
    return results


nums = [10,1,2,7,6,1,5]
nums.sort()
target = 8
result = CombinationSum2(nums,target)
print(result)