class Solution:
    def dayOfYear(self, date: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        y, m, d = map(int, date.split('-'))
        
        return d + sum(days[:m-1]) + (m > 2 and ((y % 4 == 0 and y % 100 != 0) or y % 400 == 0))