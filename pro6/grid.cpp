#include "grid.h"
#include <iostream>
using namespace std;

// creating grid in 2d array
Grid::Grid() {
    for (int i = 0; i < COLS; i++) {
        for (int j = 0; j < ROWS; j++) {
            m_grid[i][j] = ' ';
        }
    }
}

// setting character in 2d array as drawing purpose
void Grid::set(int x, int y, char c) {
    // checking that x and y should exist in boundary of grid
    if (x >= 0 && x < COLS && y >= 0 && y < ROWS) {
        m_grid[x][y] = c;
    }
}

// printing 2d grid array
void Grid::print() {
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            cout << m_grid[j][i];
        }
        cout << endl;
    }
}