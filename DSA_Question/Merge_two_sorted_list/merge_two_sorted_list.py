# Definition for singly linked list
# class ListNode:
#     def __init__:
#         self.val = val
#         self.next = next
    

class Solution :

    def merge_two_sorte_list(self, l1:ListNode, l2 : ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None :
            return l1
        dummy = ListNode()
        tail = dummy 

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next 
            else:
                tail.next = l2
                l2 = l2.next 
            tail = tail.next         

        if l1 :
            tail.next = l1

        if l2 :
            tail.next = l2        
        return dummy.next    