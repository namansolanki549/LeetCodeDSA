# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
# Example 4:

# Input: x = 0
# Output: 0


# Constraints:

# -231 <= x <= 231 - 1

class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        y = ''
        if x[0] == '-':
            y = '-'
            new_x = x[::-1]
            new_x = new_x[:-1]
        else:
            new_x = x[::-1]
        if int(y+new_x) <= (-1)*2**(31) or int(y+new_x) >= 2**31-1:
            return 0
        return int(y+new_x)
