class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        carry = 0
        if len(a) < len(b):
            difference = len(b) - len(a)
            for i in range(0, difference):
                a = "0" + a
        else:
            difference = len(a) - len(b)
            for i in range(0, difference):
                b = "0" + b
        
        for charA, charB in reversed(list(zip(a, b))):
            result = str(int(charA) ^ int(charB) ^ carry) + result
            print(charA, charB)
            # print(charB)
            if charA == '1' and charB == '1' or charA == '1' and carry == 1 or charB == '1' and carry == 1:
                carry = 1
            else:
                carry = 0
        if carry == 1:
            result = '1' + result
        
        return result
        