class Solution:
    def intToRoman(self, num: int) -> str:
        letterOnes = ["-","I","X","C", "M"]
        letterFives = ["-","V","L","D"]
        roman = ""

        nDigits = len(str(num))
        for i in range(nDigits): # loop thorugh each digit
            digit = num//10**(nDigits-1) # get first digit
            num %= 10**(nDigits-1)
            
            if nDigits == 4:
                roman += "M"*digit
            else:
                if 0<=digit<=3:
                    roman += letterOnes[nDigits]*digit
                elif digit == 4 or digit == 5:
                    roman += letterOnes[nDigits]*(digit==4) + letterFives[nDigits]
                elif 6<=digit<=8:
                    roman += letterFives[nDigits] + letterOnes[nDigits]*(digit%5)
                else:
                    roman += letterOnes[nDigits]*(10-digit) + letterOnes[nDigits+1]
                    
            
            print(digit, num, roman)
            nDigits-=1
        return(roman)
        
