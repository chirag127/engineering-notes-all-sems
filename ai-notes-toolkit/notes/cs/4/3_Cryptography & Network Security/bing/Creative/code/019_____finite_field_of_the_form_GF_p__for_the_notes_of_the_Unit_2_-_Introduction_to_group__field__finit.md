### Finite field of the form GF(p)

- A finite field is a set of elements that can be added, subtracted, multiplied and divided by each other, obeying certain rules called axioms   .
- A finite field has a finite number of elements, denoted by its order. The order of a finite field must be a power of a prime number, i.e., pn, where p is a prime number and n is a positive integer   .
- A finite field of the form GF(p) is a special case where n = 1, i.e., the order of the field is a prime number p    .
- GF(p) is defined as the set of integers {0, 1, ..., p-1} together with arithmetic operations modulo p, i.e., the remainder when dividing by p    .
- For example, GF(5) is the set {0, 1, 2, 3, 4} with arithmetic operations modulo 5. The addition and multiplication tables for GF(5) are shown below:

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

- In GF(p), every nonzero element has a multiplicative inverse, i.e., an element that when multiplied by it gives 1. For example, in GF(5), the inverse of 2 is 3, because 2 x 3 = 6 = 1 (mod 5)   .
- The multiplicative inverse of an element a in GF(p) can be found using the extended Euclidean algorithm, which finds integers x and y such that ax + py = 1. Then, x is the inverse of a (mod p)   .
- Finite fields of the form GF(p) are important in cryptography because they provide a mathematical structure for performing operations on data that are resistant to certain attacks. For example, the Advanced Encryption Standard (AES) uses finite fields of the form GF(2^8^) to encrypt and decrypt data  .