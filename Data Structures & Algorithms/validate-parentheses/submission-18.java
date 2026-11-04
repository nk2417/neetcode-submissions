class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        Map<Character, Character> validPaids = Map.of(
            ')', '(',
            '}', '{',
            ']', '['
        ); 

        for (char c : s.toCharArray()){
            if (validPaids.containsKey(c)){
                if (!stack.isEmpty() && stack.peek().equals(validPaids.get(c))){
                    stack.pop();
                } else {
                    return false;
                    
                }
            } else {
                stack.push(c);
            }
        }        
        return stack.isEmpty();
    }
}