# RAMEAR

RAMEAR is a project from [PennApps](pennapps.com) Spring 2016. RAMEAR uses the RF signals created
from exciting the data bus between memory and CPU to transmit data off an air-gapped
computer. When the data bus is excited with random data, the data bus transmit an
above-average RF signal (due to power). The project utilizes this fact to transmit
binary signals.

During the hackathon, we were able to transmit the signal from as far as `20cm` at a
rate of `2 bits/second`. Although realistically this isn't fast enough to transmit
plain text / metadata, it takes around 20 minutes to transmit an 2048-bit RSA key
and around 2 minutes to transmit a 256-bit AES key, which are reasonable
amounts of time.

The program has a low CPU process consumption and memory footprint, making it hard
to detect. It is also worth mentioning that this 'attack' / 'hack' does not
require root (aka `sudo`) access.

## Demo

[Live Demo - Pennapps Spring 2016 Presentation](https://www.youtube.com/watch?v=UGVrB8IdINo#t=753)

[Project at devpost](http://devpost.com/software/ramear)


## The Science

For technicalities / science of the project, checkout:

* [A blog post by Fu Yong (mainly about tranmistting signals)](http://www.fyquah.me/ramear)

## Code Structure

On the machine transmitting signals

* `main.c`
The main process, queries for a string and sends it as a binary signal
* `transmitter.c`
Functions to send bytes / bits
* `transmitter.h`
Header files for the transmitter

On the machine receiving signals

* `main.py`
The code to decode parse the signals on the machine

## BladeRF Configuration

We used a bladeRF as our receiver. These are our configurations:

* `samplerate 100000`
* `frequency 513M`
* `bandwidth 1.5M`

We ran our experiments on a old Dell desktop booted with Ubuntu 14.04.
Unfortunately, we do not know the name of the model and the exact specs,
other than the RAM being 667 MHz. The configurations above might be
different depending on the specs of the computer.

## Reference

* Guri, M., Kachlon, A., Hasson, O., Kedma, G., Mirsky, Y. and Elovici, Y., 2015. GSMem: data exfiltration from air-gapped computers over GSM frequencies. In *24th USENIX Security Symposium (USENIX Security 15)* (pp. 849-864).


## License

GNU GPL v3
