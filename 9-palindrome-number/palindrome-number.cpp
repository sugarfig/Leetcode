class Solution {
public:
    bool isPalindrome(int x) {
        long int newNumber = 0;
        int originalNumber = x;
        if (x < 0)
        {
            return false;
        }

        if (x >= 0 && x <=9)
        {
            return true;
        }

        while (x > 0)
        {
            int modulus = x % 10;
            std::cout << "modulus: " << modulus << endl;
            x = x / 10;
            std::cout << "x - division: " << x << endl;

            newNumber = (newNumber * 10) + modulus;
            std::cout << "modulus * 10: " << modulus * 10 << endl;
            std::cout << "newNumber: " << newNumber << endl;
        }

        return (newNumber == originalNumber);
    }
};