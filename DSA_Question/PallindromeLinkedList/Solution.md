# Palindrome Linked List: A Step-by-Step Solution

A palindrome is a sequence that reads the same backward as forward. In this article, we'll explore how to determine if a singly linked list is a palindrome. We will use a two-pointer approach to achieve this with O(n) time complexity and O(1) space complexity. This method involves finding the middle of the list, reversing the second half, and then comparing the two halves.

## Problem Statement

Given a singly linked list, determine if it is a palindrome.

### Key Concepts

1. **Palindrome**: A sequence that reads the same backward as forward.
2. **Singly Linked List**: A list where each element points to the next, with the last element pointing to `null`.

## Solution Approach

We will solve this problem using two pointers:
1. `slow` pointer moves one step at a time.
2. `fast` pointer moves two steps at a time.

By the time the `fast` pointer reaches the end, the `slow` pointer will be at the middle of the list.

### Step-by-Step Solution

#### Step 1: Finding the Middle of the Linked List

The goal of this step is to position the `slow` pointer at the middle of the list.

```cpp
// Initializing pointers
fast = head;
slow = head;

// Finding the middle
while (fast != null && fast.next != null) {
    fast = fast.next.next;
    slow = slow.next;
}
```

#### Step 2: Reversing the Second Half

Once we find the middle, we will reverse the second half of the list starting from the `slow` pointer.

```cpp
prev = null;
while (slow != null) {
    temp = slow.next;
    slow.next = prev;
    prev = slow;
    slow = temp;
}
// Now, prev points to the head of the reversed second half.
```

#### Step 3: Checking for Palindrome

With the second half reversed, we will compare the first half and the reversed second half node by node.

```cpp
left = head;
right = prev; // Start of the reversed second half

while (right != null) {
    if (left.val != right.val) {
        return false;
    }
    left = left.next;
    right = right.next;
}
return true;
```

## Detailed Algorithm

Here is the complete algorithm combining all steps:

1. **Initialize Pointers**: Set `fast` and `slow` to the head of the list.
2. **Find Middle**:
   - Move `fast` two steps and `slow` one step until `fast` reaches the end.
3. **Reverse Second Half**:
   - Reverse the list from the `slow` pointer to the end.
4. **Compare Halves**:
   - Compare nodes from the start of the list with nodes from the start of the reversed second half.

### Example

Consider the linked list `1 -> 2 -> 3 -> 2 -> 1`.

- **Finding the Middle**: After the loop, `slow` points to `3`.
- **Reversing the Second Half**: The list becomes `1 -> 2 -> 3 -> 1 -> 2`.
- **Comparing Halves**: The first half `1 -> 2 -> 3` is compared with the reversed second half `1 -> 2 -> 3`.

Since all corresponding nodes match, the list is a palindrome.

## Pseudocode

Here is a pseudocode representation of the algorithm:

```cpp
// Initialize pointers
fast = head;
slow = head;

// Find the middle
while (fast != null && fast.next != null) {
    fast = fast.next.next;
    slow = slow.next;
}

// Reverse the second half
prev = null;
while (slow != null) {
    temp = slow.next;
    slow.next = prev;
    prev = slow;
    slow = temp;
}

// Check for palindrome
left = head;
right = prev;
while (right != null) {
    if (left.val != right.val) {
        return false;
    }
    left = left.next;
    right = right.next;
}
return true;
```

## Conclusion

This algorithm efficiently determines if a singly linked list is a palindrome by utilizing a two-pointer technique to find the middle, reverse the second half, and compare the two halves. The overall time complexity is O(n), and the space complexity is O(1), making it an optimal solution. By understanding and implementing this approach, you can easily check for palindromes in linked lists.
