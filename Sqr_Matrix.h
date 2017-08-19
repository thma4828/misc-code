#pragma once
#include <iostream>
#include <vector>
#include "NxM_Matrix.h"

using namespace std;

struct column {
	int height;
	vector<int>col;
};

struct row {
	int len;
	vector<int>r;
};

class Sqr_Matrix : public NxM_Matrix{
public:
	int side;
	vector<row>r;
	vector<column>c;
	Sqr_Matrix(int N) : NxM_Matrix(N, N){
		side = N;
	}
	column *act_col(column *A) {
		for (int i = 0; i < A->col.size(); i++) {
			A->col[i] = activate(A->col[i]);
		}
		return A;
	}
	int activate(int a) {
		return a % 100;
	}
	void print_row(row *A) {
		cout << '[';
		for (int i = 0; i < A->r.size(); i++) {
			cout << ' ' <<  A->r[i] << ' ,';
		}
		cout << ']' << endl;
	}
	void print_row2(row *A, int t) {
		cout << '[';
		for (int i = 0; i < t; i++) {
			cout << ' ' << A->r[i] << ' ,';
		}
		cout << ']' << endl;
	}

	void print_col(column *A) {
		cout << '[';
		for (int i = 0; i < A->col.size(); i++) {
			cout << A->col[i] << ',' << endl;
		}
		cout << ']' << endl;
	}

	column * col_x_mat(column * B, Sqr_Matrix * C) {
		if (C->rows.size() != 0 && B->col.size() != 0) {
			column *sCOL = new column();
			for (int i = 0; i < C->side; i++) {
				int sum = 0;
				for (int j = 0; j < C->side; j++) {
					int n = C->rows[i][j];
					sum += (n * B->col[j]);
				}
				sCOL->col.push_back(sum);
			}
			return sCOL;
		}
		return NULL;
	}

	column *col_plus_col(column *A, column *B) {
		column *z = new column();
		if (A->col.size() == B->col.size()) {
			for (int p = 0; p < A->col.size(); p++) {
				z->col.push_back(A->col[p] + B->col[p]);
			}
			return z;
		}
		return NULL;
	}

	void print_mat(Sqr_Matrix *E) {
		for (int z = 0; z < E->rows.size(); z++) {
			try {
				row *eRow = new row();
				eRow->r = E->rows[z];
				eRow->len = eRow->r.size();
				print_row2(eRow, E->side);
			}
			catch (exception e) {
				cout << "[-100] exception thrown [-100]" << endl;
				break;
			}
		}
	}

	row * col_to_row(column *C) {
		if (C->col.size() == 0) { return NULL; }
		row *T = new row();
		for (int z = 0; z < C->col.size(); z++) {
			T->r.push_back(C->col[z]);
		}
		return T;
	}

	column * row_to_col(row *T) {
		if (T->r.size() == 0) { return NULL; }
		column *C = new column();
		for (int z = 0; z < T->r.size(); z++) {
			C->col.push_back(T->r[z]);
		}
		return C;
	}

	Sqr_Matrix * add_2_matrices(Sqr_Matrix * A, Sqr_Matrix * B) {
		if (A->side == B->side){
			//you are creating a new object here... should be deleted somehow...
			Sqr_Matrix *sumAB = new Sqr_Matrix(A->side);
			for (int i = 0; i < A->side; i++) {
				for (int j = 0; j < A->side; j++) {
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
			sumAB->side = A->side;
			return sumAB;
		}
		else {
			cout << "[-] error: not square matrices" << endl;
			return NULL;
		}
	}
	int row_x_col(row *A, column *B) {
		if (A == NULL || B == NULL) {
			cout << "FATAL ERROR" << endl;
			return -999;
		}
		int s = 0;
		if (A->r.size() == B->col.size()) {
			for (int i = 0; i < A->r.size(); i++) {
				int a = A->r[i];
				int b = B->col[i];
				int ab = a * b;
				s += ab;
			}
			return s;
		}
		return 0;
	}

	Sqr_Matrix * mat_mul(Sqr_Matrix *X, Sqr_Matrix *Y) {
		Sqr_Matrix *sum_mat = new Sqr_Matrix(X->side);
		int SIDE = X->side;
		int row_i = SIDE;
		int col_i = SIDE;
		if (X->side != Y->side || X->side == 0 || Y->side == 0) {
			return NULL;
		}
		else {
			vector<vector<int>>s2;
			for (int j = 0; j < X->side; j++) {
				vector<int>s1;
				for (int k = 0; k < X->side; k++) {
					cout << "j,k == " << j << ',' << k << endl;
					row *crow = new row();
					column *ccol = new column();
					crow = X->get_row(j + 1);
					ccol = Y->get_col(k + 1);
					int sj = row_x_col(crow, ccol);
					if (sj != -999) {
						s1.push_back(sj);
					}
					else {
						s1.push_back(0);
					}
					
					delete crow, ccol;
				}
				s2.push_back(s1);
			}
			sum_mat->rows = s2;
			return sum_mat;
			//todo, use sums vector to construct a new square matrix as a pointer then return it. 
		}
	}

	Sqr_Matrix * identity_mat() {
		Sqr_Matrix * identity = new Sqr_Matrix(side);
		for (int i = 0; i < side; i++) {
			for (int j = 0; j < side; j++) {
				if (i == j) {
					identity->rows[i][j] = 1;
				}
				else {
					identity->rows[i][j] = 0;
				}
			}
		}
		if (side >= 1)
			return identity;
		else
			return NULL;
	}

	column * get_col(int w) {
		if (w >= side || w < 1) {
			return NULL;
		}
		column *C = new column();
		for (int i = 0; i < side; i++) {
			for (int j = 0; j < side; j++) {
				if (j == w - 1) {
					cout << rows[i][j] << endl;
					C->col.push_back(rows[i][j]);
				}
			}
		}
		C->height = C->col.size();
		return C;
	}

	row * get_row(int r) {
		if (r >= side || r < 1) {
			return NULL;
		}
		row *A = new row();
		vector<int>R = rows[r];
		A->r = R;
		A->len = side;
		cout << "returning row of size: " << side << endl;
		return A;
	}

	row * row_plus_col(row *A, column *B) {
		if (A->len != B->height || A->len == 0 || B->height == 0) {
			cout << "[-] error, row and col not structured right, or not initialized right" << endl;
			cout << "A->length == " << A->len << "{*-{-*-}-*} B->length == " << B->height << endl;
			return NULL;
		}
		int LENGTH = A->len;
		row *C = new row();
		for (int i = 0; i < LENGTH; i++) {
			int s = A->r[i];
			int q = B->col[i];
			int sq = s + q;
			C->r.push_back(sq);
		}
		return C;
	}
};


