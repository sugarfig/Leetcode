class Solution {
// take letter of the first one and as soon as you see a letter that doesnt match the first then return nothing
// if first letter matches first letter of everything else then go back to the first one and add second letter
// make sure to keep running tab of letter matches & current letters being tested. 
public:
    string longestCommonPrefix(vector<string>& strs) {
        string letterMatches = "";
        string currentTestMatch = "";
        bool allMatched = false;

        if (strs.size() == 0)
        {
            return "";
        }

        if (strs.size() == 1)
        {
            return strs[0];
        }

        // string smallestString = strs[0];

        // for(int j = 1; j < strs.size(); j++)
        // {
        //     if (strs[j].length() < smallestString.length())
        //     {
        //         smallestString = strs[j];
        //     }
        // }
        // std::cout << "smallestString" << smallestString << endl;
        // currentTestMatch.push_back(strs[0][0]);

        for(int j = 0; j < strs[0].size(); j++)
        {
            currentTestMatch.push_back(strs[0][j]);
            std::cout << "currentTestMatch:" << currentTestMatch << endl;

            for (int i = 1; i < strs.size(); i++)
            {
                if ((currentTestMatch.length() <= strs[i].length()) && (currentTestMatch == strs[i].substr(0, currentTestMatch.length())))
                {
                    allMatched = true;
                    std::cout << currentTestMatch << " matches at " << i << endl;
                }
                else {
                    allMatched = false;
                    break;
                }
                // for (int j = 0; j < strs[i].length(); j++)
                // {
                //     currentTestMatch.push_back(strs[i][j]);
                //     // currentTestMatch = strs[i][j];
                //     std::cout << "currentTestMatch:" << currentTestMatch << endl;
                // }
                // std:cout << "here";
            }

            if(!allMatched)
            {
                return letterMatches;
            }

            letterMatches = currentTestMatch;
        }

        return letterMatches;
        
    }
};