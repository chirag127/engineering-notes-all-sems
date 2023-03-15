### Look ahead carries adders

- A look ahead carry adder is a type of adder that reduces the propagation delay by using more complex hardware to compute the carry signals faster  .
- The propagation delay is the time taken for the carry signal to propagate from the least significant bit to the most significant bit of the adder.
- A look ahead carry adder uses the concepts of carry generate and carry propagate to determine the carry out of each bit position as soon as the carry in is known.
- Carry generate, Cg, is a boolean function that indicates whether an output carry is generated internally by the full adder, regardless of the carry in. Cg is true when both the input bits A and B are 1 .
- Carry propagate, Cp, is a boolean function that indicates whether an output carry is propagated from the carry in. Cp is true when either of the input bits A or B is 1 .
- The carry out of each bit position can be expressed as a boolean function of Cg, Cp, and the carry in, Cin. For example, the carry out of the first bit position, C1, is given by C1 = Cg0 + Cp0 * Cin .
- A look ahead carry adder can be implemented by dividing the adder into blocks of fixed size, such as 4 bits, and providing circuitry to quickly compute the carry out of each block as a function of the carry in and the Cg and Cp signals of the block .
- The carry out of each block can be used as the carry in of the next block, thus reducing the propagation delay across the blocks. The carry out of the last block is the final carry out of the adder .
- A look ahead carry adder can be designed using various logic gates, such as AND, OR, and XOR gates, to implement the Cg, Cp, and carry out functions  .
- A look ahead carry adder can perform faster addition than a ripple carry adder, but it requires more hardware and power consumption .