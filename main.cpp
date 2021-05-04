#include <iostream>
#include <cstdlib>
#include <ctime>
#include <vector>
#include "CMatriz.hpp"
#include <cmath>
using namespace std;


void decMat(pair<int, int>*** mat, int filas, int columnas)
{
  *mat = new pair<int, int>*[filas];
  for(short i  = 0; i < filas; i++)
    *mat[i] = new pair<int, int>[columnas];
}

int* imput()
{
  int* a = new int[2]; 
  a[0] = a[1] = 0;
  for(int _ = 0; _ < 2; _++){
    do{
      printf("Ingrese numero\n");
      cin >> a[_];
    }while(!((a[_] == 2 || a[_] == 3)));
  }
  return a;
}




int main() {
  
 srand(time(0));

Matrix *matriz = new Matrix(3, 3);
matriz->fillmatrix();
matriz->show();
cout << "\n";
cout << "Fila eliminada: " << matriz->toDelRow() + 1; 
matriz->reducematrixF();
cout << "\n";
matriz->show();
cout << "\n";
cout << "\n";
cout << "Columna eliminada: " << matriz->toDelCol() + 1 << "\n";
matriz->reducedmatrixC();
matriz->show();
cout << "\n";
cout << "\n";
//cout<< matriz->ENEP()[1].first << " " << matriz->ENEP()[1].second << endl;
matriz->nash();
cout<<"\n";
matriz->CS();

  return 0;
}