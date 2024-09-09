# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math

class Solution:
    

    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:    
        
        matrix =  [[-1 for i in range(n)] for j in range(m)]

        direction = 0 #r, d ,l ,u

        top = 0
        bottom = m-1
        left = 0
        right = n-1

        value = head
        counter = 0
        while top <= bottom and left <= right:
            if direction == 0: # right
                for i in range(left, right+1):
                    matrix[top][i] = value.val
                    if value.next != None:
                        value = value.next
                    else:
                        return(matrix)
                    # print(value.val)
                    counter += 1
                top += 1
                direction = 1
            elif direction == 1: #down
                for i in range(top, bottom+1):
                    matrix[i][right] = value.val
                    if value.next != None:
                        value = value.next
                    else:
                        return(matrix)
                    # print(value.val)
                    counter += 1
                right -= 1
                direction = 2
            elif direction == 2: # left
                for i in range(right, left-1, -1):
                    matrix[bottom][i] = value.val
                    if value.next != None:
                        value = value.next
                    else:
                        return(matrix)
                    # print(value.val)
                    counter += 1
                bottom -= 1
                direction = 3
            elif direction == 3: #up
                for i in range(bottom, top-1, -1):
                    matrix[i][left] = value.val
                    if value.next != None:
                        value = value.next
                    else:
                        return(matrix)
                    # print(value.val)
                    counter += 1
                left += 1
                direction = 0

        return(matrix)
        





