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
vector<int> Objetivos;
int num;
#define INFINITY INT_MAX

void showVectors(int *vec, int num) {
	printf("\n");
	for (int i = 0; i < num; i++) {
		printf("%d: %d\n", i, *(vec + i));
	}
}
void BellmanFord(int src) {
	for (int i = 0; i < NODES; i++) {
		d[i] = INFINITY;
	}
	d[src] = 0;

	for (int i = 0; i < NODES; i++) {
		for (int j = 0; j < EDGES; j++) {
			if (d[edges[j].u] + edges[j].w < d[edges[j].v]) {
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
		freopen("in.txt","rt",stdin);
		freopen("out.txt", "wt", stdout);
		
		for (int i = 0; i < NODES; i++) {
			for (int  j= 0; j < NODES; j++) {
				scanf("%d", &w);
				if (w!= 0) {
					edges[k].u = i;
					edges[k].v = j;
					edges[k].w = w;
					k++;
							}
						}
					}	
		/*
		int mat[5][5] = {
			{0,6,0,7,0},
			{0,0,5,8,-4},
			{0,-2,0,0,0},
			{0,0,-3,0,9},
			{2,0,7,0,0}
		};

		for (int i = 0; i < NODES; i++) {
			for (int  j= 0; j < NODES; j++) {			
				
				if (mat[i][j]!= 0) {
					edges[k].u = i;
					edges[k].v = j;
					edges[k].w = mat[i][j];
					k++;
				}
			}
		}*/

		EDGES = k;
		

		int source = 0;
		BellmanFord(source);
		printf("\nNode\tDistancia\n");
		printf("----\t------\n");
		for (int i = 0;i<NODES;i++) {
			printf("%d\t\t\t%d\n",i,d[i]);
		}
		
		return 0;
	}