#include<iostream>
#include"finder.h"
#include<conio.h>

using namespace std;

int main() {
	int a[] = {34,3,47,91,32,0};
	Finder* f = new Finder();
	int n = sizeof(a) / sizeof(int);
	cout << "n=> " << n
		<< " Max Value: "
		<< f->maxValue(a,0,n) << endl;	
	_getch();
	return(0);

}