package PallindromeLinkedList;

public class Solution {
    // Assuming a ListNode class is defined with int val and ListNode next

/**
 * @param head
 * @return
 */
public boolean isPalindrome(ListNode head) {
    ListNode fast = head;
    ListNode slow = head;
    while (fast != null && fast.next != null) {
        fast = fast.next.next;
        slow = slow.next;
    }

    // Reversing the linked list from the middle as slow is the middle of the linked list
    ListNode prev = null;
    while (slow != null) {
        ListNode temp = slow.next;
        slow.next = prev;
        prev = slow;
        slow = temp;
    }

    // Comparing
    ListNode left = head;
    ListNode right = prev;
    while (right != null) {
        if (right.val != left.val) {
            return false;
        }
        left = left.next;
        right = right.next;
    }

    // If everything is right
    return true;
}
}
