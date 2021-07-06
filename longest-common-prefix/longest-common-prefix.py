class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        strs.sort(key=len)
        
        Fstr = strs[0]
        shortLen = len(Fstr)
        
        ans = ""
        
        for i in range(shortLen):
            for j in strs:
                if Fstr[i] != j[i]:
                    return ans                    
            ans = ans + Fstr[i]
        
        return ans
                