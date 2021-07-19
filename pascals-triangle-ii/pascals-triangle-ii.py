class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        output = [[1]]

        for i in range(1, rowIndex+1):
            currentRow = []
            for j in range(i+1):
                if j == 0 or j == i:
                    currentRow.append(1)
                else:
                    currentRow.append(output[i-1][j-1] + output[i-1][j])
            output.append(currentRow)

        return output[rowIndex]