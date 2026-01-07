class Solution:
    # take the shortest string and check if it is divisble by the base
    # if it is divisible, multiply the base by the number of length gotten from division 
    # for both string 1 and 2 and then check if new strings are equal to original strings
    # if yes, return base
    # if no, then remove last character from base and do again until base == ""
    # if it is not divisble, remove last chacter from base and loop process/checks again until 
    # base == ""
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        base = ""
        if len(str1) < len(str2):
            base = str1
        else:
            base = str2
        
        while base != "":
            # print("here")
            if (len(str1) % len(base)) == 0 and (len(str2) % len(base)) == 0:
                # print("here1")
                str1Multiple = len(str1) // len(base) # // does floor in division
                str2Multiple = len(str2) // len(base) # // does floor in division
                str1Test = base * str1Multiple
                str2Test = base * str2Multiple
                # print("str1Multiple", str1Multiple)
                # print("str2Multiple", str2Multiple)
                # print("str1Test", str1Test)
                # print("str2Test", str2Test)
                # print("str1", str1)
                # print("str2", str2)
                if str1Test == str1 and str2Test == str2:
                    return base
                # print("here2")
                base = base[:-1]
            else:
                # print("here3")
                base = base[:-1]
        return ""
        
        