

class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        ''' a really inefficient one using two pointers'''

        if len(s) == 0:
            return 0
        
        if len(s) == 1:
            return 1
        
        if len(s) == 2:
            if s[0] != s[1]:
                return 2
            else:
                return 1
            
        #use two pointers
        start = 0
        longest = 1
        d = {}
        d[s[0]] = 0
        i = 1
        
        # record the appearance position of each character
        while i < len(s):
            if s[i] in d and d[s[i]] >= start:
                if i - start > longest:
                    longest = i - start
                start = d[s[i]] + 1
            
            d[s[i]] = i
            i += 1
        
        if i - start > longest:
            longest = i - start
            
        return longest
        