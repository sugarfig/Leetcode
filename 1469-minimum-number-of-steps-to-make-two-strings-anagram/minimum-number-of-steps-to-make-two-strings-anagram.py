class Solution:
    # put both strings into a hashmap with the key being the letter and the value 
    # being how many times the letter shows up in the string
    # go thru both hashmaps til you reach the end of hashmap s
    # in the loop, compare if t is not in s or t value is less than s value 
    # if yes, then add s value minus t value to a global counter
    # return counter at end cause that is how many numbers you have to replace.
    def minSteps(self, s: str, t: str) -> int:
        sMap = defaultdict(int)
        tMap = defaultdict(int)

        minSteps = 0

        for char in s:
            sMap[char] += 1
        for char in t:
            tMap[char] += 1
        
        print(sMap)
        print(tMap)

        for key, value in sMap.items():
            # if key in tMap and tMap[key] == value:
            #     #continue
            # else:
            #     minSteps += 1
            if key not in tMap or tMap[key] < value:
                minSteps += value - tMap[key]
        
        return minSteps
        
        

        