#include "square.h"
#include <iostream>
using namespace std;
Square::Square(int x, int y, int size) : Shape(x, y)
{
    this->size = size;
}

// drawing square on grid
// input grid as reference
void Square::draw(Grid &grid)
{
    for (int i = m_y; i < (m_y + size); i++)
    {
        grid.set(m_x, i, '*');
    }
    for (int i = m_x + 1; i < (m_x + size - 1); i++)
    {
        grid.set(i, m_y, '*');
        grid.set(i, m_y + size - 1, '*');
    }
    for (int i = m_y; i < (m_y + size); i++)
    {
        grid.set(m_x + size - 1, i, '*');
    }
}
