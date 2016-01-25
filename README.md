RAMEAR uses the hardware every computer already has to secretly transmit your data, without you realising!

What it does
------------

RAMEAR is combination transmitter and receiver designed for transmitting signals outside of standard computer interfaces. We have taken a standard Ubuntu PC, and managed to wirelessly transmit data from it - even though the PC has no Ethernet connection, no WiFi and no Bluetooth.

This is accomplished by bashing the Data Bus of the computer - the main communication avenue between the RAM and the CPU of the computer. We use a special assembler instruction to transmit 128 bits in parallel to the RAM, bypassing the cache. We repeatedly run this instruction to transmit random data over a period of 500ms, effectively increasing the radiated RF power from the bus substantially.

A ‘1’ transmission in our system corresponds to a period of high activity on the Data bus, and a ‘0’ transmission corresponds to average activity.

On the receiving end, we calculate the amplitude of the signal and process it [5 stages] to decode the waveform. We developed the transmission system from scratch in order to fit our needs, including both developing noise rejection code ourselves and automatic clock synchronisation.

How we built it
---------------

On the transmission end, we used standard hardware to emulate a wall-gapped-system, potentially inside a secure facility. We wrote some low-profile code in C which hits the data bus at its maximumum frequency - on this computer, approximately 513Mhz [that's 513 million 128-bit transactions per second]. The code has a very low memory footprint [as it writes to the same location continually], and also has a very low CPU footprint - as the memory frequency is much lower than the CPU frequency.

On the receiving end, we use a python script to process the RF data from the [bladeRF](<http://nuand.com/>). During the course of the hackathon we developed our own transmission protocol, and our own algorithms for automatic clock resynchronisation and noise rejection. In order to reject noise, we did have to maximise the transmission period, such that our data rate is approximately 2 bits per second. However, for an example use case of transmitting a 512 bit secure key from a remote air-gapped computer, this only takes 4 minutes to transmit, which we consider reasonable.

Challenges we ran into
----------------------

We get noise from the frequency channel of our RAM. We had to do a lot of signal processing to reconstruct the data we send to our RAM. The main challenges were involved with the RF processing (we had no prior RF experience) and decoding of the signal. We are dealing with extremely noisy data with no synchronising clock, and therefore the decoding algorithm was complex. However, we are comfortable with how it performed at the end - in several tests it managed to transmit 40 bytes consecutively without a single error.

Accomplishments that we're proud of
-----------------------------------

Actually managing to make it work was a challenge - especially when it came to data decoding. The data decoding automatically resynchronises the clock on high quality pulses, and then relies on this timing when the signal becomes worse in quality. Secondly, the system automatically keeps track of the high and low signal powers, and continually readjusts the thresholds to ensure that a drift in power still remains readable.

What we learned
---------------

-   How to use the BladeRF

-   How to integrate assembler instructions into a C program

-   How to calculate the power of a I/Q RF signal

-   How to roll-your-own clock resynchronisation

What's next for RAMEAR
----------------------

At another hackathon we would love to increase the power of the system and improve its range. We believe we should be able to achieve substantially greater ranges by incorporating more RF knowledge into the project - using tools such as increasing the gain in hardware.

We would also like to hijack the mobile baseband in your phone to pick up these signals automatically - without the need for a Software Defined Radio (SDR) like the BladeRF. Overall, for 36 hours - we are happy!

Built With
----------

-   blade
-   bladerf
-   [c](<http://devpost.com/software/built-with/c>)
-   [python](<http://devpost.com/software/built-with/python>)


For more details, see http://devpost.com/software/ramear
