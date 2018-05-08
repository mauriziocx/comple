#include<iostream>
#include"adder.h"
#include<conio.h>
using namespace std;

int main() {
	int arr[] = {-2,-3,4,-1,-2,1,5,-3};
	int n = sizeof(arr) / sizeof(arr[0]);
	Adder* a = new Adder();
	int max_sum = a->maxSubArraySum(arr,0,n);
		cout << "Maximum contiguous Array Sum is " << max_sum;

		_getch();
		return 0;
}