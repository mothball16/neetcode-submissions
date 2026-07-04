class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word = ""

        word_len_diff = len(word1) - len(word2)
        alternate_length = len(word1) + len(word2) - abs(word_len_diff)
        for i in range(alternate_length):
            word += word1[i // 2] if i % 2 == 0 else word2[i // 2]
        
        if word_len_diff < 0:
            word += word2[len(word1):]
        else:
            word += word1[len(word2):]
            
        return word