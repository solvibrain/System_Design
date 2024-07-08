class ListNode:
    def __init__(self,val =0, next = None)
        self.val
        self.next = next
class solution :
    def isPallindrome(self, head : ListNode())-> bool:

        # Using Two Pointe to get the middle node track of the LInked List
        fast = head
        slow = head
        while fast and fast.next :
            fast = fast.next.next
            slow = slow.next

        # Reversing the linkedLit from the Middle as slow is the middle of the Linked List
        prev = None
        while slow :
            temp = slow.next
            slow.next = prev
            prev = slow 
            slow = temp

        # comparing 
        left , right = head , prev
        while right:
            if right.val != left.val :
                return False
            left = left.next
            right = right.next        

        # If Everything is right and return True 
        return True    