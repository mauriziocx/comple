#include<iostream>
#include<conio.h>
#include<string>
#include<sstream>
using namespace std;

void ordenar(int *arr,int n) {
	for (int i = 0; i <= n; i++) {
	 
	}
	
}
bool palindromo(string n) {
	for (int i = 0; i < n.size();i++) {
		for (int j = n.size();j>=0;j--) {
			if (n[i] == n[j])
				return true;
			else
				return false;
		}
	}

}

int binario(string n) {
	int i = 1;
	int res = 0;
	
	for (int j = n.size()-1; j >= 0; j--) {
		int y;
		stringstream s;
		s << n[j] ;
		s >> y;
		if (y == 1) {
			
			res += i;
		}
			
		i *= 2;
		
	}
	return res;
}
	
	/*
int main() {
	int arr[]={5,9,4,3};
	int n = (sizeof(arr) / sizeof(arr[0]))-1;

	ordenar(arr,n);
}
*/
/*
int main() {
	string n ;
	cin >>n;
	if (palindromo(n))
		cout << "es palindromo";
	else
		cout << "no es";

	
	_getch();
	return(0);

}*/
int main() {
	string n;
	cin >> n;
	
	 cout<<binario(n);
	_getch();
	return (0);
}