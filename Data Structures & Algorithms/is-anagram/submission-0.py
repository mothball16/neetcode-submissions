class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        occurences = {}
        for ch in s:
            occurences[ch] = occurences.get(ch, 0) + 1
        for ch in t:
            count = occurences.get(ch)
            if not count or count == 0:
                return False
            occurences[ch] -= 1
        for v in occurences.values():
            if v != 0:
                return False

        return True
