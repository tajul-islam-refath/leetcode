#include<bits/stdc++.h>
using namespace std;


int calculate(string &s)
{

    int res =0;
    stack<string> ex;
    stack<string> c;

    string st;
    for(int i=0; i<s.size(); i++)
    {
        if(s[i] == '+' || s[i] == '-' || s[i] == '*' || s[i] == '/')
        {
            st = s[i];
            ex.push(st);
        }
        else if(s[i] == ' ')
        {
            continue;
        }
        else
        {
            st = s[i];
            c.push(st);
        }
    }

    int num1;
    int num2;


    while(!ex.empty())
    {

        if(ex.top() == "+")
        {
            num2 =  stoi(c.top());
            c.pop();
            num1 = stoi(c.top());
            c.pop();
            res = num1 + num2;
            c.push(to_string(res));
            ex.pop();
        }
        else if(ex.top() == "-")
        {
            num2 = stoi(c.top());
            c.pop();
            num1 = stoi(c.top());
            c.pop();
            res = num1 - num2;
            c.push(to_string(res));
            ex.pop();
        }
        else if(ex.top() == "*")
        {
            num2 = stoi(c.top());
            c.pop();
            num1 = stoi(c.top());
            c.pop();
            res = num1*num2;
            c.push(to_string(res));
            ex.pop();
        }
        else
        {
            num2 = stoi(c.top());
            c.pop();
            num1 = stoi(c.top());
            c.pop();
            res = num1 / num2;
            c.push(to_string(res));
            ex.pop();
        }
    }


    return res;
}

int main()
{

    string s;
    cin >> s;

    int res = calculate(s);
    cout << res << endl;


}

