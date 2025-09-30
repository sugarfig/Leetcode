class Solution:
    # 2 for loops
    # 1 to go over accounts and 1 to go over banks
    # for every account sum amount in banks and add to an array
    # then go thru array and take biggest
    # dont actually need array. can just keep running total of largest wealth
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

        # max_wealth_so_far = 0
        
        # # Iterate over accounts
        # for account in accounts:
        #     # Add the money in each bank
        #     curr_customer_wealth = sum(account)
        #     # Update the maximum wealth seen so far if the current wealth is greater
        #     # If it is less than the current sum
        #     max_wealth_so_far = max(max_wealth_so_far, curr_customer_wealth)
            
        # # Return the maximum wealth
        # return max_wealth_so_far