class Solution {
public:
    bool hasIncreasingSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        for(int i = 0; i < n; i++){
            //  if(n ==2 && k==1) return true;
            if(i+2*k>n) break;
           
            bool first = true;
            bool second = true;
            for(int j = 1; j < 2 * k; j++){
                if(j+i >= nums.size()) continue;
                
                if(j < k && j!=k){
                    if(nums[i+j-1] >= nums[i+j]){
                        first = false;
                        break;
                    }
                }else if(j > k){
                    if(nums[i+j-1] >= nums[i+j]){
                        second = false;
                        break;
                    }
                }
            }

            if (first && second) return true;
        }
        return false;
    }
};