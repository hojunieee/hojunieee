class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        aaa=list()
        bbb=list()
        dictionarya = dict()
        dictionaryb = dict()

        for i in s:
            aaa.append(i)
        for i in aaa:
            dictionarya[i] = dictionarya.get(i,0)+1


        for i in t:
            bbb.append(i)
        for i in bbb:
            dictionaryb[i] = dictionaryb.get(i,0)+1

        if dictionarya == dictionaryb:
            return True
        else:
            return False