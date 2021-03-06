// Online C++ compiler to run C++ program online
#include <iostream>
int sum( int a, float b , char c)
{
    std::cout<<"\n a= "<<a;
    std::cout<<"\t b= "<<b;
    std::cout<<"\t c= "<<c<<"\n";
    float d =  a+b+"+"+c;
    std::cout<<"\t d= "<<d<<"\n";
   
    return d;    
}
int sum( int a, int b)
{
    return a+b;    
}


int main() {
    // Write C++ code here
    std::cout << "Hello world!";
    float a,b,c,r,v;
    v = sum(3,4);
    std::cout<<"\n v= "<<v;
   std::cout << "\n --------------- \n";
    
    r = sum(3.9,5.6,0.1);
    std::cout<<"\n r= "<<r;
    
    return 0;
}