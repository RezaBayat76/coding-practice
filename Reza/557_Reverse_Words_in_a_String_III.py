class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        def reverseString(s):
            """
            :type s: List[str]
            :rtype: None Do not return anything, modify s in-place instead.
            """
            left, right = 0, len(s) - 1
            while left <= right:
                tmp = s[right]
                s[right] = s[left]
                s[left]= tmp
                left += 1
                right -= 1

            new = ''
            for x in s:
                new += x 
            return new
    
        s_new = ''
        for idx, word in enumerate(s.split()):
            word_reversed = reverseString(list(word))
            s_new += word_reversed
            if idx < len(s.split()) - 1:
                s_new += ' '
                
        return s_new        
