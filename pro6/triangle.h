#ifndef TRIANGLE_H
#define TRIANGLE_H

#include "shape.h"

class Triangle : public Shape {
public:
    Triangle(int x, int y);
    // method draw override from Shape class
    void draw(Grid& grid) override;
};

#endif
