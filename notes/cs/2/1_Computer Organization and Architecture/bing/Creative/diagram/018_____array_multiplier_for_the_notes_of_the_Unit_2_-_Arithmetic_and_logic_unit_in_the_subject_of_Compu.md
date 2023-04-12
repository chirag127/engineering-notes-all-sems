### Array Multiplier

- An array multiplier is a digital combinational circuit used for multiplying two binary numbers by employing an array of full adders and half adders .
- This array is used for the nearly simultaneous addition of the various product terms involved.
- To form the various product terms, an array of AND gates is used before the Adder array.
- The design structure of the array multiplier is regular, it is based on the add-shift algorithm principle.
- The add-shift algorithm states that the partial product is equal to the multiplicand multiplied by the multiplier bit.
- The partial products are shifted according to their bit orders and then added using the adders.
- The advantage of the array multiplier is its simplicity and regularity in design.
- The disadvantage of the array multiplier is its high propagation delay, which depends on the number of bits in the operands .
- The propagation delay of an array multiplier can be calculated as follows:

  - Let n be the number of bits in the operands.
  - Let t<sub>AND</sub> be the delay of an AND gate.
  - Let t<sub>HA</sub> be the delay of a half adder.
  - Let t<sub>FA</sub> be the delay of a full adder.
  - Then, the propagation delay of an array multiplier is given by:

    - t<sub>PD</sub> = t<sub>AND</sub> + (n-1)t<sub>HA</sub> + (n-1)(n-2)t<sub>FA</sub>/2

- The following diagram shows an example of a 4x4 array multiplier :

  ```
  A3 A2 A1 A0
  x  B3 B2 B1 B0
  --------------
     A0B0
  A1B0
  A2B0
  A3B0
  +  A0B1
  + A1B1
  + A2B1
  + A3B1
  +  A0B2
  + A1B2
  + A2B2
  + A3B2
  +  A0B3
  + A1B3
  + A2B3
  + A3B3
  --------------
  P7 P6 P5 P4 P3 P2 P1 P0
  ```

  ```
  +---+---+---+---+---+---+---+---+
  | A3| A2| A1| A0|   |   |   |   |
  +---+---+---+---+---+---+---+---+
  |   |   |   |   | B3| B2| B1| B0|
  +---+---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
  | P7| P6| P5| P4| P3| P2| P1| P0|
  +---+---+---+---+---+---+---+---+
  ```

  ```
  +---+---+---+---+---+---+---+---+
  | A3| A2| A1| A0|   |   |   |   |
  +---+---+---+---+---+---+---+---+
  |   |   |   |   | B

```
