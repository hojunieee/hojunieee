class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box=[]

        for i in board:
            row =[]
            for j in i:
                if j ==".":
                    continue
                if j in row:
                    return False
                row.append(j)
        
        for i in range(9):
            column=[]
            for j in board:
                if j[i] ==".":
                    continue
                if j[i] in column:
                    return False
                column.append(j[i])

        k = 1
        col = [1,4,7]
        row = [1,4,7]
        dirs = [[0,0],[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[1,-1],[-1,1],[1,1]]
        for i in row:
            for j in col:
                vals = []                                        
                for r,c in dirs:
                    temp = board[i+r][j+c]
                    if temp == '.':
                        continue
                    elif temp in vals:
                        return False
                    vals.append(temp)
                            
        return True