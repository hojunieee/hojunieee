class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1]]
        for i in range(1, numRows):
            row = []
            for j in range(i+1):
			# the first and last value of evry row is 1
                if j == 0 or j == i:
                    row.append(1)
                else:
			# otherwise current value = previous row's (current value + next value)	
                    row.append(output[i-1][j-1] + output[i-1][j])
            output.append(row)
        return output