#include <bits/stdc++.h>
using namespace std;

class Number
{
public:
    int a, b;

    void set_value(int x, int y)
    {
        a = x;
        b = y;
    }

    friend Number operator+(Number obj_1, Number obj_2);
};

Number operator+(Number obj_1, Number obj_2)
{
    Number res;
    res.a = obj_1.a + obj_2.a;
    res.b = obj_1.b + obj_2.b;
    return res;
}

int main()
{
    Number ob1, ob2, ob3;
    ob1.set_value(1, 2);
    ob2.set_value(3, 4);
    ob3.set_value(5, 6);
    Number ans = ob1 + ob2 + ob3;
    cout << ans.a << " " << ans.b << endl;

    return 0;
}
