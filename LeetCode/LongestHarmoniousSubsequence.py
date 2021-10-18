def LongestHarmoniousSubsequence(nums):
    d = dict()
    res = 0
    for num in nums:
        d[num] = d.get(num,0) + 1
        if((num + 1) in d.keys()):
            res = max(res,d[num] + d[num + 1])
        if((num - 1) in d.keys()):
            res = max(res,d[num] + d[num - 1])
    return res

nums = [1,3,2,2,5,2,3,7]
res = LongestHarmoniousSubsequence(nums)
print(res)