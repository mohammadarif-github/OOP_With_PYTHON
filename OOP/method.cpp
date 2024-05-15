#include <bits/stdc++.h>

using namespace std;

class A
{
private:
   int value;

public:
   void set_value(int v)
   {
      value = v;
   }

   void show_value()
   {
      cout << "The value is: " << value << endl;
   }
};

int main()
{
   A obj;
   obj.set_value(10);
   obj.show_value();
   return 0;
}
