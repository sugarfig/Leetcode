class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        dictionary = {}
        
        for i in range(len(arr)):
            dictionary[arr[i]] = dictionary.get(arr[i], 0) + 1
            # print(arr[i])
        
        for k, v in dictionary.items():
            if k == 0 and v > 1:
                return True
            if k != 0 and k / 2 in dictionary:
                print("k/2", k/2, v)
                return True
            if k != 0 and k * 2 in dictionary:
                # print("k * 2")
                return True
            
        return False