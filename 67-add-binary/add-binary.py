class Solution:
    # check to see which string was longer/shorter and add leading zeroes to the shorter one
    # loop thru both lists (they should be the same length now)
    # do a xor operation on both chars from string A and string B and an xor on carry then add to front of result string
    # check if there should be a carry value and if not set back to zero, if yes then make carry 1
    # check if there is still a carry value after for loop. if there is then add to the front of result.
    # September 23, 2025 #18
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
            # print(charA, charB)
            # print(charB)
            if charA == '1' and charB == '1' or charA == '1' and carry == 1 or charB == '1' and carry == 1:
                carry = 1
            else:
                carry = 0
        if carry == 1:
            result = '1' + result
        
        return result
        