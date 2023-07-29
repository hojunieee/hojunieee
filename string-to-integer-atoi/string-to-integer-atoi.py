class Solution:
    def myAtoi(self, s: str) -> int:
        
        Reading = False
        sign = True
        digits = ['0','1','2','3','4','5','6','7','8','9']
        answer = ""

        for char in s:
            if not Reading:
                # iterate until we start number
                if char in digits or char == '-' or char == '+':
                    Reading = True
                    if char == '-':
                        sign = False
                    elif char == '+':
                        continue
                    else:
                        answer = answer + char
                elif char != ' ':
                    return 0
            else:
                # started reading 
                if char not in digits: 
                    break
                else:
                    answer = answer + char

        # convert to int, and check size
        if answer == "":
            return 0

        answer = int(answer)
        if answer > 2**31 and not sign:
            return -2**31
        elif answer > 2**31 - 1 and sign:
            return 2**31 - 1
        elif not sign:
            return -answer
        else:
            return answer
