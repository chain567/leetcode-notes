/*
class Solution {
public:
    int climbStairs(int n) {
        if (n == 1){
            return 1;
        } else if (n == 2){
            return 2;
        } else {
            return climbStairs(n-1) + climbStairs(n-2);
        }
    }
};
*/
// C++ learning -> Using these Easy problems to practice C++ syntax.
class Solution {
    int lib[46] = {0};
public:
    int climbStairs(int n) {
        if (n == 1){
            return 1;
        } else if (n == 2){
            return 2;
        } else {
            if (lib[n]) return lib[n];
            return lib[n] = climbStairs(n-1) + climbStairs(n-2);
        }
    }
};