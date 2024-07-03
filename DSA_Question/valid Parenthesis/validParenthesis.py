import java.util.Stack;

public class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        char[] mapping = {')', '(', '}', '{', ']', '['};

        for (char c : s.toCharArray()) {
            if (c == mapping[0] && !stack.isEmpty() && stack.peek() == mapping[1]) {
                stack.pop();
            } else if (c == mapping[2] && !stack.isEmpty() && stack.peek() == mapping[3]) {
                stack.pop();
            } else if (c == mapping[4] && !stack.isEmpty() && stack.peek() == mapping[5]) {
                stack.pop();
            } else {
                stack.push(c);
            }
        }
        return stack.isEmpty();
    }
}