package Coin change;

public class Solution {
    
        public static int coinChange(int[] coins, int amount) {
            int[] dp = new int[amount + 1];
            for (int i = 0; i <= amount; i++) {
                dp[i] = amount + 1;
            }
            dp[0] = 0;
    
            for (int a = 1; a <= amount; a++) {
                for (int c : coins) {
                    if (a - c > 0) {
                        dp[a] = Math.min(dp[a], 1 + dp[a - c]);
                    }
                }
            }
    
            return dp[amount] == amount + 1 ? -1 : dp[amount];
        }
    
        public static void main(String[] args) {
            int[] coins = {1, 2, 5};
            int amount = 11;
            System.out.println(coinChange(coins, amount));
        }
    
}
