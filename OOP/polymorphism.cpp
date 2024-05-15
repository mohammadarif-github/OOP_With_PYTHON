#include <bits/stdc++.h>

using namespace std;

class Vehicle
{
public:
    virtual void fare() const = 0;
};

class Aeroplane : public Vehicle
{
private:
    string going_to;
    int distance;

public:
    Aeroplane(string destination, int dis) : going_to(destination), distance(dis) {}

    void fare() const override
    {
        cout << "Your flight costs around: " << distance * 100 << endl;
    }
};

class Bus : public Vehicle
{
private:
    string going_to;
    int distance;

public:
    Bus(string destination, int dis) : going_to(destination), distance(dis) {}

    void fare() const override
    {
        cout << "Your bus fare costs around: " << distance * 30 << endl;
    }
};

class Taxi : public Vehicle
{
private:
    string going_to;
    int distance;

public:
    Taxi(string destination, int dis) : going_to(destination), distance(dis) {}

    void fare() const override
    {
        cout << "Your taxi fare costs around: " << distance * 10 << endl;
    }
};

int main()
{
    Aeroplane person_rich("Cox's Bazar", 150);
    Bus person_middle_class("Cox's Bazar", 150);
    Taxi person_poor_me("Cox's Bazar", 150);

    person_rich.fare();
    person_middle_class.fare();
    person_poor_me.fare();

    return 0;
}
