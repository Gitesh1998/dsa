#ifndef SQUARE_H
#define SQUARE_H

#include "shape.h"

class Square : public Shape
{
public:
    Square(int x, int y, int size);
    // method draw override from Shape class
    void draw(Grid &grid) override;

private:
    int size;
};

#endif
