#include<iostream>
#include<vector>
#include<queue>
#include<conio.h>
 

using namespace std;

void agregar(int v, vector<vector<int>> G, vector<vector<int>> In, vector<vector<int>> Gr,int j)
{
	for (int i = 0; i < G[v].size(); i++)
	{
		int a = G[v][i];
		for (int r = 0; r < Gr[j].size(); r++){
			if (!(Gr[j][r] == a)) {
				Gr[j].push_back(a);
				agregar(a, G, In, Gr, j);
			}
		}
	}

	for (int i = 0; i < In[v].size(); i++)
	{
		int b = In[v][i];
		for (int r = 0; r < Gr[j].size(); r++) {
			if (!(Gr[j][r] == b)) {
				Gr[j].push_back(b);
				agregar(b, G, In, Gr, j);
			}
		}
		
	}
}
int main() {
	int c;
	cin >> c;
	for (int i = 0; i < c; i++) {
		int n, m; //# of vertex, # of edges
		cout << "n m?" << endl;
		cin >> n >> m;
		queue<int> q;
		//----------
		int* incoming;
		incoming = new int[n];
		for (int i = 0; i < n; i++) {
			incoming[i] = 0;
		}
		//----------    
		vector<vector<int>> G(n);
		vector<vector<int>> Gr(3);
		vector<vector<int>> In(n);

		//----------    
		int u, v;
		for (int i = 0; i < m; i++) {
			cout << (i + 1) << ": (u -> v)?: ";
			cin >> u >> v;
			incoming[v]++;
			
			G[u].push_back(v);
			In[v].push_back(u);
		}

		for (int i = 0; i < n; i++) {
			if (incoming[i] == 0)
				q.push(i);
		}

		
		//-----------------------
		//Topological Order
		//-----------------------    
		for (int j = 0; j < q.size(); j++)
		{
          while (!q.empty()) {
			int u = q.front(); q.pop();
			Gr[j].push_back(u);
			for (int i = 0; i < G[u].size(); i++) {
				int v = G[u][i];
				Gr[j].push_back(v);
				agregar(v,G,In,Gr,j);			
				}

			}
		  
		}
		for (int i = 0; i < Gr.size(); i++)
		{
			for (int j = 0; j < Gr[i].size(); j++)
				cout << Gr[i][j];
			cout << endl;
		}
		
		//-----------------------    
	}
	_getch();
	return(0);
}