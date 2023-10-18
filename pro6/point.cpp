#include "point.h"

Point::Point(int x, int y, char symbol) : Shape(x, y)
{
    this->symbol = symbol;
}


// drawing point on grid
// input grid as reference 
void Point::draw(Grid &grid)
{
    grid.set(m_x, m_y, symbol);
}
