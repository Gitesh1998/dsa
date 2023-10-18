shapes: main.o shape.o grid.o triangle.o square.o circle.o point.o
	g++ -Wall -pedantic -g -std=c++11 -o shapes main.o shape.o grid.o triangle.o square.o circle.o point.o

grid_test: grid_test.o grid.o
	g++ -Wall -pedantic -g -std=c++11 -o grid_test grid_test.o grid.o

grid_test.o: grid_test.cpp grid.h 
	g++ -Wall -pedantic -g -std=c++11 -c grid_test.cpp

main.o: main.cpp shape.h grid.h triangle.h square.h circle.h point.h
	g++ -Wall -pedantic -g -std=c++11 -c main.cpp

shape.o: shape.cpp shape.h grid.h
	g++ -Wall -pedantic -g -std=c++11 -c shape.cpp

grid.o: grid.cpp grid.h
	g++ -Wall -pedantic -g -std=c++11 -c grid.cpp

triangle.o: triangle.cpp triangle.h shape.h grid.h
	g++ -Wall -pedantic -g -std=c++11 -c triangle.cpp

square.o: square.cpp square.h shape.h grid.h
	g++ -Wall -pedantic -g -std=c++11 -c square.cpp

circle.o: circle.cpp circle.h shape.h grid.h
	g++ -Wall -pedantic -g -std=c++11 -c circle.cpp

point.o: point.cpp point.h shape.h grid.h
	g++ -Wall -pedantic -g -std=c++11 -c point.cpp

clean:
	rm -f shapes shapes.exe main.o shape.o grid.o triangle.o square.o circle.o point.o grid_test grid_test.o
