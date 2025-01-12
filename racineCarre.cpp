#include <iostream>
using namespace std;

 int main() 
 {
    int  nbre1, nbre2 ,nbre3, maximum;
    cout <<"entrez trois nombre entier naturel:"<< endl;
    cin >>nbre1 >> nbre2 >> nbre3;
 
    if(nbre1<nbre2 && nbre2<nbre3){ 
        maximum = nbre3;
        cout <<"le maximum est:"<< endl;
        cout << maximum<<endl;
    }
    else if (nbre1>nbre2 &&  nbre2>nbre3){
        maximum=nbre2;
        cout <<"le maximum est:"<< endl;
        cout << maximum<<endl;
    }


    else if (nbre2>nbre3){
        maximum=nbre2;
        cout <<"le maximum est:"<< endl;
        cout << maximum<<endl;

    }


    
    else {
        maximum=nbre1;
        cout <<"le maximum est:"<< endl;
        cout << maximum<<endl;
    }

return 0;


 }