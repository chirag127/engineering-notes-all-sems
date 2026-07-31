### Binary arithmetic

Binary arithmetic is the set of rules for performing arithmetic operations on numbers represented in binary form. Binary numbers have only two digits: 0 and 1. Binary arithmetic operations include binary addition, binary subtraction, binary multiplication, and binary division. These operations are simpler than decimal arithmetic operations because they involve fewer cases to consider. However, they also require more bits to represent the same range of values as decimal numbers.

#### Binary addition

Binary addition is the simplest and most basic operation of binary arithmetic. It follows four rules based on the truth table below:

| A | B | Sum | Carry |
|---|---|-----|-------|
| 0 | 0 |  0  |   0   |
| 0 | 1 |  1  |   0   |
| 1 | 0 |  1  |   0   |
| 1 | 1 |  0  |   1   |

- Rule 1: 0 + 0 = 0
- Rule 2: 0 + 1 = 1
- Rule 3: 1 + 0 = 1
- Rule 4: 1 + 1 = 0, with a carry of 1 to the next higher bit

To perform binary addition, we align the two numbers to be added and start from the rightmost bit. We apply the rules above and write the sum bit below the corresponding bits. If there is a carry, we add it to the next pair of bits. We repeat this process until we reach the leftmost bit. If there is a final carry, we write it as the most significant bit of the result.

For example, to add 1011 and 1101 in binary, we do the following:

```
  1011
+ 1101
------
 11000
```

We start from the rightmost bit and apply the rules:

- 1 + 1 = 0, with a carry of 1
- 1 + 0 + 1 (carry) = 0, with a carry of 1
- 0 + 1 + 1 (carry) = 0, with a carry of 1
- 1 + 1 + 1 (carry) = 1, with a carry of 1
- The final carry is written as the most significant bit of the result

Therefore, 1011 + 1101 = 11000 in binary.

#### Binary subtraction

Binary subtraction is the inverse operation of binary addition. It follows four rules based on the truth table below:

| A | B | Difference | Borrow |
|---|---|------------|--------|
| 0 | 0 |     0      |   0    |
| 0 | 1 |     1      |   1    |
| 1 | 0 |     1      |   0    |
| 1 | 1 |     0      |   0    |

- Rule 1: 0 - 0 = 0
- Rule 2: 0 - 1 = 1, with a borrow of 1 from the adjacent bit to the left
- Rule 3: 1 - 0 = 1
- Rule 4: 1 - 1 = 0

To perform binary subtraction, we align the two numbers to be subtracted and start from the rightmost bit. We apply the rules above and write the difference bit below the corresponding bits. If there is a borrow, we subtract it from the next pair of bits. We repeat this process until we reach the leftmost bit. If there is a final borrow, we discard it as it indicates an overflow or an underflow.

For example, to subtract 1001 from 1100 in binary, we do the following:

```
  1100
- 1001
------
  0011
```

We start from the rightmost bit and apply the rules:

- 0 - 1 = 1, with a borrow of 1
- 0 - 0 - 1 (borrow) = 1, with a borrow of 1
- 1 - 0 - 1 (borrow) = 0
- 1 - 1 = 0

Therefore, 1100 - 1001 = 0011 in binary.

#### Binary multiplication

Binary multiplication is the repeated addition of one number by another number. It follows two rules based on the truth table below: