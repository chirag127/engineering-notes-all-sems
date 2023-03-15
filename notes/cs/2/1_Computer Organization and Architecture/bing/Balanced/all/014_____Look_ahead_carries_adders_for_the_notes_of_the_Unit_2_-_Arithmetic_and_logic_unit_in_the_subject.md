# Look ahead carries adders

- A look ahead carry adder is a type of adder that reduces the propagation delay by using more complex hardware.
- Propagation delay is the time taken for the carry to propagate from one stage to the next in a ripple carry adder.
- A look ahead carry adder divides the adder into blocks and provides circuitry to quickly determine the carry out of a block as soon as the carry in is known.
- A look ahead carry adder uses the concepts of carry generate and carry propagate to compute the carry out of a block.
- Carry generate (Cg) occurs when an output carry is generated internally by the full adder, regardless of the carry in. Cg = A.B
- Carry propagate (Cp) occurs when an output carry is equal to the carry in, meaning that the full adder propagates the carry to the next stage. Cp = A ⊕ B
- The carry out of a block can be expressed as a function of Cg, Cp and the carry in (Cin) of the block. Cout = Cg + Cp.Cin
- The carry out of a block can be computed in parallel with the sum outputs of the block, thus reducing the delay.
- A look ahead carry adder can be implemented using a 4-bit carry look ahead adder (CLA) module, which has four inputs (A0, A1, A2, A3), four outputs (S0, S1, S2, S3), a carry in (Cin) and a carry out (Cout).
- A 4-bit CLA module consists of four full adders, a carry look ahead generator (CLG) and a carry look ahead propagator (CLP).
- The CLG computes the Cg and Cp signals for each bit of the block.
- The CLP computes the Cout signal using the Cg and Cp signals and the Cin signal.
- The sum outputs are computed by the full adders using the A, B and Cp signals.
- A 4-bit CLA module can be extended to a 16-bit CLA adder by using four 4-bit CLA modules and a 4-bit CLA module as a carry look ahead unit (CLU).
- The CLU computes the carry out signals for each 4-bit block using the Cg and Cp signals of the blocks and the Cin signal of the adder.
- The carry out signals of the CLU are connected to the carry in signals of the corresponding 4-bit blocks.
- The sum outputs of the 16-bit CLA adder are the sum outputs of the four 4-bit blocks.
- A 16-bit CLA adder can be further extended to a 64-bit CLA adder by using four 16-bit CLA adders and a 4-bit CLA module as a CLU.