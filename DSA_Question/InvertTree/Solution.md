# Inverting a Binary Tree: A Step-by-Step Solution

Inverting a binary tree means swapping the left and right children of every node in the tree. This article will guide you through the process of inverting a binary tree using Depth-First Search (DFS) and recursion. By the end of this article, you will understand how to implement this solution efficiently.

## Problem Statement

Given a binary tree, invert the tree and return its root.

### Key Concepts

1. **Binary Tree**: A tree data structure where each node has at most two children, referred to as the left child and the right child.
2. **Inversion**: Swapping the left and right children of each node in the tree.
3. **DFS (Depth-First Search)**: An algorithm for traversing or searching tree data structures, starting at the root and exploring as far as possible along each branch before backtracking.

## Solution Approach

We will solve this problem using recursion and DFS. The idea is to traverse each node, swap its left and right children, and then recursively apply the same operation to the left and right subtrees.

### Step-by-Step Solution

#### Step 1: Recursive Function to Invert the Tree

We define a recursive function `invertTree` that inverts a binary tree rooted at a given node. The base case for this function is when the node is `null`.

#### Step 2: Swapping the Children

For each node, we swap its left and right children.

#### Step 3: Recursive Calls

After swapping the children, we recursively call the `invertTree` function on the left and right children.

### Detailed Algorithm

Here is the algorithm in a step-by-step format:

1. **Check if the Node is Null**: If the node is `null`, return `null`.
2. **Swap the Children**: Swap the left and right children of the current node.
3. **Recursive Calls**: Recursively call `invertTree` on the left and right children.

### Example

Consider the binary tree:
```
    4
   / \
  2   7
 / \ / \
1  3 6  9
```

After inversion, the tree becomes:
```
    4
   / \
  7   2
 / \ / \
9  6 3  1
```

## Pseudocode

Here is a pseudocode representation of the algorithm:

```cpp
function invertTree(root):
    if root is null:
        return null
    
    // Swap the left and right children
    temp = root.left
    root.left = root.right
    root.right = temp
    
    // Recursively invert the left and right subtrees
    invertTree(root.left)
    invertTree(root.right)
    
    return root
```

### Python Implementation

Here is a Python implementation of the algorithm:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    if root is None:
        return None
    
    # Swap the left and right children
    temp = root.left
    root.left = root.right
    root.right = temp
    
    # Recursively invert the left and right subtrees
    invertTree(root.left)
    invertTree(root.right)
    
    return root
```

## Conclusion

Inverting a binary tree is a straightforward problem that can be efficiently solved using DFS and recursion. By swapping the left and right children of each node and recursively applying this process to the entire tree, we achieve the desired inversion. This approach ensures that the tree is correctly inverted with a time complexity of O(n), where n is the number of nodes in the tree.
