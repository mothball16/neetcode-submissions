class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word = ""
        idx = 0

        word_len_diff = abs(len(word1) - len(word2))
        alternate_length = len(word1) + len(word2) - word_len_diff
        for i in range(alternate_length):
            word += word1[i // 2] if i % 2 == 0 else word2[i // 2]
        
        if len(word1) < len(word2):
            word += word2[len(word1):]
        else:
            word += word1[len(word2):]
            
        return word