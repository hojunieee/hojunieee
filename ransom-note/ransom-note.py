class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magdict = dict()
        for i in magazine:
            magdict[i] = magdict.get(i,0)+1

        for i in ransomNote:
            if i in magdict:
                magdict[i] = magdict[i]-1
                if magdict[i]<0:
                    return False
            else:
                return False
        return True