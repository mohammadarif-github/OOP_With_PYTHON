#include <bits/stdc++.h>
using namespace std;




class Number
{
public:
   int a, b;




   void getValue(int x, int y)
   {
       a = x;
       b = y;
   }




   Number operator+(Number obj)
   {
       Number result;
       result.a = a + obj.a;
       result.b = b + obj.b;
       return result;
   }
};




int main()
{
   Number ob_1, ob_2, ob_3;
   ob_1.getValue(1, 4);
   ob_2.getValue(2, 5);
   ob_3.getValue(3, 6);
   Number ans = ob_1 + ob_2 + ob_3;
   cout << ans.a << " " << ans.b << endl;




   return 0;
}
