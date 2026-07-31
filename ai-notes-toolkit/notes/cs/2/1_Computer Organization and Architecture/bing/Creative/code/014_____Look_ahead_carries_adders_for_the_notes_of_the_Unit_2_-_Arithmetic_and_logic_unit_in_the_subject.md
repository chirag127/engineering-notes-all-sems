# Look ahead carries adders

- A look ahead carry adder is a type of adder that reduces the propagation delay by using more complex hardware.
- Propagation delay is the time taken for the carry to propagate from one stage to the next in a ripple carry adder.
- A look ahead carry adder divides the adder into blocks and provides circuitry to quickly determine the carry out of a block as soon as the carry in is known.
- A look ahead carry adder uses the concepts of carry generate and carry propagate to compute the carry out of a block.
- Carry generate (Cg) occurs when an output carry is generated internally by the full adder, regardless of the carry in. Cg = A.B
- Carry propagate (Cp) occurs when an output carry is equal to the carry in, meaning that the full adder propagates the carry to the next stage. Cp = A ⊕ B
- The carry out of a block can be expressed as a function of Cg, Cp and the carry in (Cin) of the block. Cout = Cg + Cp.Cin
- A look ahead carry adder can be implemented using a carry look ahead generator (CLG) and a group of carry look ahead adders (CLA).
- A CLG generates the carry out signals for each block using the Cg and Cp signals of the block.
- A CLA adds the bits within a block using the carry in signal from the CLG and generates the Cg and Cp signals for the CLG.
- A look ahead carry adder can improve the speed of addition by reducing the number of logic levels for the carry computation. However, it also increases the hardware complexity and power consumption.