## Implementation of 4-bit parallel adder using 7483 IC for the notes of the Discrete Structure & Logic Lab in the subject of Discrete Structure & Logic

- A 4-bit parallel adder is a circuit that can perform the addition of two 4-bit binary numbers and produce a 4-bit sum and a carry bit.
- A 7483 IC is a 4-bit binary full adder with fast carry that can be used to implement a 4-bit parallel adder.
- The 7483 IC has 16 pins, as shown in the following diagram:

```
    +---+--+---+
    |1  +--+ 16|
    +---+--+---+
    |2  +--+ 15|
    +---+--+---+
    |3  +--+ 14|
    +---+--+---+
    |4  +--+ 13|
    +---+--+---+
    |5  +--+ 12|
    +---+--+---+
    |6  +--+ 11|
    +---+--+---+
    |7  +--+ 10|
    +---+--+---+
    |8  +--+  9|
    +---+--+---+
```

- The pin configuration of the 7483 IC is as follows:

|Pin Number|Pin Name|Description|
|:--------:|:------:|:---------:|
|1|C0|Carry input|
|2|A3|Most significant bit of first 4-bit number|
|3|B3|Most significant bit of second 4-bit number|
|4|S3|Most significant bit of sum output|
|5|A2|Third bit of first 4-bit number|
|6|B2|Third bit of second 4-bit number|
|7|S2|Third bit of sum output|
|8|GND|Ground|
|9|S1|Second bit of sum output|
|10|B1|Second bit of second 4-bit number|
|11|A1|Second bit of first 4-bit number|
|12|S0|Least significant bit of sum output|
|13|B0|Least significant bit of second 4-bit number|
|14|A0|Least significant bit of first 4-bit number|
|15|C4|Carry output|
|16|VCC|Power supply|

- To implement a 4-bit parallel adder using 7483 IC, the following steps are required:

  - Connect the power supply to pin 16 (VCC) and pin 8 (GND) of the IC.
  - Connect the two 4-bit numbers to be added to the inputs A0-A3 and B0-B3 of the IC. These can be either switches, logic gates, or other sources of binary signals.
  - Connect the carry input C0 to either ground (for no initial carry) or VCC (for initial carry of 1).
  - Connect the outputs S0-S3 and C4 of the IC to the display devices, such as LEDs, 7-segment displays, or other indicators of binary signals.
  - Verify the operation of the 4-bit parallel adder by changing the inputs and observing the outputs. The outputs should match the binary addition of the inputs and the carry input. For example, if A = 0101, B = 1100, and C0 = 0, then S = 0001 and C4 = 1.