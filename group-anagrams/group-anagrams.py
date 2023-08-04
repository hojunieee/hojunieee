class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # isAnagram(str1,str2)
        
        wordBank = dict()
        
        for s in strs:
            s_sorted = ''.join(sorted(s))
            if s_sorted in wordBank:
                wordBank[s_sorted].append(s)
            else:
                wordBank[s_sorted] = [s]
        
        ansList = [words for words in wordBank.values()]

        return ansList
                
