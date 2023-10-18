#ifndef CIRCLE_H
#define CIRCLE_H

#include "shape.h"

class Circle : public Shape {
public:
    Circle(int x, int y);
    // method draw override from Shape class
    void draw(Grid& grid) override;
};

#endif
