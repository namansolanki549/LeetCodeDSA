# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
 

# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.findall("[a-zA-Z0-9]+", s)
        s = ''.join(s)
        s = s.lower()
        # if len(s) == 1:
        #     return False
        if s == s[::-1]:
            return True
        return False
