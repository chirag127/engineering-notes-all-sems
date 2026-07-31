# Binary arithmetic

Binary arithmetic is a set of rules for performing arithmetic operations on numbers represented in binary form. Binary numbers have only two digits: 0 and 1. Binary arithmetic operations include binary addition, binary subtraction, binary multiplication, and binary division. These operations are simpler than decimal arithmetic operations because they involve fewer cases and rules.

## Binary addition

Binary addition is the simplest and most basic operation of binary arithmetic. It is used to add two binary numbers and produce a binary sum. The rules of binary addition are based on the truth table shown below:

| A | B | Carry | Sum |
|---|---|-------|-----|
| 0 | 0 | 0     | 0   |
| 0 | 1 | 0     | 1   |
| 1 | 0 | 0     | 1   |
| 1 | 1 | 1     | 0   |

The carry bit is generated when both the bits are 1 and is added to the next pair of bits. The sum bit is the result of the exclusive OR (XOR) operation on the two bits. Binary addition is performed from right to left, starting from the least significant bit (LSB).

For example, to add 1011 and 1101, we follow these steps:

| Step | A    | B    | Carry | Sum  |
|------|------|------|-------|------|
| 1    | 1011 | 1101 | 0     |      |
| 2    | 1011 | 1101 | 0     | 0    |
| 3    | 1011 | 1101 | 1     | 10   |
| 4    | 1011 | 1101 | 1     | 000  |
| 5    | 1011 | 1101 | 1     | 1000 |

The final sum is 10000.

## Binary subtraction

Binary subtraction is another basic operation of binary arithmetic. It is used to subtract one binary number from another and produce a binary difference. The rules of binary subtraction are based on the truth table shown below:

| A | B | Borrow | Difference |
|---|---|--------|------------|
| 0 | 0 | 0      | 0          |
| 0 | 1 | 1      | 1          |
| 1 | 0 | 0      | 1          |
| 1 | 1 | 0      | 0          |

The borrow bit is generated when the first bit is 0 and the second bit is 1 and is subtracted from the next pair of bits. The difference bit is the result of the XOR operation on the two bits. Binary subtraction is performed from right to left, starting from the LSB.

For example, to subtract 1010 from 1100, we follow these steps:

| Step | A    | B    | Borrow | Difference |
|------|------|------|--------|------------|
| 1    | 1100 | 1010 | 0      |            |
| 2    | 1100 | 1010 | 0      | 0          |
| 3    | 1100 | 1010 | 0      | 10         |
| 4    | 1100 | 1010 | 1      | 010        |
| 5    | 1100 | 1010 | 0      | 0010       |

The final difference is 10.

## Binary multiplication

Binary multiplication is a more complex operation of binary arithmetic. It is used to multiply two binary numbers and produce a binary product. The rules of binary multiplication are based on the truth table shown below:

| A | B | Product |
|---|---|---------|
| 0 | 0 | 0       |
| 0 | 1 | 0       |
| 1 | 0 | 0       |
| 1 | 1 | 1       |

The product bit is the result of the AND operation on the two bits. Binary multiplication is performed by multiplying each bit of the first number by each bit of the second number and adding the partial products. The partial products are shifted left by one bit for each position of the multiplier.

For example, to multiply 101 and 110, we follow these steps:

| Step | A   | B   | Partial product |
|------|-----|-----|-----------------|
| 1