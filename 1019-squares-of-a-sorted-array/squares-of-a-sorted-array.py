class Solution:
    # create new array squares and append num*num in every loop
    # use sort function to sort array
    # return the sorted array
    
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = []
        
        for num in nums:
            squares.append(num * num)
            
        return sorted(squares)