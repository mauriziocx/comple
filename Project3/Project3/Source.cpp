#include<iostream>
#include<vector>

using namespace std;

typedef pair<int, int>iPair;
void ordenar(vector<pair<int, iPair>>&obj)
{
	pair<int, iPair>aux;
	for (int i = 0; i<obj.size(); i++)
		for (int j = i + 1; j<obj.size(); j++)

			if (obj[i].second.first>obj[j].second.first) {
				aux = obj[i];
				obj[i] = obj[j];
				obj[j] = aux;

			}
}
void heapify(vector<pair<int, iPair>>&obj, int n, int i)
{
	int largest = i;  // Initialize largest as root
	int l = 2 * i + 1;  // left = 2*i + 1
	int r = 2 * i + 2;  // right = 2*i + 2

						// If left child is larger than root
	if (l < n && obj[l].second.first> obj[largest].second.first)
		largest = l;

	// If right child is larger than largest so far
	if (r < n && obj[r].second.first > obj[largest].second.first)
		largest = r;

	// If largest is not root
	if (largest != i)
	{
		swap(obj[i], obj[largest]);

		// Recursively heapify the affected sub-tree
		heapify(obj, n, largest);
	}
}
void heapSort(vector<pair<int, iPair>>&obj, int n)
{
	// Build heap (rearrange array)
	for (int i = n / 2 - 1; i >= 0; i--)
		heapify(obj, n, i);

	// One by one extract an element from heap
	for (int i = n - 1; i >= 0; i--)
	{
		// Move current root to end
		swap(obj[0], obj[i]);

		// call max heapify on the reduced heap
		heapify(obj, i, 0);
	}
}
bool verificar(int j, int temp[], int k)
{
	int in = 0;
	for (int i = 0; i <= k; i++)
	{
		if (temp[i] == j)
			in = 1;
	}
	if (in == 1)
		return false;
	else
		return true;
}




void Mochila(int n, int Peso[], int Valor[], int indice[], int PMax) {
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
			int sum = 0;
			if ((Peso[j] <= i) && (a[i] < a[i - Peso[j]] + Valor[j]) && (verificar(j, temp, i) == true)) {
				a[i] = a[i - Peso[j]] + Valor[j];
				temp[i] = j;
			}
			for (int k = 1; k <= n; k++) {
				if (verificar(k, temp, i) == false)
				{
					sum += Valor[k];
					a[i + 1] = sum;
				}
			}

		}

	aux = PMax;
	int tempM = PMax;
	while ((aux <= PMax) && (aux>0)) {
		if (temp[aux] != -1) {
			cout << "Se agrego " << indice[temp[aux]] << " ($" << Valor[temp[aux]] << ", " << Peso[temp[aux]] << "Kg) Espacio disponible: " << tempM - Peso[temp[aux]] << endl;
			tempM -= Peso[temp[aux]];
			aux -= Peso[temp[aux]];
		}
		else
			aux -= 1;

	}
	cout << "Valor total: $" << a[PMax] << endl;
	delete[] temp;
	delete[] a;
}

int main() {
	int n, PMax;

	vector<pair<int, iPair>>objetos;
	cout << "Ingrese la cantidad de objetos: ";
	cin >> n;
	int *Peso = new int[n];
	int *Valor = new int[n];
	int *indice = new int[n];

	for (int i = 1; i <= n; i++) {
		int val, peso;
		cout << "Ingrese el Peso del objeto " << i << ": ";
		cin >> val;
		cout << "Ingrese el Valor del objeto " << i << ": ";
		cin >> peso;
		objetos.push_back({ i,{ val,peso } });
		cout << endl;
	}
	heapSort(objetos,objetos.size());
	for (int i = 0; i < objetos.size(); i++) {
		cout << "objeto" << objetos[i].first <<" "<< objetos[i].second.first <<"\n";
	}
	for (int i = 1; i <= n; i++) {
		indice[i] = objetos[i - 1].first;
		Peso[i] = objetos[i - 1].second.first;
		Valor[i] = objetos[i - 1].second.second;

	}
	cout << "Ingrese el peso maximo de la mochila: ";
	cin >> PMax;
	cout << endl << "Calculando..." << endl;
	Mochila(n, Peso, Valor, indice, PMax);
	system("pause");
	return 0;
}
