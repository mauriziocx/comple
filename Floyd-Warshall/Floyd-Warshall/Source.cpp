#include<stdio.h>
#include<iostream>
#include<conio.h>
#include<fstream>
#include<string>
#include<vector>
#define V 4
#define INF 99999
using namespace std;
void print(int dist[][V]) {
	printf("Distancia mas corta entre pares de Vertices \n");
	for (int i = 0;i < V;i++) {
		for (int j = 0;j < V;j++) {
			if (dist[i][j] == INF)
				printf("%7s", "INF");
			else
				printf("%7d",dist[i][j]);
		}
		printf("\n");
	}
}

void floydWarshell(int graph[][V]) {
	int dist[V][V],i ,j,k ;
	for (i = 0;i < V;i++)
		for (j = 0;j < V;j++)
			dist[i][j] = graph[i][j];

	for (k = 0;k < V;k++) {
		for (i = 0;i < V;i++) {
			for (j = 0;j < V;j++){
				if (dist[i][k] + dist[k][j] < dist[i][j])
					dist[i][j] = dist[i][k] + dist[k][j];
				}
			}
		}
	print(dist);
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
	ifstream read;
	ofstream write;
	string line;
	int c;
	read.open("input.txt");
	getline(read, line);
	c = stoi(line);
	
	while (!c==0)
	{
		int n, m;
		getline(read, line);
		n = stoi(line);
		getline(read, line);
		m = stoi(line);
		int **graph;
		graph = new int*[n];
		while (!m == 0)
		{			
			getline(read, line);
			vector<int> ex{explode(line,' ')};
			ex[0][];
			m--;
		}
		
		getline(read, line);
		c--;
	}
	read.close();
	write.open("output.txt");

	write.close();
	int graph[V][V] = { {0,5,INF,10} ,
	{INF,0,3,INF},
	{INF,INF,0,1},
	{INF,INF,INF,0}
	};
	floydWarshell(graph);
	_getch();
	return 0;
}