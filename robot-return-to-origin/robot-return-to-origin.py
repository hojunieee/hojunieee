class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        if moves =="":
            return True
        
        ddd = dict()
        for i in moves:
            ddd[i]=ddd.get(i,0)+1

        dictionary_items = ddd.items()
        ccc = sorted(dictionary_items)
        
        if len(ccc)==1 or len(ccc)==3:
            return False
        
        if len(ccc)==2:
            if ccc[0][0] =='D' and ccc[1][0] =='U':
                if ccc[0][1] == ccc[1][1]:
                    return True
            elif ccc[0][0] =='L' and ccc[1][0] =='R':
                if ccc[0][1] == ccc[1][1]:
                    return True
            else:
                return False
        if len(ccc)==4:
            if ccc[0][1] == ccc[3][1] and ccc[1][1] == ccc[2][1]:
                return True
        else:
            return False