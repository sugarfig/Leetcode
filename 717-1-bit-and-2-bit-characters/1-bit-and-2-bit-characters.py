class Solution:
    # loop thru list and if you see a 1, add 2 to jump 2 spots cause 1 has to be 
    # paired with another 1 or 0
    # if see a 0, just aadd 1 (jump 1 spot) cause that would mean that it is the 1st char
    # continue looping until your counter is before the last index
    # if counter is at last index and that index is 0, then return true
    # otherwise it is false
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        i = 0

        while i < len(bits) - 1:
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        if i == len(bits) - 1 and bits[i] == 0:
            return True
        else:
            return False

            
        