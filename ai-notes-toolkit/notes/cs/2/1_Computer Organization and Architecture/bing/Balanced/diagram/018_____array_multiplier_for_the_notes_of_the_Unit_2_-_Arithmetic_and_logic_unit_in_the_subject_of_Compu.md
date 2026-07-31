### Array Multiplier

- An array multiplier is a digital combinational circuit used for multiplying two binary numbers by employing an array of full adders and half adders .
- This array is used for the nearly simultaneous addition of the various product terms involved.
- To form the various product terms, an array of AND gates is used before the Adder array.
- The design structure of the array multiplier is regular, it is based on the add shift algorithm principle.
- The add shift algorithm states that the partial product is equal to the multiplicand multiplied by the multiplier bit.
- The partial product is shifted according to their bit orders and then added using full adders and half adders.
- The advantage of the array multiplier is its simplicity and regularity in design .
- The disadvantage of the array multiplier is its high propagation delay, which depends on the number of bits in the operands .
- The propagation delay can be calculated by counting the number of gates from the inputs to the outputs along the longest path.
- For example, a 4x4 array multiplier has a propagation delay of 8 units, as shown in the diagram below.

```
    A3 A2 A1 A0
    B3 B2 B1 B0
    ------------
    P0  P1  P2  P3
    P4  P5  P6  P7
    P8  P9  P10 P11
    P12 P13 P14 P15
    ------------
    S0  S1  S2  S3  S4  S5  S6  S7

    P0  = A0 AND B0
    P1  = A1 AND B0
    P2  = A2 AND B0
    P3  = A3 AND B0
    P4  = A0 AND B1
    P5  = A1 AND B1
    P6  = A2 AND B1
    P7  = A3 AND B1
    P8  = A0 AND B2
    P9  = A1 AND B2
    P10 = A2 AND B2
    P11 = A3 AND B2
    P12 = A0 AND B3
    P13 = A1 AND B3
    P14 = A2 AND B3
    P15 = A3 AND B3

    S0 = P0
    S1 = P1 XOR P4
    S2 = P2 XOR P5 XOR P8
    S3 = P3 XOR P6 XOR P9 XOR P12
    S4 = P7 XOR P10 XOR P13
    S5 = P11 XOR P14
    S6 = P15
    S7 = Carry out

    The longest path is from A3 and B3 to S7, which passes through 8 gates:

    A3 -> AND -> P15 -> FA -> S6 -> FA -> S5 -> FA -> S4 -> FA -> S7
    B3 -> AND -> P15 -> FA -> S6 -> FA -> S5 -> FA -> S4 -> FA -> S7
```