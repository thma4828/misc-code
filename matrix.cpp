// matrix.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include "NxM_Matrix.h"
#include "Sqr_Matrix.h"

using namespace std;


int main()
{
	//Control object to add other matrix objects (note: could be done in a better way)
	//NxM means columns by rows, so we actually have 3x2 matrices
	/***
		( 0, 0 )
		( 0, 0 )
		( 0, 0 )
	***/
	NxM_Matrix Control(2, 3);
	NxM_Matrix M_2_3a(2, 3);
	NxM_Matrix M_2_3b(2, 3);
	//double for loop to create an interesting matrix for each of our two examples. 
	for (int z = 0; z < 3; z++) {
		for (int p = 0; p < 2; p++) {
			int v1 = rand() % 100;
			int v2 = rand() % 100;
			cout << "in A; setting element [" << z << "][" << p << "] to: " << v1 << endl;
			cout << "in B; setting element [" << z << "][" << p << "] to: " << v2 << endl;
			M_2_3a.set_element(z, p, v1);
			M_2_3b.set_element(z, p, v2);
		}
	}
	
	//get the element at 1,1
	cout << M_2_3a.get_element(1, 1) << endl;
	
	//add our two matrices together 
	NxM_Matrix *l = Control.add_2_matrices(&M_2_3a, &M_2_3b);

	//get the elements back out at the end. 
	for (int g = 0; g < 3; g++) {
		for (int k = 0; k < 2; k++) {
			//cout << "getting element at k,g ==" << k << ',' << g << endl;
			int i = l->get_element(k, g);
			cout << i << endl;
		}
	} 
	//multiply a matrix by a scalar value
	l = Control.scalar_mul(2, l);
	for (int g = 0; g < 3; g++) {
		for (int k = 0; k < 2; k++) {
			//cout << "getting element at k,g ==" << k << ',' << g << endl;
			int i = l->get_element(k, g);
			cout << i << endl;
		}
	}
	Sqr_Matrix *Console = new Sqr_Matrix(10);
	Sqr_Matrix *C = new Sqr_Matrix(10);
	Sqr_Matrix *D = new Sqr_Matrix(10);
	//now that the rows variable is public its actually easier...
	for (int c = 0; c < C->side; c++) {
		for (int d = 0; d < D->side; d++) {
			C->rows[c][d] = rand() % 1000;
			D->rows[c][d] = rand() % 2000;
		}
	}
	Sqr_Matrix *Smat = Console->add_2_matrices(C, D);
	cout << "dot prod calculation init" << endl;
	Sqr_Matrix *Pmat = Console->mat_mul(C, D);
	cout << "Printing dot product of matrix C and matrix D" << endl;
	try {
		Console->print_mat(Pmat);
	}
	catch (exception e) {
		cout << "[1] exception e" << endl;
	}

	if (Smat != NULL) {
		for (int c = 0; c < Smat->side; c++) {
			for (int d = 0; d < Smat->side; d++) {
				cout << Smat->rows[c][d] << endl;
			}
		}
	}
	else {
		cerr << "[100] error: add matrices returned NULL [100]" << endl;
	}

	Sqr_Matrix *E = new Sqr_Matrix(4);
	Sqr_Matrix *F = new Sqr_Matrix(4);
	Sqr_Matrix *G;
	cout << "Identity matrix" << endl;
	G = E->identity_mat();
	for (int q = 0; q < G->side; q++) {
		for (int u = 0; u < G->side; u++) {
			cout << '(' << q << ',' << u << ')' << endl;
			cout << G->rows[q][u] << endl;
		}
	}
	column *t = new column();
	cout << "------------------" << endl;
	t = G->get_col(3);
	t->height = t->col.size();
	cout << "------------------" << endl;
	for (int a = 0; a < t->col.size(); a++) {
		cout << a << ": " << t->col[a] << endl;
	}
	cout << "------------------" << endl;
	row *_ROW = new row();
	cout << "------------------" << endl;
	_ROW = G->get_row(2);
	cout << "------------------" << endl;
	for (int zz = 0; zz < _ROW->len; zz++) {
		cout << _ROW->r[zz] << endl;
	}
	row *newR = G->row_plus_col(_ROW, t);
	if (newR != NULL) {
		for (int r = 0; r < newR->r.size(); r++) {
			cout << "new row[" << r << ']' << " == " << newR->r[r] << endl;
		}
	}
	else {
		cout << "row plus col function returned null" << endl;
	}
	cout << "------------------" << endl;

	row *srow = Smat->get_row(2);
	column *scol = Smat->get_col(3);
	Smat->print_row(srow);
	Smat->print_col(scol);

	row *scr = Smat->row_plus_col(srow, scol);
	Smat->print_row(scr);
	cout << "printing matrix of size = " << Smat->side << endl;
	row *sr1 = Smat->get_row(1);
	cout << "first row should be: ";
	Smat->print_row2(sr1, Smat->side);
	cout << "prnt mat init" << endl;
	Smat->print_mat(Smat);
	cout << "calculating input x weight matrix" << endl;
	column *theo = Smat->col_x_mat(scol, Smat);
	cout << "printing input x weight column" << endl;
	Smat->print_col(theo);
	column *bias = new column();
	for (int G = 0; G < 10; G++) {
		bias->col.push_back(rand() % 10);
	}
	cout << "printing bias matrix" << endl;
	Smat->print_col(bias);
	cout << "adding bias" << endl;
	column *output = Smat->col_plus_col(theo, bias);
	cout << "output" << endl;
	Smat->print_col(output);
	cout << "activating column (psudeo act func)" << endl;
	column * act = Smat->act_col(output);
	cout << "printing column" << endl;
	Smat->print_col(act);
	//choose a return value
	int r;
	cin >> r;
    return r;
}

