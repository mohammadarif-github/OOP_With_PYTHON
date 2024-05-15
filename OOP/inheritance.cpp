#include <bits/stdc++.h>

using namespace std;

class Grandpa
{
public:
    Grandpa(string grandpa_name) : grandfather_name(grandpa_name) {}

    string grandfather_name;
};

class Father : public Grandpa
{
public:
    Father(string father_name, string grandpa_name)
        : Grandpa(grandpa_name), father_name(father_name) {}

    string father_name;
};

class Son : public Father
{
public:
    Son(string name, string father_name, string grandfather_name)
        : Father(father_name, grandfather_name), name(name) {}

    void show_details()
    {
        cout << "I am " << name << ", son of Mr. " << father_name
             << ". My grandfather's name is: " << grandfather_name << endl;
    }

private:
    string name;
};

int main()
{
    Son good_son("Mohammad", "Kamal", "Jamal");
    good_son.show_details();

    return 0;
}
