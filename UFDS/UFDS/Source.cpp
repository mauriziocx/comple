#include<iostream>
#include<conio.h>

using namespace std;
int FindSet(int p[],int i) {
	if (p[i]==i)
	return i;
	else 
		return FindSet(p,p[i]);
}
bool IsSameSet(int p[], int i,int j) {
	int x = FindSet( p, i);
	int y = FindSet( p, j);
	return x == y;
}
void UnionSet(int p[], int i, int j, int rank[]) {
	int x = FindSet(p, i);
	int y = FindSet(p, j);
	if (x != y)
	{
		if (rank[x] > rank[y])
			p[y] = x;
		else p[x] = y;

	}
}

	int main() {

		bool bandera = false;
		bool flag = false;
		int tecla;
		while (!flag) {
			int n;
			cout << "Ingrese numero de vertices:";
			cin >> n;
			int *p;
			p = new int[n];
			for (int i = 0; i < n; i++)
			{
				p[i] = i;
			}
			int *rank;
			rank = new int[n];
			for (int i = 0; i < n; i++)
			{
				rank[0] = 0;
			}
			while (!bandera)
			{
				cout << "Menu - UFDS" << endl;
				cout << "-----------" << endl << endl;
				cout << "\t1 .- Findset" << endl;
				cout << "\t2 .- Is same set" << endl;
				cout << "\t3 .- Union set" << endl;
				cout << "\t4 .- Salir" << endl << endl;
				cout << "Elije una opcion: ";

				cin >> tecla;

				switch (tecla)
				{
				case 1:
					int f;
					cout << "encontrar set de:";
					cin >> f;
					cout << FindSet(p, f) << endl;
					break;

				case 2:
					int f1;
					int f2;
					cout << "saber si tienen el mismo set:";
					cin >> f1;
					cin >> f2;
					if (IsSameSet(p, f1, f2) == true)
						cout << "si" << endl;
					else
						cout << "no" << endl;
					break;

				case 3:
					int f3;
					int f4;
					cout << "Unir:";
					cin >> f3;
					cin >> f4;
					UnionSet(p, f3, f4, rank);
					for (int i = 0; i < n; i++)
					{
						cout << i << " " << "p -> " << p[i] << endl;
					}
					break;


				case 4:
					bandera = true;
					break;

				default:
					cout << "Opcion no valida.\a\n";
					break;
				}
			}
		}

		_getch();



	}


