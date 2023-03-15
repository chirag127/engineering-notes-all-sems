## Implementation of 4-bit parallel adder using 7483 IC

- A 4-bit parallel adder is a logic circuit that can perform the addition of two 4-bit binary numbers and produce a 4-bit sum and a carry output.
- A 7483 IC is a 16-pin integrated circuit that contains four interconnected full adders and a look-ahead carry circuit. It can be used to implement a 4-bit parallel adder with minimal external components.
- The pin diagram of 7483 IC is shown below:

```
        +---+--+---+
    A4  |1  +--+ 16|  Vcc
    B4  |2       15|  C4
    A3  |3       14|  S4
    B3  |4   74  13|  S3
    A2  |5   83  12|  S2
    B2  |6       11|  S1
    A1  |7       10|  C0
    B1  |8        9|  GND
        +----------+
```

- The inputs A4, A3, A2, A1 and B4, B3, B2, B1 are the two 4-bit numbers to be added. The outputs S4, S3, S2, S1 are the 4-bit sum and C4 is the carry output. C0 is the carry input which can be used to cascade multiple 7483 ICs for larger bit addition. GND and Vcc are the ground and power supply pins respectively.
- The truth table for the 4-bit parallel adder using 7483 IC is given below:

| A4 | A3 | A2 | A1 | B4 | B3 | B2 | B1 | C0 | S4 | S3 | S2 | S1 | C4 |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  |
| 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 0  | 0  | 0  | 1  | 0  |
| 0  | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 0  | 0  | 0  | 0  | 1  | 0  |
| 0  | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 1  | 0  | 0  | 1  | 0  | 0  |
| 0  | 0  | 0  | 0  | 0  | 0  | 1  | 0  | 0  | 0  | 0  | 1  | 0  | 0  |
| 0  | 0  | 0  | 0  | 0  | 0  | 1  | 0  | 1  | 0  | 0  | 1  | 1  | 0  |
| 0  | 0  | 0  | 0  | 0  | 0  | 1  | 1  | 0  | 0  | 0  | 1  | 1  | 0  |
| 0  | 0  | 0  | 0  | 0  | 0  | 1  | 1  | 1  | 0  | 1  | 0  | 0  | 0  |
| 0  | 0  | 0  | 0  | 0  | 1  | 0  | 0  | 0  | 0  | 1  | 0  | 0  |