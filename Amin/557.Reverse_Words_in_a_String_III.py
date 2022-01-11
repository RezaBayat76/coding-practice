class Solution:
    def reverseWords(self, s: str) -> str:
        reverse_words = []
        for word in s.split():
            reverse_words.append(word[::-1])
            
        return ' '.join(reverse_words)
        
