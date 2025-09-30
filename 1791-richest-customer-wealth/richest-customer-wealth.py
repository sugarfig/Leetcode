class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        results = [0] * len(accounts)
        for i in range(len(accounts)):
            for j in range(len(accounts[i])):
                results[i] = accounts[i][j] + results[i]
        largest = 0
        for i in range(len(results)):
            if results[i] > largest:
                largest = results[i]
        return largest