#include<iostream>
#include<conio.h>

using namespace std;
#ifndef IGUALA23
#define IGUALA23

class Expresion  {
	int len;
	int*vec;
	bool solved, *flag;
public:
	Expresion() {
		int vic[] = { 2,3,7,5,11 };
		this->solved = false;
		//this->vec = new int[5];
		this->vec = vic;

		len = 5;// sizeof(this->vec) / sizeof(int);

	}
	int getsolved() { return this->solved; }

	void print() {
		if (solved)cout << "posible" << endl;
		else cout << "imposible" << endl;
	}

	void backtracking(int i = 0, int res = 0) {
		//cout << i << ", " << res << endl;
		if (this->solved)return;
		if (res == 23 && i >= len) {
			this->solved = true;
			return;
		}
		else if (i >= len)return;
		for (int j = 0; j < len; j++) {
			backtracking(i + 1, res + vec[j]);
			backtracking(i + 1, res - vec[j]);
			backtracking(i + 1, res * vec[j]);
		}

	}
};

#endif // !IGUALA23