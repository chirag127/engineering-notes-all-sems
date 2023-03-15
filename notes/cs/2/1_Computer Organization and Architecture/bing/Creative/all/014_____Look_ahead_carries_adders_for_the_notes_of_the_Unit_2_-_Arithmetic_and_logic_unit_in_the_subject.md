# Look ahead carries adders

- A look ahead carry adder is a type of adder that reduces the propagation delay by using more complex hardware.
- Propagation delay is the time taken for the carry to propagate from one stage to the next in a ripple carry adder.
- A look ahead carry adder divides the adder into blocks and provides circuitry to quickly determine the carry out of a block as soon as the carry in is known.
- A look ahead carry adder uses the concepts of carry generate and carry propagate to calculate the carry out of a block.
- Carry generate (Cg) occurs when an output carry is generated internally by the full adder, regardless of the carry in. Cg = A.B
- Carry propagate (Cp) occurs when an output carry is propagated from the carry in, regardless of the input bits. Cp = A ⊕ B
- The carry out of a block can be expressed as a function of Cg, Cp and the carry in (Cin). Cout = Cg + Cp.Cin
- A look ahead carry adder can be implemented using a carry look ahead generator (CLG) and a group of full adders.
- A CLG takes the Cg and Cp signals from each full adder and generates the carry out signals for each block using logic gates.
- A full adder takes the input bits (A and B) and the carry in (Cin) and generates the sum bit (S) and the carry out (Cout) using logic gates.
- The sum bit can be expressed as a function of A, B and Cin. S = A ⊕ B ⊕ Cin
- A look ahead carry adder can be designed for any number of bits by cascading the CLG and the full adders.
- A look ahead carry adder can improve the speed of addition by reducing the carry propagation delay, but it requires more hardware and power than a ripple carry adder.