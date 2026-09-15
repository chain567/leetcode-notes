class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int length = nums.size();
        int target = length * (length + 1) / 2;
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }
        return target - sum;
    }
};