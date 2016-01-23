#include <stdio.h>
#include <stdint.h>
#include <time.h>
#include <stdlib.h>
#include <emmintrin.h>
#define BUFFER_SIZE 164096

uint32_t tx_time = 500000;
static volatile __m128i * buffer;
static volatile __m128i reg;


static inline uint32_t current_time() {
	clock_t now = clock();
	return now;
}

static inline void steroids()
{
	__m128i* buffer_ptr = (__m128i*) buffer;

	for (uint32_t i = 0 ; i < BUFFER_SIZE ; i++) {
		_mm_stream_si128(&reg, *buffer_ptr);
		buffer_ptr = buffer_ptr + 1;
	}
}

int main()
{
	double period = (double) ((double) (tx_time) / CLOCKS_PER_SEC);
	double frequency = 1 / period;
	printf("pulse period = %.6f, pulse frequency = %.6f\n",
	       period, frequency);
	buffer = (__m128i*) malloc(sizeof(__m128i) * BUFFER_SIZE);
	for (uint32_t i = 0 ; i < BUFFER_SIZE ; i++) {
		buffer[i][0] = rand();
		buffer[i][1] = rand();
	}

	uint32_t data = 0x55555555;

	for (uint32_t bit_index = 0 ; bit_index < 32 ; bit_index++) {
		if (((data >> bit_index) & 0b1) == 1) {
			clock_t begin = clock();
			while(clock() - begin < tx_time) {
				steroids();
			}
			puts("HIGH");
		} else {
			clock_t begin = clock();
			while(clock() - begin < tx_time);
			puts("LOW");
		}
	}
}

