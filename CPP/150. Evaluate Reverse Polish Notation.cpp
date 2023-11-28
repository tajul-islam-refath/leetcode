#include<bits/stdc++.h>
using namespace std;


int evalRPN(vector<string>& tokens)
{
    int res = 0;
    stack<int> stack;
    int num1 , num2;
    for(int i=0; i<tokens.size(); i++)
    {
        if(tokens[i] == "+")
        {
            num2 = stack.top();
            stack.pop() ;
            num1 = stack.top();
            stack.pop() ;
            res = num2 + num1;
            stack.push(res);

        }
        else if(tokens[i] == "-")
        {

            num2 = stack.top();
            stack.pop() ;
            num1 = stack.top();
            stack.pop() ;
            res = num1 - num2;
            stack.push(res);

        }
        else if(tokens[i] == "*")
        {

            num2 = stack.top();
            stack.pop() ;
            num1 = stack.top();
            stack.pop() ;
            res = num2 * num1;
            stack.push(res);

        }
        else if(tokens[i] == "/")
        {
            num2 = stack.top();
            stack.pop() ;
            num1 = stack.top();
            stack.pop() ;
            res = (int) num1 / num2;
//            cout << num1 << " " << num2 << " " <<  res << endl;
            stack.push(res);
        }
        else
        {
            int token = stoi(tokens[i]);
            stack.push(token);
        }
    }

    return stack.top();
}

int main()
{

    int n;
    cin >> n;

    vector<string> arr(n);
    for(int i=0; i<n; i++) cin >> arr[i];

    int res = evalRPN(arr);
    cout << res << endl;


}
