# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head
        while(fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
            if(slow == fast):
                return True
        return False

nums = [3,2,0,-4]
head = None
root = None
for num in nums:
    temp = ListNode(num)
    if(head == None):
        root = temp
        head = temp
    else:
        head.next = temp
        head = head.next
sol = Solution()
res = sol.hasCycle(root)
print(res)


        