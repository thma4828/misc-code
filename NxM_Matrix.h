#pragma once
#include <iostream>
#include <vector>

using namespace std;
//My matrix class that holds its size mxn...
class NxM_Matrix {
private:
public:
	int N;
	int M;
	vector<vector<int>>rows;
	//constructor
	NxM_Matrix(int n, int m) {
		N = n;
		M = m;
		//init n x m matrix to a 0 matrix. 
		for (int j = 0; j < m; j++) {
			vector<int>null_row(m);
			for (int c = 0; c < m; c++) {
				null_row.push_back(0);
			}
			rows.push_back(null_row);
		}

	}
	//get element function with exception handling
	int get_element(int x, int y) {
		try {
			//cout << "x = " << x << " and y = " << y << endl;
			return (rows[x][y]);
		}
		catch (exception e) {
			cout << "ERROR 1: element out of bounds!" << endl;
		}
	}
	//set element function with exception handling
	void set_element(int x, int y, int a) {
		try {
			//cout << "x = " << x << " and y = " << y << endl;
			rows[x][y] = a;
		}
		catch (exception e) {
			cout << "ERROR 1 element out of bounds!" << endl;
		}
	}
	//add 2 matrices and return a pointer to the new matrix --> IF THEY HAVE THE SAME SIZE
	NxM_Matrix * add_2_matrices(NxM_Matrix * A, NxM_Matrix * B) {
		if ((A->M == B->M) && (A->N == B->N)) {
			//you are creating a new object here... should be deleted somehow...
			NxM_Matrix *sumAB = new NxM_Matrix(A->M, A->N);
			for (int i = 0; i < A->M; i++) {
				for (int j = 0; j < A->N; j++) {
					cout << "i: " << i << " and j: " << j << endl;
					//cout << "trying to access rows[i][j]" << endl;
					//sum same elements. 
					int x = A->rows[i][j];
					int y = B->rows[i][j];
					int S = x + y;
					//cout << "x =" << x << " and y =" << y << endl;
					//cout << "x + y = " << S << endl;
					cout << "inserting s = " << S << " at element i,j =" << i << ',' << j << endl;
					//insert new elements into the new matrix we created to return
					sumAB->set_element(j, i, S);
				}
			}
			return sumAB;
		}
		else {
			cout << "[-] error: matrices not shaped correctly [-]" << endl;
			return NULL;
		}
	}

	NxM_Matrix * scalar_mul(int a, NxM_Matrix * C) {
		for (int i = 0; i < C->M; i++) {
			for (int j = 0; j < C->N; j++) {
				C->rows[i][j] = C->rows[i][j] * a;
			}
		}
		return C;
	}

};
