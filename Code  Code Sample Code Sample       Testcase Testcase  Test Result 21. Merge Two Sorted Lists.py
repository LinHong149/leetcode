# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        a = ans

        while list1 or list2:
            if list1 == None:
                a.next = list2
                break
            elif list2 == None:
                a.next = list1
                break

            if list1.val < list2.val:
                a.next = ListNode(list1.val, None)
                list1 = list1.next
            else:
                a.next = ListNode(list2.val, None)
                list2 = list2.next
            a = a.next



        return ans.next
                
