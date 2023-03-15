### Look ahead carries adders

- A look ahead carry adder is a type of adder that reduces the propagation delay by using more complex hardware to compute the carry signals faster.
- The propagation delay is the time taken for the carry signal to propagate from the least significant bit to the most significant bit of the adder.
- A look ahead carry adder divides the adder into blocks and provides circuitry to quickly determine the carry out of a block as soon as the carry in is known.
- The carry out of a block depends on two variables: carry generate and carry propagate.
- Carry generate, Cg, occurs when an output carry is generated internally by the full adder, regardless of the carry in. For example, Cg = 1 when A = 1 and B = 1.
- Carry propagate, Cp, occurs when an output carry is propagated from the carry in. For example, Cp = 1 when A = 1 and B = 0, or when A = 0 and B = 1.
- The carry out of a block can be expressed as a function of Cg, Cp, and the carry in, Ci: Co = Cg + Cp * Ci.
- The carry look ahead logic computes the Cg and Cp values for each block in parallel, and then uses them to calculate the carry out of each block in a two-level logic.
- The advantage of a look ahead carry adder is that it reduces the propagation delay from O(n) to O(log n), where n is the number of bits in the adder.
- The disadvantage of a look ahead carry adder is that it requires more hardware and power than a simple ripple carry adder.