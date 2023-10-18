sim: cust.o pqueue.o sim.o
	g++ -Wall -pedantic -g -o sim cust.o pqueue.o sim.o

sim.o: cust.h pqueue.h sim.cpp
	g++ -Wall -pedantic -g -std=c++11 -c sim.cpp

cust.o: cust.h cust.cpp
	g++ -Wall -pedantic -g -std=c++11 -c cust.cpp

pqueue.o: pqueue.h pqueue.cpp cust.h
	g++ -Wall -pedantic -g -std=c++11 -c pqueue.cpp

clean:
	rm -f sim sim.exe cust.o pqueue.o sim.o
