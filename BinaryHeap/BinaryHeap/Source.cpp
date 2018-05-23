#include<iostream>
#include<conio.h>
#include<vector>
#include<string>
#pragma once
#define MAX 1000
using namespace std;


void parentorder(int p[],vector<int>&A) {
	for (int i = 0; i < A.size(); i++)
	{
		if (i == 0)
			p[0] = A[0];
		else
		{
			int pr = abs((i - 1) / 2);
			p[i] = A[pr];
		}

	}
}
void order(int n, vector<int>&A) {
	
	int k = abs((n - 1) / 2);
	for (int j = n;j>=1;j--) {
		if (A[k] < A[n])
		{
			swap(A[n], A[k]);
		
		}	
		n--;
		k = abs((n - 1) / 2);
		
	}

}
template <class T>
void insertar(T a, vector<int>&A,int n,int p[])
{
	A.push_back(a);
	order(n,A);
	parentorder(p,A);
}
void crear(vector<int> v, vector<int>&A,int p[])
{
	for (int i = 0; i < v.size(); i++)
		insertar(v[i], A,i,p);
}
const vector<int> explode(const string& s, const char& c)
{
	string buff{ "" };
	vector<int> v;

	for (auto n : s)
	{
		if (n != c) buff += n; else
			if (n == c && buff != "") { v.push_back(stoi(buff)); buff = ""; }
	}
	if (buff != "") v.push_back(stoi(buff));

	return v;
}
void extractMax(vector<int>&A, int p[]) {
	int n = A.size() - 1;
	swap(A[0], A[n]);
	A.erase(A.begin()+n);
	n = A.size() - 1;
	order(n,A);
	parentorder(p,A);
}
void DeleteKey(int i,vector<int>&A,int p[])
{
	int min = INT32_MAX;
    A[i] = 99;
	order((A.size() - 1),A);
	parentorder(p, A);
	extractMax(A,p);

}
int main()
{
	string a;
	cout << "crear arbol:";
	getline(cin, a);
	vector<int> v{ explode(a, ',') };
	vector<int>A;
	int *p;
	p = new int[v.size() - 1];

	for (int i = 0; i < v.size(); i++)
	{
		if (i == 0)
			p[0] = v[0];
		else
		{
			int pr = abs((i - 1) / 2);
			p[i] = v[pr];
		}

	}

	crear(v, A, p);
	for (int i = 0; i < A.size(); i++)
		cout << A[i] << " p ->" << p[i] << endl;
	//--- insertar
	/*
    int n;
	cout << "insertar:";
	cin >> n;
	insertar(n,A, A.size(),p);
	cout << A.size()<< endl;
	
	for (int i = 0; i <5; i++)
		cout << A[i] << " p ->" << p[i] << endl;*/
	// ---- extractmax
	/*
	extractMax(A,p);
	for (int i = 0; i < A.size(); i++)
		cout << A[i] << " p ->" << p[i] << endl;*/
	//---- delete key
	int k;
	cout << "borrar:";
	cin >> k;
	DeleteKey(k,A,p);
	for (int i = 0; i < A.size(); i++)
		cout << A[i] << " p ->" << p[i] << endl;
	_getch();
}