#ifndef POINT_H
#define POINT_H

#include "shape.h"

class Point : public Shape {
public:
    Point(int x, int y, char symbol);
    // method draw override from Shape class
    void draw(Grid& grid) override;

private:
    char symbol;
};

#endif
