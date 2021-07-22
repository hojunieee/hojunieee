import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= s.lower()
        s = re.findall('[a-z0-9+]',s)

        length = int(len(s))
        answer =True

        for i in range(length-1):
            if s[i] == s[length-1-i]:
                answer = True
            else: 
                answer = False
                break
        return answer