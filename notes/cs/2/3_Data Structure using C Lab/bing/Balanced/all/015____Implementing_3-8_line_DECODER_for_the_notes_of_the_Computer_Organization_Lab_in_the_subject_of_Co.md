## Implementing 3-8 line DECODER for the notes of the Computer Organization Lab in the subject of Computer Organization

- A 3-8 line decoder is a digital circuit that converts a 3-bit binary input into an 8-bit output, where only one of the output lines is high (logic 1) and the rest are low (logic 0).
- The 3-bit input represents a decimal number from 0 to 7, and the output line that is high corresponds to that number.
- For example, if the input is 010, the output is 00000100, where the fourth line is high and the rest are low.
- A 3-8 line decoder can be implemented using logic gates, such as AND, OR, and NOT gates.
- The logic expression for each output line can be derived from the truth table of the decoder, where A, B, and C are the input bits and Y0 to Y7 are the output bits.

| A | B | C | Y0 | Y1 | Y2 | Y3 | Y4 | Y5 | Y6 | Y7 |
|---|---|---|----|----|----|----|----|----|----|----|
| 0 | 0 | 0 | 1  | 0  | 0  | 0  | 0  | 0  | 0  | 0  |
| 0 | 0 | 1 | 0  | 1  | 0  | 0  | 0  | 0  | 0  | 0  |
| 0 | 1 | 0 | 0  | 0  | 1  | 0  | 0  | 0  | 0  | 0  |
| 0 | 1 | 1 | 0  | 0  | 0  | 1  | 0  | 0  | 0  | 0  |
| 1 | 0 | 0 | 0  | 0  | 0  | 0  | 1  | 0  | 0  | 0  |
| 1 | 0 | 1 | 0  | 0  | 0  | 0  | 0  | 1  | 0  | 0  |
| 1 | 1 | 0 | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 0  |
| 1 | 1 | 1 | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 1  |

- The logic expressions are:

  - Y0 = A' B' C'
  - Y1 = A' B' C
  - Y2 = A' B C'
  - Y3 = A' B C
  - Y4 = A B' C'
  - Y5 = A B' C
  - Y6 = A B C'
  - Y7 = A B C

- Where A', B', and C' are the complements of A, B, and C, respectively.
- A schematic diagram of the 3-8 line decoder using logic gates is shown below:

```
    A ────┐
         ┌┴┐
         │ │
         │ │
         │ │
         │ │
         │ │
         │ │
         │ │
         │ │
         │ │
         │ │
         │ │
         │ │
         │ │
         └┬┘
    B ────┼────┐
         ┌┴┐  ┌┴┐
         │ │  │ │
         │ │  │ │
         │ │  │ │
         │ │  │ │
         │ │  │ │
         │ │  │ │
         │ │  │ │
         │ │  │ │
         │ │  │ │
         │ │  │ │
         └┬┘  └┬┘
    C ────┼─────┼────┐
         ┌┴┐   ┌┴┐  ┌┴┐
         │ │   │ │  │ │
         │ │   │ │  │ │
         │ │   │ │

```
