#include "transmitter.h"

int main()
{
	uint8_t data[]=  {
		0b01011000
	};
	uint8_t byte = 0b10101010;
	transmit_init();
	while (1) {
		/* transmit_bytes(&byte, 1); */
		transmit_bytes(data, 1);
	}
	transmit_free();
}

