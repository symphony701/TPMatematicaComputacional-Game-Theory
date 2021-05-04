#include <iostream>
#include <cstdlib>
#include <vector>
#define int_max 2147483647
using namespace std;

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

  int toDelCol()
  {
    short dc;
    short ct = 0; //Valores booleanos
    short ans = 0;
    for(short j = 0; j < columnas; j++){
      for(short j_2 = j + 1; j_2 < columnas; j_2++){ //columnas restantes a comparar 
        for(short v = 0; v < filas; v++)//j recorre los valores de la columna
        {
          if(matrix[v][j].second > matrix[v][j_2].second)
            ct = 1; 
          else if(matrix[v][j].second == matrix[v][j_2].second)
            ct = 4;
          else
            ct = 0;
          ans += ct;
        }
        if(ans == filas){
          dc = j_2; return dc; 
        }
        else if(ans == 0){
          dc = j; return dc; 
        }
        else
          ct = 0; 
        ans = 0;
      }
    }
    return -1;
  }

  int toDelRow()
  {
    short dr;
    short ct = 0; //Valores booleanos
    short ans = 0;
    for(short i = 0; i < filas; i++){
      for(short i_2 = i + 1; i_2 < filas; i_2++){ //filas restantes a comparar 
        for(short v = 0; v < columnas; v++)//j recorre los valores de la columna
        {
          if(matrix[i][v].first > matrix[i_2][v].first)
            ct = 1; 
          else if(matrix[i][v].first == matrix[i_2][v].first)
            ct = 4; 
          else
            ct = 0;
          ans += ct;
        }
        if(ans == columnas){
          dr = i_2; return dr; 
        }
        else if(ans == 0){
          dr = i; return dr;
        }
        else
          ct = 0;
        ans = 0;
      }
    }
    return -1;
  }

  

  void reducematrixF()
  {
    pair<int,int> **rf;
    rf = new pair<int, int>*[filas-1];
    for(short a  = 0; a < filas - 1; a++)
      rf[a] = new pair<int, int>[columnas];
    int drow = toDelRow();
    
    short k = 0;
    for(short i = 0; i < filas; i++){
      for(short j = 0; j < columnas; j++){
        if(i != drow)
          rf[k][j] = matrix[i][j];
        else
          continue;
      }
      if(i != drow)
        k++;
    }
    matrix = rf;
    filas--;
    
  }

   void reducedmatrixC()
  {
     
    pair<int,int> **rf;
    rf = new pair<int, int>*[filas];
    for(short a  = 0; a < filas; a++)
      rf[a] = new pair<int, int>[columnas-1];
    int dcol = toDelCol();
    
    short k = 0;
    for(short i = 0; i < filas; i++){
      for(short j = 0; j < columnas; j++){
        if(j != dcol){
          rf[i][k] = matrix[i][j];
          k++;
        }
        else
          continue;
      }
      k = 0;
    }
    matrix = rf;
    columnas--;
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

  void CS(){
    cout<<"CS: {";
    for(int i=0;i<filas;i++){
      for(int j=0;j<columnas;j++){
      cout<<"("<<matrix[i][j].first<<","<<matrix[i][j].second<<")";
      (i + j != columnas) && cout<<";";
      
      } 
    }
    cout<<"}\n";
  }
   
  void nash(){
    pair<int,int>enep[2];
    int mayorx=matrix[0][0].first;
    int mayory=matrix[0][0].second;

    for(int i=0;i<filas;i++){
      for(int j=0;j<columnas;j++){
        if(matrix[i][j].first>mayorx){
          enep[0]=matrix[i][j];
          mayorx=matrix[i][j].first;
          }
        if(matrix[i][j].second > mayory){
          enep[1]=matrix[i][j];
          mayory=matrix[i][j].second;
          }
      }
    }
    cout<<"ENEP :{("<<enep[0].first<<";"<<enep[0].second<<");";
    cout<<"("<<enep[1].first<<";"<<enep[1].second<<")}";
  }
   


  /*pair<int,int>* ENEP()
  {
    pair<int,int>* enep = new pair<int,int>[2];
    int maxJ1 = matrix[0][0].first;
    int maxJ2 = matrix[0][0].second;
    short j;
    int f1,c1,f2,c2;
    for(short i = 0; i < filas*columnas; i++)
    {
      j = -(columnas*) + i;
     if(maxJ1 < matrix[int(i/columnas)][j].first) { maxJ1 =  matrix[int(i/columnas)][j].first; f1 = i/columnas; c1 = j;  }
     if(maxJ2 < matrix[int(i/columnas)][j].second) { maxJ2 = matrix[int(i/columnas)][j].second; f2 = i/columnas; c2 = j; }
    }
    return enep;
  }*/



  void show(){
    for(int i=0;i<filas;i++){
      for(int j=0;j<columnas;j++){
      cout<<"("<<matrix[i][j].first<<","<<matrix[i][j].second<<")";
      } 
      cout<<endl;
    }
  }

  private:
  pair<int,int> **matrix;
  int filas;
  int columnas;
};
