class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        d=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


        onlyletters = ''
        for i in s:
            if i in d:
                onlyletters=onlyletters+i
        aaa=len(onlyletters)

        c=''
        j=0
        for i in range(len(s)):
            if s[i] in d:
                j=j+1
                c=c+(onlyletters[aaa-j])
            else:
                c=c+(s[i])
        
        return c