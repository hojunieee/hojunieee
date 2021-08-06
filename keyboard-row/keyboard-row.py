class Solution:
    
    

    def findWords(self, words: List[str]) -> List[str]:
        
        def Convert(string):
            list1=[]
            list1[:0]=string
            return list1
    
        firstR = "qwertyuiop"
        secondR = "asdfghjkl"
        thirdR = "zxcvbnm"
        frdictkey = Convert(firstR)
        srdictkey = Convert(secondR)
        trdictkey = Convert(thirdR)

        anslist = []


        for i in words:
            iii=i.lower()
            a=0
            b=0
            c=0
            
            for j in range(len(iii)):
                if iii[j] in frdictkey:
                    a=a+1
                elif iii[j] in srdictkey:
                    b=b+1
                elif iii[j] in trdictkey:
                    c=c+1
                    
            if a == len(i) or b == len(i) or c == len(i):
                anslist.append(i)
        
        return anslist