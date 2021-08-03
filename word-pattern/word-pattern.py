class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        patternlist = list()
        for i in pattern:
            patternlist.append(i)
            
        stringsplit = s.split(" ")
        
        
        
        if len(patternlist) != len(stringsplit):
            return False
        
        
        
        ccc=dict()

        for i in range(len(patternlist)):
            if patternlist[i] in ccc:
                if ccc[patternlist[i]] != stringsplit[i]:
                    return False
            else:
                ccc[patternlist[i]] = stringsplit[i]
                
                
        ddd = dict()
        for k, v in ccc.items():
            ddd[v] = k
              
        for i in range(len(stringsplit)):
            if stringsplit[i] in ddd:
                if ddd[stringsplit[i]] != patternlist[i]:
                    return False
            else:
                ddd[stringsplit[i]] = patternlist[i]
                
        return True
