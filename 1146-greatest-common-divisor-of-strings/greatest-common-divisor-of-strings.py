class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # i = j = 0
        # divisor = ""
        base = ""
        if len(str1) < len(str2):
            base = str1
        else:
            base = str2
        
        while base != "":
            print("here")
            if (len(str1) % len(base)) == 0 and (len(str2) % len(base)) == 0:
                print("here1")
                str1Multiple = len(str1) // len(base)
                str2Multiple = len(str2) // len(base)
                str1Test = base * str1Multiple
                str2Test = base * str2Multiple
                print("str1Multiple", str1Multiple)
                print("str2Multiple", str2Multiple)
                print("str1Test", str1Test)
                print("str2Test", str2Test)
                print("str1", str1)
                print("str2", str2)
                if str1Test == str1 and str2Test == str2:
                    return base
                print("here2")
                base = base[:-1]
            else:
                print("here3")
                base = base[:-1]
        return ""

        # while i < len(str1) and j < len(str2):
        #     if str1[i] != str2[j]:
        #         return ""
        #     else:
        #         divisor = divisor + str1[i]
        #         i += 1
        #         j += 1
        
        