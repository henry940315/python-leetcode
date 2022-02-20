# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        a = []
        for i in lists:
            a = a + i
            a.sort()
                
                
        return a

data = Solution.mergeKLists(0,[[1,4,5],[1,3,4],[2,6]])
print(data)
