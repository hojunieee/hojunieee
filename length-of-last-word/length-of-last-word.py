class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        a= s.split()

        if a == []:
            return 0
        else:
            alen =len(a)-1
            answerWord=a.pop(alen)
            return len(answerWord)