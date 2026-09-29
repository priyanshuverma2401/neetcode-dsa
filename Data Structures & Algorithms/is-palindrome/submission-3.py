class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left <= right: #O(N)
            if not s[left].isalnum() or s[left] == " ":
                left+=1
            elif not s[right].isalnum() or s[right] == " ":
                right-=1
            else:
                if s[left].lower() != s[right].lower():
                    return False
                else:
                    left+=1
                    right-=1
        return True

# Time Complexity: O(N)
# Space Complexity: O(1)

        