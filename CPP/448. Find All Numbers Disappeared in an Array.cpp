#include<bits/stdc++.h>
using namespace std;

vector<int> findDisappearedNumbers(vector<int>& nums)
{
    int n = nums.size();

    map<int,int> arr;
    vector<int> ans;

    for(int i=0; i<n; i++)
    {
        arr[nums[i]] = 1;
    }


    for(int i=1; i<=n; i++)
    {
        cout << arr[i] << endl;
        if(arr[i] == 0)
        {
            ans.push_back(i);
        }
    }

    return ans;
}

int main()
{
    int n;
    cin >> n;

    vector<int> arr(n);
    for(int i=0; i<n; i++) cin >> arr[i];

    vector<int> ans = findDisappearedNumbers(arr);

    for(int i=0; i< ans.size() ; i++) cout << ans[i] << " ";

}


