# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
# Example 4:

# Input: s = "([)]"
# Output: false
# Example 5:

# Input: s = "{[]}"
# Output: true
 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.
class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in range(len(s)):
            if st != []:
                if st[-1] == '(' and s[i] == ')':
                    st.pop()
                    # print(1)
                elif st[-1] == '[' and s[i] == ']':
                    st.pop()
                    # print(2)
                elif st[-1] == '{' and s[i] == '}':
                    st.pop()
                    # print(3)
                else:
                    st.append(s[i])
            else:
                st.append(s[i])
        # print(st)
        if st != []:
            return False
        return True
