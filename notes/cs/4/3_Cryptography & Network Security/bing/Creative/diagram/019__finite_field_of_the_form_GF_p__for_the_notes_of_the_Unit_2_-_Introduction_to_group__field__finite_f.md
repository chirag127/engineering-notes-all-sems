A finite field of the form GF(p) is a set of integers {0, 1, ..., p-1} where p is a prime number, together with the arithmetic operations of addition, subtraction, multiplication and division modulo p. A finite field of the form GF(p) has the following properties:

- It is closed under addition, subtraction, multiplication and division, meaning that the result of any of these operations on two elements of the field is also an element of the field.
- It is commutative, meaning that the order of the operands does not affect the result of any of the operations.
- It is associative, meaning that the grouping of the operands does not affect the result of any of the operations.
- It has an additive identity, which is 0, meaning that adding 0 to any element of the field does not change its value.
- It has a multiplicative identity, which is 1, meaning that multiplying 1 by any element of the field does not change its value.
- It has additive inverses, meaning that for every element a in the field, there exists an element -a such that a + (-a) = 0.
- It has multiplicative inverses, meaning that for every nonzero element a in the field, there exists an element a^-1 such that a * a^-1 = 1.
- It satisfies the distributive property, meaning that a * (b + c) = (a * b) + (a * c) for any elements a, b and c in the field.

The following diagram illustrates the basic structure of a finite field of the form GF(p) using ASCII characters:

```
+---------------------+
| Finite field of the |
| form GF(p)          |
+---------------------+
|                     |
| 0 1 2 ... p-2 p-1   |
|                     |
+---------------------+
|                     |
| + - * / mod p       |
|                     |
+---------------------+
```