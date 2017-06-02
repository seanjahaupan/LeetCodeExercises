class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 1
        while True:
            newSquare = i * i
            if newSquare == num:
                return True
            if newSquare > num:
                return False
            i += 1
            
