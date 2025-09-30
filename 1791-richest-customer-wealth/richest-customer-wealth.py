class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # results = [0] * len(accounts)
        # for i in range(len(accounts)):
        #     for j in range(len(accounts[i])):
        #         results[i] = accounts[i][j] + results[i]
        # largest = 0
        # for i in range(len(results)):
        #     if results[i] > largest:
        #         largest = results[i]
        # return largest

                # Initialize the maximum wealth seen so far to 0 (the minimum wealth possible)
        max_wealth_so_far = 0
        
        # Iterate over accounts
        for account in accounts:
            # Add the money in each bank
            curr_customer_wealth = sum(account)
            # Update the maximum wealth seen so far if the current wealth is greater
            # If it is less than the current sum
            max_wealth_so_far = max(max_wealth_so_far, curr_customer_wealth)
            
        # Return the maximum wealth
        return max_wealth_so_far