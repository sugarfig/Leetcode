class Solution:
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
        