from collections import Counter

class Solution(object):
    def longestPalindrome(self, s):
        pal = 0
        odd = False

        palindrome = Counter(s)

        for v in palindrome.values():
            if v % 2 == 0:
                pal += v
            else:
                pal += v-1
                odd = True
        
        if odd:
            pal += 1
            
        return pal