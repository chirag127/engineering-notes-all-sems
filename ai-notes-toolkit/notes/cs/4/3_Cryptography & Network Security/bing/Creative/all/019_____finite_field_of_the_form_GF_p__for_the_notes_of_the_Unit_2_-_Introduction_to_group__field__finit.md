# Finite field of the form GF(p)

- A finite field is a set of elements that can be added, subtracted, multiplied and divided by each other, obeying certain rules called axioms   .
- A finite field has a finite number of elements, denoted by its order. The order of a finite field must be a power of a prime number, i.e., pn, where p is a prime number and n is a positive integer   .
- A finite field of the form GF(p) is a special case where n = 1, i.e., the order of the field is a prime number p    .
- The elements of GF(p) are the integers from 0 to p-1, i.e., GF(p) = {0, 1, ..., p-1}    .
- The arithmetic operations of GF(p) are performed modulo p, i.e., the remainder of the division by p    .
- For example, GF(5) = {0, 1, 2, 3, 4}, and the addition and multiplication tables are as follows:

| + | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| 0 | 0 | 1 | 2 | 3 | 4 |
| 1 | 1 | 2 | 3 | 4 | 0 |
| 2 | 2 | 3 | 4 | 0 | 1 |
| 3 | 3 | 4 | 0 | 1 | 2 |
| 4 | 4 | 0 | 1 | 2 | 3 |

| x | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 2 | 3 | 4 |
| 2 | 0 | 2 | 4 | 1 | 3 |
| 3 | 0 | 3 | 1 | 4 | 2 |
| 4 | 0 | 4 | 3 | 2 | 1 |

- Some properties of GF(p) are:
  - It is a commutative ring, i.e., it satisfies the axioms of closure, associativity, commutativity and distributivity for both addition and multiplication   .
  - It has an additive identity (0) and a multiplicative identity (1), i.e., for any element a in GF(p), a + 0 = a and a x 1 = a   .
  - It has additive inverses and multiplicative inverses for all nonzero elements, i.e., for any element a in GF(p), there exists an element b in GF(p) such that a + b = 0 and a x b = 1   .
  - It is a field, i.e., it satisfies all the axioms of a field   .
  - It is a cyclic group under both addition and multiplication, i.e., there exists an element g in GF(p) such that every element in GF(p) can be obtained by repeated addition or multiplication of g   .
  - It is a Galois field, i.e., it is the smallest field that contains GF(p) as a subfield    .
- Finite fields of the form GF(p) are important in cryptography because they provide a simple and efficient way of performing arithmetic