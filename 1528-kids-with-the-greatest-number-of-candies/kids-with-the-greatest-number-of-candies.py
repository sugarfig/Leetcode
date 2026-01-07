class Solution:
    # loop through number of candies array, get largest amount of candy.
    # loop through again and add extra candies to each array value.
    # if greater than or equl to the largest amount, then write true to boolean array
    # otherwise write false.
    # return boolean result array.
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatestCandyAmount = 0
        hasGreatestCandyAmount = []
        for child in range(len(candies)):
            if candies[child] > greatestCandyAmount:
                greatestCandyAmount = candies[child]

        for child in range(len(candies)):
            if candies[child] + extraCandies >= greatestCandyAmount:
                hasGreatestCandyAmount.append(True)
            else:
                hasGreatestCandyAmount.append(False)

        return hasGreatestCandyAmount 
        