#include<iostream>
#include<cstdio>
#include<climits>
#include<conio.h>
#include<vector>
using namespace std;
typedef struct {
	int u, v, w;
} Edge;

const int NODES = 5;
int EDGES;
Edge edges[32];
int d[32];
vector<int> nav;
#define INFINITY INT_MAX

void showVectors(int *vec, int num) {
	printf("\n");
	for (int i = 0; i < num; i++) {
		printf("%d: %d\n", i, *(vec + i));
	}
}
void BellmanFord(int src,int dest) {
	for (int i = 0; i < NODES; i++) {
		d[i] = INFINITY;
	}
	d[src] = 0;

	for (int i = 0; i < NODES; i++) {
		for (int j = 0; j < EDGES; j++) {
			if (d[edges[j].u] + edges[j].w < d[edges[j].v]) {
				if (edges[j].v == dest)
					nav.push_back(edges[j].u);
				d[edges[j].v] = d[edges[j].u] + edges[j].w;
			}
		}
	}
	for (int i = 0; i < NODES; i++) {
		for (int j = 0; j < EDGES; j++) {
			if (d[edges[j].u] + edges[j].w < d[edges[j].v]) {
				printf("Graph contains a negative-weigth cycle\n");
			}
		}

	}
}
	int main() {
		
		int w, k = 0;
/*		freopen("int.txt","rt",stdin);
		freopen("out.txt", "wt", stdout);*/
		int mat[5][5] = {
			{0,6,0,7,0},
			{0,0,5,8,-4},
			{0,-2,0,0,0},
			{0,0,-3,0,9},
			{2,0,7,0,0}
		};

		for (int i = 0; i < 5; i++) {
			for (int  j= 0; j < 5; j++) {			
				
				if (mat[i][j]!= 0) {
					edges[k].u = i;
					edges[k].v = j;
					edges[k].w = mat[i][j];
					k++;
				}
			}
		}

		EDGES = k;
		int source = 0;
		BellmanFord(source,4);

		printf("\nNode\tDistancia\n");
		printf("----\t------\n");
		for (int i = 0;i<NODES;i++) {
			printf("%d\t\t\t%d\n",i,d[i]);
		}
		for (int i = 0; i < nav.size(); i++)
		{
			cout << nav[i]<<",";
		}
		_getch();		
		return 0;
	}