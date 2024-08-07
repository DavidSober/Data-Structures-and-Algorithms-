class Solution {
public:
    int minMovesToSeat(vector<int>& seats, vector<int>& students) {
        // sol is just abs diff for the sorted lists summed
        std::sort(seats.begin(), seats.end());
        std::sort(students.begin(), students.end());
        int ans = 0;
        for (int i = 0; i < seats.size(); i++) {
            ans += std::abs(seats[i] - students[i]);
        }
        return ans;
    }
};