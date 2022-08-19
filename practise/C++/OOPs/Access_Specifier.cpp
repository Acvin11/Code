#include <iostream>

using namespace std;
class Employee
{
    private: 
        int a,b,c;
    public:
    
        int d,e;
        void setData(int a1, int b1, int c1);
        void getData()
        {
            std::cout<<"\n a \t"<<a;
            std::cout<<"\n b \t"<<b;
            std::cout<<"\n c \t"<<c;
            std::cout<<"\n d \t"<<d;
            std::cout<<"\n e \t"<<e;
        }    
};

void Employee::setData(int a1, int b1, int c1)
{
    a=a1;
    b=b1;
    c=c1; 
}    

int main()
{
    Employee harry;
    harry.d =1123;
    harry.e =1123;
    harry.setData(1,2,3);
    
    harry.getData();
    cout<<"\n Hello World";

    return 0;
}
