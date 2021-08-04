class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u","A", "E", "I", "O", "U"]
        vindex = []
        v2change = []

        #find the index for vowels
        for i in range(len(s)):
            if s[i] in vowels:
                vindex.append(i)

        #Swtich the order of vowels
        for i in vindex:
            v2change.append(s[i])
        v2change.reverse()

        #replaced the vowel in a list
        sss=list(s)
        for i in range(len(v2change)):
            a=vindex[i]
            sss[a] = v2change[i]

        #make list format into str
        new_string = "".join(sss)

        return new_string