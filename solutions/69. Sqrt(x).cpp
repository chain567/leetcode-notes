class Solution {
public:
    int mySqrt(int x) {
        if (x<2) return x;
        int left = 1, right = x/2;
        int ans = 0;
        int mid;
        while (left <= right){
            mid = (left + right) / 2;
            if (x / mid == mid){
                ans = mid;
                break;
            } else if (x / mid < mid) {
                right = mid - 1;
            } else{
                ans = mid;
                left = mid + 1;
            }
        }
        return ans;
    }
};