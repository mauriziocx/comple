#include<iostream>
#include<conio.h>
#include<fstream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

typedef pair<int, int>iPair;	
int *p,*rank1;
int FindSet(int *&p, int i) {
	if (p[i] == i)
		return i;
	else
		return FindSet(p, p[i]);
}
void pathcompression(int *&p, int i) {
	int x = FindSet(p, i);
	p[i] = x;
}
bool IsSameSet(int p[], int i, int j) {
	int x = FindSet(p, i);
	int y = FindSet(p, j);
	return x == y;
}
void UnionSet(int *&p, int i, int j, int *&rank) {
	int x = FindSet(p, i);
	pathcompression(p, i);
	int y = FindSet(p, j);
	pathcompression(p, j);

	if (x != y)
	{
		if (rank[x] > rank[y]) {
			p[y] = x;

		}
		else {
			p[x] = y;
			if(rank[x]==rank[y])
				rank[y]++;
		}
		
		

	}
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
int main() {
	int n,m;
	int i=0;
	ifstream read;
	ofstream write;
	string line; 
	vector<pair<int,iPair>>edges;

	
	read.open("input.txt");
	while (!read.eof())
	{
		if (i == 0)
		{
			getline(read, line);
			vector<int> v{ explode(line, ' ') };
			n = v[0];
			m = v[1];          
			p = new int[n];
			rank1 = new int[n];
			for (int i = 0; i < n; i++)
			{
				p[i] = i;
				rank1[i] = 0;
			}	
			
			
		
		}
		else {
			getline(read,line);
			vector<int> v1{ explode(line, ',') };
			edges.push_back({ v1[0], {v1[1],v1[2]} });
		}
	
		i++;


	}
	read.close();

	sort(edges.begin(),edges.end());
	for (int i = 0; i < m; i++)
	{
		UnionSet(p,edges[i].second.first, edges[i].second.second,rank1);
		
	}
	 
	write.open("output.txt");
	for(int i=0;i<n;i++)
		write << i<< p[i]<< rank1[i]<< endl;
	write.close();
		
		
	
	
	_getch();



}


