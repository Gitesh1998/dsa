
videos: video.o main.cpp
	g++ -Wall -pedantic -g -std=c++11 -o videos video.o main.cpp


video.o: video.h video.cpp
	g++ -Wall -pedantic -g -std=c++11 -c video.cpp

clean:
	rm -f videos main.o
