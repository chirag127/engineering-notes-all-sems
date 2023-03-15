## Implementing HALF ADDER, FULL ADDER using basic logic gates for the notes of the Computer Organization Lab in the subject of Computer Organization

A half adder is a combinational circuit that performs the addition of two bits. It has two inputs, A and B, and two outputs, Sum and Carry. The Sum output is the result of the addition of the two input bits, while the Carry output indicates if there is a carry generated during the addition.

The truth table for a half adder is as follows:

| A | B | Sum | Carry |
|---|---|-----|-------|
| 0 | 0 |  0  |   0   |
| 0 | 1 |  1  |   0   |
| 1 | 0 |  1  |   0   |
| 1 | 1 |  0  |   1   |

From the truth table, we can derive the following Boolean expressions for the Sum and Carry outputs:

Sum = A XOR B
Carry = A AND B

A half adder can be implemented using basic logic gates such as XOR and AND gates.

A full adder is a combinational circuit that performs the addition of three bits: two input bits and a carry bit from the previous stage of addition. It has three inputs, A, B, and Carry-in, and two outputs, Sum and Carry-out. The Sum output is the result of the addition of the three input bits, while the Carry-out output indicates if there is a carry generated during the addition.

The truth table for a full adder is as follows:

| A | B | Carry-in | Sum | Carry-out |
|---|---|----------|-----|-----------|
| 0 | 0 |    0     |  0  |     0     |
| 0 | 0 |    1     |  1  |     0     |
| 0 | 1 |    0     |  1  |     0     |
| 0 | 1 |    1     |  0  |     1     |
| 1 | 0 |    0     |  1  |     0     |
| 1 | 0 |    1     |  0  |     1     |
| 1 | 1 |    0     |  0  |     1     |
| 1 | 1 |    1     |  1  |     1     |

From the truth table, we can derive the following Boolean expressions for the Sum and Carry-out outputs:

Sum = A XOR B XOR Carry-in
Carry-out = (A AND B) OR (Carry-in AND (A XOR B))

A full adder can be implemented using basic logic gates such as XOR, AND, and OR gates. It can also be implemented using two half adders and an OR gate. The first half adder computes the Sum and Carry outputs for the A and B inputs, while the second half adder computes the Sum and Carry outputs for the Carry-in input and the Sum output of the first half adder. The final Sum output is the Sum output of the second half adder, while the final Carry-out output is the OR of the Carry outputs of the two half adders.