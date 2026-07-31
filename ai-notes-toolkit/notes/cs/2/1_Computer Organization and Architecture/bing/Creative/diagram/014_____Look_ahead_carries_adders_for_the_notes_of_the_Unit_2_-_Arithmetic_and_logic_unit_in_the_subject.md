### Look ahead carries adders

- A look ahead carry adder is a type of adder that reduces the propagation delay by using more complex hardware to compute the carry signals faster.
- The propagation delay is the time taken for the carry signal to propagate from the least significant bit to the most significant bit of the adder.
- A look ahead carry adder divides the adder into blocks and provides circuitry to quickly determine the carry out of a block as soon as the carry in is known.
- The carry out of a block depends on two variables: carry generate and carry propagate .
- Carry generate (Cg) occurs when an output carry is generated internally by the full adder, regardless of the carry in. For example, Cg = 1 when A = 1 and B = 1.
- Carry propagate (Cp) occurs when an output carry is propagated from the carry in, regardless of the internal inputs. For example, Cp = 1 when A = 1 or B = 1.
- The carry out of a block can be expressed as a function of Cg, Cp, and the carry in (Cin) as follows :

  - Cout = Cg + Cp * Cin
- The carry look ahead logic can be implemented using a carry look ahead generator (CLG) that computes the Cg and Cp signals for each block, and a carry look ahead propagator (CLP) that computes the Cout signals for each block using the Cg and Cp signals .
- The CLG and CLP can be designed using two-level logic, such as AND-OR or NAND-NAND gates .
- The advantage of a look ahead carry adder is that it reduces the propagation delay from O(n) to O(log n), where n is the number of bits in the adder .
- The disadvantage of a look ahead carry adder is that it requires more hardware and power than a simple ripple carry adder .

- A diagram of a 4-bit look ahead carry adder is shown below:

```
  A3 A2 A1 A0
+ B3 B2 B1 B0
---------------
  S3 S2 S1 S0
```

```
  Cin
   |
   v
+-----+     +-----+     +-----+     +-----+
| FA3 |     | FA2 |     | FA1 |     | FA0 |
+-----+     +-----+     +-----+     +-----+
   |           |           |           |
   v           v           v           v
  S3          S2          S1          S0
   |           |           |           |
   v           v           v           v
+-----+     +-----+     +-----+     +-----+
| CLG |     | CLG |     | CLG |     | CLG |
+-----+     +-----+     +-----+     +-----+
   |           |           |           |
   v           v           v           v
  Cg3 Cp3    Cg2 Cp2    Cg1 Cp1    Cg0 Cp0
   |   |       |   |       |   |       |   |
   |   +-------+   +-------+   +-------+   |
   |           |           |           |   |
   v           v           v           v   v
+-----+     +-----+     +-----+     +-----+
| CLP |     | CLP |     | CLP |     | CLP |
+-----+     +-----+     +-----+     +-----+
   |           |           |           |
   v           v           v           v
  Cout3      Cout2      Cout1      Cout0
```

- FA: Full adder
- CLG: Carry look ahead generator
- CLP: Carry look ahead propagator
- Cg: Carry generate
- Cp: Carry propagate
- Cin: Carry in
- Cout: Carry out
- S: Sum
- A: Augend
- B: Addend

: https://www.geeksforgeeks.org/carry-look-ahead-adder/
: https://te