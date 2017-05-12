class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        Given a roman numeral, convert it to an integer.Input is guaranteed to be within the range from 1 to 3999.
        https://leetcode.com/problems/roman-to-integer/#/description
        """
        roman = {'M': 1000, 'D': 500, 'C':100, 'L': 50, 'X': 10, 'V':5, 'I':1}
        count = 0
        
        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]: #check for things like XL, which is 40
                count -= roman[s[i]]
            else:
                count += roman[s[i]]
                
        return count + roman[s[-1]] #add the last character
