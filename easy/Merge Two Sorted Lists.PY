# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution(object):
    def mergeTwoLists( list1, list2):
        
        combine_list = list1 + list2

        
data = Solution.mergeTwoLists([1,2,3],[1,3,7])
print(data)
