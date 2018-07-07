#include<iostream>		
using namespace std;
bool verificar(int j,int temp[],int k)
{
	int in=0;
	for (int i = 0; i < k; i++)
	{
		if (temp[i] == j)
			in = 1;
		}
	if (in == 1)
		return false;
	else
		return true;
	}
	
		


void Mochila(int n, int Peso[], int Valor[], int PMax) {
	int *a = new int[PMax];
	int *temp = new int[PMax];
	int aux;

	for (int i = 0; i <= PMax; i++) {
		a[i] = 0;
		temp[i] = -1;
	}

	a[0] = 0;
	for (int i = 1; i <= PMax; i++)
		for (int j = 1; j <= n; j++) {
			if (verificar(j, temp, i) == false)
				a[i] += Peso[j];
			if ((Peso[j] <= i) && (a[i] < a[i - Peso[j]] + Valor[j]) && (verificar(j, temp, i) == true)) {
				a[i] = a[i - Peso[j]] + Valor[j];
				temp[i] = j;
			}
		}

	aux = 1;
	int tempM=PMax;
	while ((aux<=PMax) && (temp[aux] != -1)) {
		
		cout << "Se agrego " << temp[aux]  << " ($" << Valor[temp[aux]] << ", " << Peso[temp[aux]] << "Kg) Espacio disponible: " << tempM- Peso[temp[aux]] << endl;
		
		aux += 1;
	}
	cout << "Valor total: $" << a[PMax] << endl;
	delete[] temp;
	delete[] a;
}

int main() {
	int n, PMax;
	cout << "Ingrese la cantidad de objetos: ";
	cin >> n;
	int *Peso = new int[n];
	int *Valor = new int[n];
	for (int i = 1; i<=n; i++) {
		cout << "Ingrese el Peso del objeto " << i << ": ";
		cin >> Peso[i];
		cout << "Ingrese el Valor del objeto " << i << ": ";
		cin >> Valor[i];
		cout << endl;
	}
	cout << "Ingrese el peso maximo de la mochila: ";
	cin >> PMax;
	cout << endl << "Calculando..." << endl;
	Mochila(n, Peso, Valor, PMax);
	system("pause");
	return 0;
}
/*
int max(int a, int b)
{
	return (a > b) ? a : b;
}

// Returns the maximum value that can be put in a knapsack of capacity W
int knapSack(int W, int wt[], int val[], int n)
{
	int i, w;
	int K[n + 1][W + 1];

	// Build table K[][] in bottom up manner
	for (i = 0; i <= n; i++)
	{
		for (w = 0; w <= W; w++)
		{
			if (i == 0 || w == 0)
				K[i][w] = 0;
			else if (wt[i - 1] <= w)
				K[i][w]
				= max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w]);
			else
				K[i][w] = K[i - 1][w];
		}
	}

	return K[n][W];
}

int main()
{
	cout << "Enter the number of items in a Knapsack:";
	int n, W;
	cin >> n;
	int val[n], wt[n];
	for (int i = 0; i < n; i++)
	{
		cout << "Enter value and weight for item " << i << ":";
		cin >> val[i];
		cin >> wt[i];
	}

	//    int val[] = { 60, 100, 120 };
	//    int wt[] = { 10, 20, 30 };
	//    int W = 50;
	cout << "Enter the capacity of knapsack";
	cin >> W;
	cout << knapSack(W, wt, val, n);

	return 0;
}*/