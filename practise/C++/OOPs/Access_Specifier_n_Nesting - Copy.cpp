#include <iostream>
#include <string>
using namespace std;
class Binary
{
    private: 
        string s = "1001";
        int n =s.length();
         void checkBin();
       
    public:
        void oneCompliment();
        void display();
};

void Binary::checkBin()
{
    for(int i=0; i<n ;i++)
    {
        if (s.at(i) != '0' && s.at(i) != '1')
        {
            cout << "\n Incorrect binary format" << endl;
            exit(0);
        }
    }
}    
void Binary::oneCompliment()
{
    checkBin();
    for(int i=0; i<n ;i++)
    {
        if (s.at(i) == '0')
        {
            s.at(i) = '1';
        }
        else
        {
            s.at(i) = '0';
        }
    }
    
    
}    

void Binary::display()
{
    std::cout<<"\n Final Output : "<<s<<endl;
}    


int main()
{
    Binary b;
    //b.checkBin();
    b.oneCompliment();
    b.display();
    
   
    return 0;
}
