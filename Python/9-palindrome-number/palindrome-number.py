class Solution:
    def isPalindrome(self, x: int) -> bool:
        xy=str(x)
        if xy==xy[::-1]:
            return True
        return False
        