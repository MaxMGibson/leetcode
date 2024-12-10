class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        temp = x
        reverse = 0
        
        while temp > 0:
            reverse = (reverse * 10) + (temp % 10)
            temp = temp / 10
            
        return reverse == x
        