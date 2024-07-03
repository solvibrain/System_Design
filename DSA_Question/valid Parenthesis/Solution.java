package valid Parenthesis;

import java.util.Stack;

public class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        char[][] closetoOpen = {{')', '('}, {'}', '{'}, {']', '['}};
        
        for (char c : s.toCharArray()) {
            for (char[] pair : closetoOpen) {
                if (c == pair[0]) {
                    if (!stack.isEmpty() && stack.peek() == pair[1]) {
                        stack.pop();
                    } else {
                        return false;
                    }
                }
            }
            if (!Character.toString(c).matches("[\\(\\{\\[]")) {
                stack.push(c);
            }
        }
        return stack.isEmpty();
    }
} 
