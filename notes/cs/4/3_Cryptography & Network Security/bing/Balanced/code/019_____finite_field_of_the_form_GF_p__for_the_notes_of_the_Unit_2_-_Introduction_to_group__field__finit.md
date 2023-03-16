### Finite field of the form GF(p)

- A finite field is a set of elements that can be added, subtracted, multiplied and divided by each other, obeying certain rules called axioms   .
- A finite field has a finite number of elements, denoted by its order. The order of a finite field must be a power of a prime number, i.e. pn, where p is a prime number and n is a positive integer   .
- A finite field of the form GF(p) is a special case where n = 1, i.e. the order of the field is a prime number p. In this case, the elements of the field are the integers from 0 to p-1, and the arithmetic operations are performed modulo p    .
- For example, GF(5) is a finite field of order 5, with elements {0, 1, 2, 3, 4}. The addition, subtraction, multiplication and division operations are defined as follows:

| + | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| 0 | 0 | 1 | 2 | 3 | 4 |
| 1 | 1 | 2 | 3 | 4 | 0 |
| 2 | 2 | 3 | 4 | 0 | 1 |
| 3 | 3 | 4 | 0 | 1 | 2 |
| 4 | 4 | 0 | 1 | 2 | 3 |

| - | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| 0 | 0 | 4 | 3 | 2 | 1 |
| 1 | 1 | 0 | 4 | 3 | 2 |
| 2 | 2 | 1 | 0 | 4 | 3 |
| 3 | 3 | 2 | 1 | 0 | 4 |
| 4 | 4 | 3 | 2 | 1 | 0 |

| x | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 2 | 3 | 4 |
| 2 | 0 | 2 | 4 | 1 | 3 |
| 3 | 0 | 3 | 1 | 4 | 2 |
| 4 | 0 | 4 | 3 | 2 | 1 |

| / | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| 0 | - | 0 | 0 | 0 | 0 |
| 1 | - | 1 | 3 | 2 | 4 |
| 2 | - | 2 | 1 | 4 | 3 |
| 3 | - | 3 | 4 | 1 | 2 |
| 4 | - | 4 | 2 | 3 | 1 |

- Note that 0 has no multiplicative inverse, so division by 0 is undefined. Also note that the operations are commutative, associative and distributive, and that there are additive and multiplicative identities (0 and 1) and inverses for every non-zero element   .
- Finite fields of the form GF(p) are important in cryptography because they provide a simple and efficient way to perform arithmetic operations on large numbers, and they have some useful properties such as Fermat's little theorem and Euler's theorem   .