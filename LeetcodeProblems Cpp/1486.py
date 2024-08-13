class Solution {
public:
    int xorOperation(int n, int start) {
        std::vector<int> arr;
        int ans = 0;
        for (int i = 0; i < n; i++) {
            int num = start + 2 * i;
            ans ^= num;
        }
        
        return ans;
    }
};