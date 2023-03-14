### Finite field of the form GF(p)

- A finite field is a set of elements that obey certain algebraic rules, such as commutativity, associativity, distributivity, identity, and inverse for both addition and multiplication operations.
- A finite field has a finite number of elements, and its order (size) must be a power of a prime number, denoted by pn, where p is a prime number and n is a positive integer.
- A finite field of the form GF(p) is a special case where n = 1, and p is a prime number. It is also called a prime field.
- A finite field of the form GF(p) consists of the set of integers {0, 1, ..., p-1}, together with the arithmetic operations modulo p. That is, the addition and multiplication of any two elements in the field are performed by taking the remainder after dividing by p.
- For example, GF(7) is a finite field of order 7, and its elements are {0, 1, 2, 3, 4, 5, 6}. The addition and multiplication operations are shown in the following tables:

| + | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| 0 | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| 1 | 1 | 2 | 3 | 4 | 5 | 6 | 0 |
| 2 | 2 | 3 | 4 | 5 | 6 | 0 | 1 |
| 3 | 3 | 4 | 5 | 6 | 0 | 1 | 2 |
| 4 | 4 | 5 | 6 | 0 | 1 | 2 | 3 |
| 5 | 5 | 6 | 0 | 1 | 2 | 3 | 4 |
| 6 | 6 | 0 | 1 | 2 | 3 | 4 | 5 |

| x | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| 2 | 0 | 2 | 4 | 6 | 1 | 3 | 5 |
| 3 | 0 | 3 | 6 | 2 | 5 | 1 | 4 |
| 4 | 0 | 4 | 1 | 5 | 2 | 6 | 3 |
| 5 | 0 | 5 | 3 | 1 | 6 | 4 | 2 |
| 6 | 0 | 6 | 5 | 4 | 3 | 2 | 1 |

- A finite field of the form GF(p) has the following properties:
  - The additive identity is 0, and the multiplicative identity is 1. That is, for any element a in the field, a + 0 = 0 + a = a, and a x 1 = 1 x a = a.
  - Every element in the field has an additive inverse and a multiplicative inverse, except for 0, which has no multiplicative inverse. That is, for any element a in the field, there exists an element b such that a + b = b + a = 0, and there exists an element c such that a x c = c x a = 1, unless a = 0.
  - The additive inverse of an element a is denoted by -a, and the multiplicative inverse of an element a is denoted by a^-1. For example, in GF(7), the additive inverse of 3 is -3, which is equivalent to 4 modulo 7, and the multiplicative inverse of 3 is 3^-1, which is equivalent to 5 modulo 7, because 3 x 5 = 15 = 1 modulo 7.
  - The arithmetic operations in the field are commutative, associative, and distributive. That