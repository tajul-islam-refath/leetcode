#include<bits/stdc++.h>
using namespace std;

vector<vector<int>> per;
void generatePerm(vector<int> &perm, int start,int e)
{

    if(start == e){
        per.push_back(perm);
    }else{

        for(int i = start; i<= e; i++){
            swap(perm[start] , perm[i]);
            generatePerm(perm , start+1 , e);
            swap(perm[start] , perm[i]);
        }

    }


}

int main()
{
    int n;
    cin >> n;

    vector<int> arr(n);
    for(int i=0; i<n; i++) cin >> arr[i];

    permute(arr ,0 , n-1);
    cout << per.size() << endl;

}
