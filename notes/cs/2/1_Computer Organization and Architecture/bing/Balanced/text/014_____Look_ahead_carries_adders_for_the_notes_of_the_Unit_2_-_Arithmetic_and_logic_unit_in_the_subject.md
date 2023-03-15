### Look ahead carries adders

- A look ahead carry adder is a type of adder that reduces the propagation delay by using more complex hardware to compute the carry signals faster.
- The propagation delay is the time taken for the carry signal to propagate from the least significant bit to the most significant bit of the adder.
- A look ahead carry adder divides the adder into blocks and provides circuitry to quickly determine the carry out of a block as soon as the carry in is known.
- The carry out of a block depends on two variables: carry generate and carry propagate.
- Carry generate (Cg) occurs when an output carry is generated internally by the full adder, regardless of the carry in. For example, Cg = 1 when A = 1 and B = 1.
- Carry propagate (Cp) occurs when an output carry is equal to the carry in. For example, Cp = 1 when A = 0 and B = 1, or when A = 1 and B = 0.
- The carry out of a block can be expressed as a function of Cg, Cp, and the carry in (Ci): Co = Cg + Cp * Ci.
- The carry in of a block can be computed from the carry generate and carry propagate of the previous blocks using a logic circuit called a carry look ahead unit (CLA).
- The CLA can be implemented using a binary tree structure that reduces the number of logic levels and improves the speed of the adder.
- The CLA can also be extended to handle larger adders by using a hierarchical structure that combines multiple CLAs.