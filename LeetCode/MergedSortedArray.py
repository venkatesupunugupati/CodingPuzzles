def MergeSortedArray(a1:list,m:int,a2:list,n:int):
    nums1[m:] = nums2[:n]
    nums1.sort()

nums1 = [4,0,0,0,0,0]
m = 1
nums2 = [1,2,3,5,6]
n = 5
MergeSortedArray(nums1,m,nums2,n)
print(nums1)