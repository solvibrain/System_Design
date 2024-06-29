class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

class Solution:
    def reverseLinkedList(self, head : ListNode) -> ListNode:
        prev, curr =None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        head = prev

        return head    
