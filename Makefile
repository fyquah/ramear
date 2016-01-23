CFLAGS+= -msse2 -Wall -std=c99 -O2

all: main

main: main.o transmitter.o

clean:
	rm -rf *.o main
