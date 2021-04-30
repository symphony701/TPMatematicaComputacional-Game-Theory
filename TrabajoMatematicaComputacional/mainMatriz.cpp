
#include <iostream>
#include <cstdlib>
#include <ctime>
#include <vector>
#include "Matriz.hpp"
#define spc "\n"
using std::cout; using std::cin; using std::vector,std::pair;

int* imput()
{
  int* a = new int[2]; 
  a[0] = a[1] = 0;
  for(int _ = 0; _ < 2; _++){
    do{
      printf("Ingrese numero\n");
      cin >> a[_];
    }while(!((a[_] == 2 or a[_] == 3)));
  }
  return a;
}

int main() {
  
 srand(time(0));

Matrix *matriz = new Matrix(3, 3);
matriz->fillmatrix();
matriz->show();
cout<<spc;
cout <<"Fila eliminada: "<< matriz->val_reduce_filas() + 1; 
matriz->reducedmatrixF();
cout<<"\n";
cout<<spc;
matriz->show();
cout<<spc;

return 0;
}
