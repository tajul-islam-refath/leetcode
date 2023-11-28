#include<bits/stdc++.h>
using namespace std;

 vector<int> buildArray(vector<int>& nums) {
        vector<int> ans;
        int length = nums.size();

        for(int i=0; i<length; i++){
            ans.push_back(nums[nums[i]]);
        }

        return ans;

}

int main(){
    int n;
    cin >> n;

    vector<int> arr(n);
    for(int i=0; i<n; i++) cin >> arr[i];

    vector<int> ans = buildArray(arr);

    for(int i=0; i< ans.size() ; i++) cout << ans[i] << " ";

}
