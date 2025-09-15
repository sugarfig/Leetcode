class Solution {
// create empty hashmap that will have keys (being the values in the array) & values (being the index of the value in the array)
// loop thru the original nums array
// subtract target from the value that is being looped thru in the nums array to get temp
// check if temp is in the hashmap
// if temp is in hashmap, then just take the value of that temp key and the current index and return those 2
// if temp is not in the hashmap then add the current value at index i of the array to the hashmap with the key being the value at index i and the value being the index i
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> values;
        vector<int> solution;

        for(int i = 0; i < nums.size(); i++)
        {
            int temp = target - nums[i];
            std::cout << "temp:";
            std::cout << temp << endl;
            std::cout << "target:";
            std::cout << target << endl;
            std::cout << "nums[i]:";
            std::cout << nums[i] << endl;
            
            if (values.count(temp))
            {
                solution.push_back(values[temp]);
                solution.push_back(i);
                std::cout << "solution";
                // for (int j = 0; j < solution.size(); j++)
                // {
                //     std::cout << solution[i];
                // }
                return solution;
            }
            else
            {
                std::cout << "here"<< endl;
                values[nums[i]] = i;
                std::cout << "values:";
                std::cout << values[nums[i]] << "at" << nums[i] << endl;
            }
        }

        return solution;
    }
};