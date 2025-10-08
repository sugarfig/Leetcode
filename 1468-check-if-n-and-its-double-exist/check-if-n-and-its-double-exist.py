class Solution:
    # go thru array and for every number add 1 to the value in the hashmap
    # now loop thru hashmap and check if the key is zero and if it is, then check if the value is more than 1. if so, return true
    # check if value is 
    def checkIfExist(self, arr: List[int]) -> bool:
        dictionary = {}
        
        for i in range(len(arr)):
            dictionary[arr[i]] = dictionary.get(arr[i], 0) + 1
            # print(arr[i])
        
        for k, v in dictionary.items():
            # written with multiple if statments for readability
            if k == 0 and v > 1:
                return True
            # if k !=0 and k / 2 in dictionary:
            #     return True
            if k != 0 and k * 2 in dictionary:
                return True
            
        return False