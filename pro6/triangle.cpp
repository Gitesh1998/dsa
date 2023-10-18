#include "triangle.h"

Triangle::Triangle(int x, int y) : Shape(x, y)
{
}

// drawing triangle on grid
// input grid as reference
void Triangle::draw(Grid &grid)
{
    grid.set(m_y+2, m_x, '+');
    grid.set(m_y + 1, m_x + 1, '+');
    grid.set(m_y + 3, m_x + 1, '+');
    grid.set(m_y, m_x+2, '+');
    grid.set(m_y + 1, m_x + 2, '+');
    grid.set(m_y + 2, m_x + 2, '+');
    grid.set(m_y + 3, m_x + 2, '+');
    grid.set(m_y + 4, m_x + 2, '+');
}
