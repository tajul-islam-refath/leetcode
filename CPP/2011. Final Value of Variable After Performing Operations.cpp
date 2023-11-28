#include<bits/stdc++.h>
using namespace std;

int finalValueAfterOperations(vector<string>& operations)
{
    int x = 0;

    for(int i=0; i<operations.size(); i++)
    {
        if(operations[i] == "++X")
        {
            ++x;
        }
        else if(operations[i] == "X++")
        {
            x++;
        }
        else if(operations[i] == "--X")
        {
            --x;
        }
        else
        {
            x--;
        }
    }

    return x;
}

int main()
{
    int n;
    cin >> n;

    vector<string> arr(n);
    for(int i=0; i<n; i++) cin >> arr[i];

    int ans = finalValueAfterOperations(arr);
    cout << ans;

}


