## LeetCode Problem 322: Coin Change

### Problem Statement

Given a set of coins with different denominations and a total amount, the task is to determine the minimum number of coins needed to make up that amount. If that amount cannot be made up by any combination of the given coins, return -1.

### Example
Consider the coin denominations \([1, 3, 4]\) and the amount \(7\). Using a greedy algorithm, one might first pick the largest coin. This method fails here, as shown in the note: Greedy would pick \(4\) first, then \(3\), resulting in \(4 + 3 = 7\). This works, but in another case with the amount \(6\), greedy would pick \(4\) and then \(1+1\), resulting in \(4+1+1 = 6\), which is not the minimal number of coins. Hence, the greedy approach does not always yield the correct solution.

### Solution Approach: Dynamic Programming

#### Concept
The idea is to use dynamic programming to build up the solution for the amount step by step using previously computed values for smaller amounts.

#### Detailed Steps
1. **Initialization:**
   - Create an array `dp` of size `(amount + 1)` to store the minimum coins required for each amount from `0` to `amount`. Initialize each entry with a large value, typically `amount + 1`, since the maximum number of coins needed will not exceed this.
   - Set `dp[0] = 0` because no coins are needed to make the amount `0`.

2. **Filling the DP Array:**
   - Iterate over each amount from `1` to `amount`.
   - For each coin, update the `dp` array: If the current amount is greater than or equal to the coin's value, update `dp[amount]` as `dp[amount - coin] + 1` if it results in a smaller number of coins than the current value of `dp[amount]`.

3. **Final Result:**
   - The value at `dp[amount]` will hold the minimum number of coins needed for the given amount. If this value is still `amount + 1`, it means the amount cannot be formed with the given coins, and we return `-1`.

#### Pseudocode

```python
# Initialize the dp array with amount + 1
dp = [amount + 1] * (amount + 1)
dp[0] = 0  # Base case

# Fill the dp array
for i in range(1, amount + 1):
    for coin in coins:
        if i >= coin:
            dp[i] = min(dp[i], dp[i - coin] + 1)

# Check the result in dp[amount]
return dp[amount] if dp[amount] != amount + 1 else -1
```

### Time and Space Complexity

- **Time Complexity:** \(O(\text{amount} \times \text{number of coins})\)
- **Space Complexity:** \(O(\text{amount})\)

### Conclusion
This dynamic programming solution ensures that all possible combinations of coins are considered, leading to an optimal solution. The approach avoids the pitfalls of the greedy algorithm by leveraging previously computed results to build up the solution in an efficient manner.

### Example Walkthrough

Let's illustrate with the coins `[1, 3, 4]` and the amount `7`:

1. **Initialization:**
   ```python
   dp = [0, 8, 8, 8, 8, 8, 8, 8]  # Start with amount + 1 (8) for all
   ```

2. **Iteration:**
   - For `i = 1`, considering coin `1`:
     ```python
     dp[1] = min(dp[1], dp[0] + 1) => dp[1] = 1
     dp = [0, 1, 8, 8, 8, 8, 8, 8]
     ```
   - For `i = 2`, considering coin `1`:
     ```python
     dp[2] = min(dp[2], dp[1] + 1) => dp[2] = 2
     dp = [0, 1, 2, 8, 8, 8, 8, 8]
     ```
   - For `i = 3`, considering coins `1` and `3`:
     ```python
     dp[3] = min(dp[3], dp[2] + 1) => dp[3] = 3
     dp[3] = min(dp[3], dp[0] + 1) => dp[3] = 1 (using coin 3)
     dp = [0, 1, 2, 1, 8, 8, 8, 8]
     ```
   - Continue this for all amounts up to `7`.

3. **Result:**
   ```python
   dp[7] = 2  # The minimum number of coins to make 7 is 2 (3 + 4)
   ```

Thus, using the dynamic programming approach, we find that the minimum number of coins to make the amount `7` with denominations `[1, 3, 4]` is `2`.
