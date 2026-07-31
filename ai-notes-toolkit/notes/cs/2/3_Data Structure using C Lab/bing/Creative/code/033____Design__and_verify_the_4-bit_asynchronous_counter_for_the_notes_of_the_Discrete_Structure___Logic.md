## Design, and verify the 4-bit asynchronous counter for the notes of the Discrete Structure & Logic Lab in the subject of Discrete Structure & Logic

An asynchronous counter is a sequential circuit that uses a series of flip-flops to generate a binary count. The output of one flip-flop is connected to the clock input of the next flip-flop, so that each flip-flop toggles at half the frequency of the previous one. The first flip-flop is driven by an external clock signal, and the rest of the flip-flops follow the state changes of the first one.

A 4-bit asynchronous counter can count from 0 to 15 in binary, and has four flip-flops, each representing one bit of the count. The most significant bit (MSB) is the output of the last flip-flop, and the least significant bit (LSB) is the output of the first flip-flop. The counter can be designed using J-K flip-flops, which have two inputs, J and K, and two outputs, Q and Q'. The J-K flip-flop can be configured to toggle its output when both J and K are high, and to hold its output when both J and K are low.

The design steps of a 4-bit asynchronous counter using J-K flip-flops are as follows:

1. Draw the state diagram of the counter, showing the binary count sequence and the transitions between the states. The state diagram for a 4-bit asynchronous counter is shown below:

![State diagram of 4-bit asynchronous counter](https://physicsteacher.in/wp-content/uploads/2021/12/4-bit-asynchronous-counter-state-diagram.png)

2. Draw the state table of the counter, showing the present state, the next state, and the inputs and outputs of each flip-flop. The state table for a 4-bit asynchronous counter is shown below:

| Present State | Next State | J A | K A | J B | K B | J C | K C | J D | K D |
|---------------|------------|-----|-----|-----|-----|-----|-----|-----|-----|
| 0000          | 0001       | 1   | X   | X   | X   | X   | X   | X   | X   |
| 0001          | 0010       | 1   | X   | 1   | X   | X   | X   | X   | X   |
| 0010          | 0011       | 1   | X   | X   | X   | X   | X   | X   | X   |
| 0011          | 0100       | 1   | X   | 1   | X   | 1   | X   | X   | X   |
| 0100          | 0101       | 1   | X   | X   | X   | X   | X   | X   | X   |
| 0101          | 0110       | 1   | X   | 1   | X   | X   | X   | X   | X   |
| 0110          | 0111       | 1   | X   | X   | X   | X   | X   | X   | X   |
| 0111          | 1000       | 1   | X   | 1   | X   | 1   | X   | 1   | X   |
| 1000          | 1001       | 1   | X   | X   | X   | X   | X   | X   | X   |
| 1001          | 1010       | 1   | X   | 1   | X   | X   | X   | X   | X   |
| 1010          | 1011       | 1   | X   | X   | X   | X   | X   | X   | X   |
| 1011          | 1100       | 1   | X   | 1   | X   | 1   | X   | X   | X   |
| 1100          | 1101       | 1   | X   | X   | X   | X   | X   | X   | X   |
| 1101          | 1110       | 1   | X   | 1   | X   | X