#include<bits/stdc++.h>
using namespace std;

int removeDuplicates(vector<int>& nums)
{
    int i = 1;
    int prev = nums[0];
    for(int j = 1; j < nums.size() ; j++)
    {
        if(nums[j] != prev)
        {
            prev = nums[j];
            nums[i] = nums[j];
            i++;
        }
    }
    return i;
}

int main()
{
    int n;
    cin >> n;

    vector<int> arr(n);
    for(int i=0; i<n; i++) cin >> arr[i];

    int ans = removeDuplicates(arr);
    cout << ans << endl;


}
