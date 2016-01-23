CFLAGS+= -msse2 -Wall -std=c99 -O2
:q

all: main

main: main.o

clean:
	rm -rf *.o main
