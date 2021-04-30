
#include <iostream>
#include <cstdlib>
#include <vector>
#define int_max 2147483647
using namespace std;


void decMat(pair<int, int>*** mat, int filas, int columnas)
{
  *mat = new pair<int, int>*[filas];
  for(short i  = 0; i < filas; i++)
    *mat[i] = new pair<int, int>[columnas];
}

class Matrix{
  public:
  Matrix(int _filas,int _columnas){
    filas=_filas;
    columnas=_columnas;
    matrix=new pair<int,int>*[filas];
    
    for(int i=0;i<filas;i++){
      matrix[i]=new pair<int,int>[columnas];
    }
  }

  int val_reduce_filas()
  {
    //Comparando valores x
    short fe = 0;
    int c = 0; int fila;
    int min = int_max;
    for(short i = 0; i < columnas; i++){
      for(short j = 0; j < filas; j++){
        if(matrix[j][i].first < min){
          min = matrix[j][i].first; c++;
          fe = j;
        }
        else continue;
      }
      if(c == columnas) { return fe; }
    
    }
    return 8;
  }

  

  void reducedmatrixF()
  {
    //Matrix* rf = new Matrix(filas - 1, columnas); 
    pair<int,int> **rf;
    rf = new pair<int, int>*[filas-1];
    for(short a  = 0; a < filas - 1; a++)
      rf[a] = new pair<int, int>[columnas];
    //decMat(&rf,filas-1,columnas);
    short k = 0;
    for(short i = 0; i < filas; i++){
      for(short j = 0; j < columnas; j++){
        if(i != val_reduce_filas())
          rf[k][j] = matrix[i][j];
        else
          j = columnas;
      }
      if(i != val_reduce_filas())
        k++;
    }
    matrix = rf;
    filas--;
    //#return matrix;
  }

  void fillmatrix()
  {
    system("clear");
    int n1,n2;
    for(short i = 0; i < filas; i++){
      for(short j = 0; j < columnas; j++){
        cout << "Fila: " << i + 1 << " Columna: " << j + 1 << "\n"; 
        cout << "Numero 1: "; cin >> n1; cout << "Numero 2: "; cin >> n2; cout << "\n";
        matrix[i][j].first = n1; matrix[i][j].second = n2; 
        system("clear");
      }
    }
    
  }

  void show(){
    for(int i=0;i<filas;i++){
      for(int j=0;j<columnas;j++){
      cout<<"("<<matrix[i][j].first<<";"<<matrix[i][j].second<<")";
      } 
      cout<<endl;
    }
  }

  private:
  pair<int,int> **matrix;
  int filas;
  int columnas;
};