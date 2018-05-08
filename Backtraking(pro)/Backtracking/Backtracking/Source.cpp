//bt-Backtraking: 
#include<iostream>
#include<ctime>
#include<conio.h>
#include<String>

#define max 5000
using namespace std;

class StringMatchingBT {
public:

	bool checkSubString(char* a, char *b,  int m) {	
		int k=0;
		bool res = false;
		int posa = 0;
		int posb = 0;
		while (res == false) {
			
			
			for ( posa,  posb ; posa < m, posb < m; posa++, posb++) {
				if (a[posa] == b[posb])
					k++;
				if (k == m)
					res = true;
			}
			posa = posa - m;
			posb = posb - m;
			posa++;
		}
		//
		return(res);

	}
	/*
	bool match(char *a, char *b, int n, int m) {
		if (a[n] == b[m]) return n;
		int p = match(a, b, n, m);
		return checkSubString(a, b, n, m, p);

	}*/

	void test(char *first, char *second, int n, int m) {
		checkSubString(first,second,m) ? cout << "Exist" : cout << "Not found";
	}

};


int main() {
	cout << "BT-Example02: String Match " << endl;
	char* f = (char*)"UPC, exigete, innova"; //20
	char* s = (char*)"exigete";//7
	StringMatchingBT* smbt = new StringMatchingBT();

	double beginTime = clock();
	smbt->test(f, s, 20, 7);
	double endTime = clock();
	int t = endTime - beginTime;

	cout << "Execution Time=> " << (double)t / ((double)CLOCKS_PER_SEC) << endl;
	cout << "string val => " << f << endl;
	cout << "string key => " << s << endl;

	cin.get();
	cin.get();

	return 0;
}