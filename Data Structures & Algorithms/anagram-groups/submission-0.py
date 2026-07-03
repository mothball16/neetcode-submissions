from collections import defaultdict

class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # how can we match two words as anagrams?
        # naively, we would count up the letter occurences
        # python supports dicts with tuple keys, so we can place them in buckets
        # key would be the tuple representing the letter count, value would be a List of words
        # in the end, we would then transform the dict to a List

        matches = defaultdict(list)
        for word in strs:
            letter_counts = [0] * 26
            for c in word:
                idx = ord(c) - ord('a')
                letter_counts[idx] += 1
            letter_key = tuple(letter_counts)
            matches[letter_key].append(word)
        
        return list(matches.values())
            


                
            