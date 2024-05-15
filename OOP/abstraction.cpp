#include <bits/stdc++.h>

using namespace std;

class example
{
private:
    int data;

public:
    void set_data(int value)
    {
        data = value;
    }

    void get_data()
    {
        cout << "Data: " << data << endl;
    }
};

int main()
{
    example obj;
    obj.set_data(12);
    obj.get_data();

    return 0;
}
