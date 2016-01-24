#include "transmitter.h"

int main()
{
	uint8_t data[]=  {
		0b01011010,
		0b10010001,
		0b00001000,
		0b11110001
	};
	uint8_t byte = 0b10101010;
	transmit_init();
	while (1) {
		transmit_bytes(&byte, 1);
		/* transmit_bytes(data, 4); */
	}
	transmit_free();
}

