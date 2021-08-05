class Solution:
    def firstUniqChar(self, s: str) -> int:
        ddd= dict()

        for i in s:
            ddd[i] = ddd.get(i,0)+1

        for i in ddd:
            if ddd[i] ==1:
                return s.find(i)
        return -1