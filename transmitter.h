#include <stdio.h>
#include <stdint.h>
#include <time.h>
#include <stdlib.h>
#include <emmintrin.h>

void transmit_init();
void transmit_free();
void transmit_begin();
void transmit_bytes(uint8_t * bytes, uint8_t len);
void transmit_end();
