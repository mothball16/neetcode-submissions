class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        for char1, char2 in zip(word1, word2):
            res.append(char1)
            res.append(char2)
        
        min_len = min(len(word1), len(word2))
        
        res.append(word1[min_len:])
        res.append(word2[min_len:])

        return "".join(res)