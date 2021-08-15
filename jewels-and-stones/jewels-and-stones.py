class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jdict = dict()
        a=0

        for i in jewels:
            jdict[i] = jdict.get(i,0)+1

        for i in stones:
            if i in jdict.keys():
                a=a+1
        return a