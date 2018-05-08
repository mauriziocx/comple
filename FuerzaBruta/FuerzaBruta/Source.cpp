#include<iostream>
#include<time.h>
#include<conio.h>
#define max 5000
using namespace std;

class StringMatching {
public:
	void findMatch(char a[max], char b[max], int n, int m) {
		int k, i, j, band = 0;
		for (i = 0; i <= n - m; i++) {
			k = i; j = 0;
			while (a[k] == b[j] && j <= m) {
				k++; j++;
			}
				if (j == m ) {
					cout << "value at position=>" << i + 1 << endl; 
					band = 1;
				}
				
			}
			if (band == 0)
				cout << "value not found!!!.."<<endl;
		
	}
};
int main() {
	cout << "FB-Example01: String Match" << endl;
	char* a = (char*)"UPC, exigete, innova";
	char* b = (char*)"exigete";
	StringMatching* sm = new StringMatching();

	int n = 20;
	int m = 7;
	double beginTime = clock();
	sm->findMatch(a,b,n,m);
	double endTime = clock();
	int t = endTime - beginTime;

	cout << "Execution Time=>" << (double)t / ((double)CLOCKS_PER_SEC) << endl;
	cout << "string val=>" << a << endl;
	cout << "string key=>" << b << endl;
	_getch();
	return 0;

}