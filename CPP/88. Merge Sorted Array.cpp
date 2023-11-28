#include<bits/stdc++.h>
using namespace std;

vector<int> merge(vector<int>& nums1, int m, vector<int>& nums2, int n)
{
    if(m !=0 && n != 0 )
    {

        vector<int> arr(m+1);
        vector<int> arr1(n+1);

        for(int c=0; c<m; c++) arr[c] = nums1[c];
        for(int c=0; c<n; c++) arr1[c] = nums2[c];

        arr[m] = INT_MAX;
        arr1[n] = INT_MAX;

        int i = 0, j=0;
        vector<int> ans(m+n);
        int len = m+n;

        for(int k=0; k<len; k++)
        {
            if(arr[i] > arr1[j])
            {
                ans[k] = arr1[j];
                j++;
            }
            else
            {
                ans[k] = arr[i];
                i++;
            }
        }

        for(int k=0; k<len; k++)
        {
            nums1[k] = ans[k];
        }
    }
    else if(m == 0)
    {
        nums1 = nums2;
    }

    return nums1;
}

int main()
{
    int n, m, k;
    cin >> n >> m >> k;
    vector<int> num1(k);
    vector<int> num2(n);

    for(int i=0; i<k; i++) cin >> num1[i];
    for(int i=0; i<n; i++) cin >> num2[i];

    vector<int> ans = merge(num1,m, num2, n);

    for(int i=0; i< ans.size() ; i++) cout << ans[i] << " ";

}
