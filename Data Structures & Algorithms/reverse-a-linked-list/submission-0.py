# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp =  head
        if temp is None:
            return None
        before = None
        after = temp.next
        while temp is not None:
            after =  temp.next
            temp.next = before
            before = temp
            temp = after
        head = before
        temp =  head
        return head
        

        