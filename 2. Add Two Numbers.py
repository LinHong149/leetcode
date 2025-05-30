# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def getNum(curr, string):
            string = str(curr.val) + string
            if curr.next == None:
                return string
            return getNum(curr.next, string)

        num1 = getNum(l1, "")
        num2 = getNum(l2, "")

        sum = str(int(num1)+int(num2))
        sum = sum[::-1]

        def createLL(i):
            if i == len(sum):
                return None

            node = ListNode(int(sum[i]))
            node.next = createLL(i+1)
            return(node)


        l3 = createLL(0)
        print(l3)
        return(l3)


