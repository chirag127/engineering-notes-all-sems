A finite field of the form GF(p) is a set of integers {0, 1, ..., p-1} where p is a prime number, together with the arithmetic operations of addition, subtraction, multiplication and division modulo p. In other words, the result of any operation is always an integer between 0 and p-1, and the inverse of any nonzero element exists and is also an integer between 0 and p-1. For example, GF(5) is the set {0, 1, 2, 3, 4} with arithmetic modulo 5. In GF(5), 2 + 3 = 0, 4 - 1 = 3, 2 * 3 = 1, and 2 / 3 = 4 (because 3 * 4 = 12 = 2 mod 5).

The following diagram illustrates the basic structure of a finite field of the form GF(p):

```
+-----------------+
|                 |
|  Finite field   |
|                 |
|    GF(p)        |
|                 |
+-----------------+
|                 |
|  Elements:      |
|                 |
|  0, 1, ..., p-1 |
|                 |
+-----------------+
|                 |
|  Operations:    |
|                 |
|  +, -, *, /     |
|                 |
|  modulo p       |
|                 |
+-----------------+
```