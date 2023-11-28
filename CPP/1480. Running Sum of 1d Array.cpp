#include<bits/stdc++.h>
using namespace std;

vector<int> runningSum(vector<int>& nums)
{
    int sum = 0;
    vector<int> ans;

    int n = nums.size();
    for(int i=0; i<n; i++)
    {
        sum += nums[i];
        ans.push_back(sum);
    }

    return ans;
}

int main()
{
    int n;
    cin >> n;

    vector<int> arr(n);
    for(int i=0; i<n; i++) cin >> arr[i];

    vector<int> ans = runningSum(arr);

    for(int i=0; i< ans.size() ; i++) cout << ans[i] << " ";

}

