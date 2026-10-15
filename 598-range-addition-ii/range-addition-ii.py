class Solution:
    # the max count will be at the smallest (x,y) value cause all the squares/rectangles
    # in the matrix overlap so we just need to find the min x and y
    # loop thru ops and get smallest a value and b value in each pair
    # multiply smallest x and y value with eachother to get the amount of spaces that have the max integer
    def maxCount(self, m: int, n: int, ops: list[list[int]]) -> int:
        minXval = m
        minYval = n

        for items in ops:
            minXval = min(minXval, items[0])
            minYval = min(minYval, items[1])
        
        return minXval * minYval
