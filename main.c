#include "transmitter.h"
#include <string.h>
#include <stdio.h>

int main()
{
	 /*
	uint8_t byte = 0b10101010;
	uint8_t zero = 0;
	*/
	transmit_init();
	while (1) {
		uint8_t * data = NULL;
		size_t len = 0;
		puts("Enter a string to transmit: ...");
		getline(&data, &len, stdin);
		transmit_begin();
		transmit_bytes(data, strlen((const char*) data) - 1);
		transmit_end();
		puts("done!");
		free(data);
	}
	transmit_free();
}

