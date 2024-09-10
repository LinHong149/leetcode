# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def GCF(a, b):
            while b:
                a, b = b, a % b
            return a


        currNode = head
        while currNode.next != None:
            gcf = GCF(currNode.val, currNode.next.val)
            newNode = ListNode(gcf, currNode.next)
            currNode.next = newNode

            # print(currNode)
            currNode = currNode.next.next
        
        # print(head)
        return(head)        
        
        
