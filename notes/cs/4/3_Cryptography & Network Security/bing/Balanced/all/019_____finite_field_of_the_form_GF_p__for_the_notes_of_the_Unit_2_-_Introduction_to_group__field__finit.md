# Finite field of the form GF(p)

- A finite field is a set of elements that can be added, subtracted, multiplied and divided by each other, obeying certain rules called axioms   .
- A finite field has a finite number of elements, denoted by its order. The order of a finite field must be a power of a prime number, i.e., pn, where p is a prime number and n is a positive integer   .
- A finite field of the form GF(p) is a special case where n = 1, i.e., the order of the field is a prime number p    .
- GF(p) is also called the Galois field, in honor of the founder of finite field theory, Évariste Galois.
- GF(p) can be constructed from the set of integers modulo p, i.e., Zp = {0, 1, ..., p-1}, together with arithmetic operations modulo p   .
- For example, GF(5) is the set {0, 1, 2, 3, 4}, with addition and multiplication modulo 5. The following tables show the addition and multiplication tables for GF(5):

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
  - It has an additive identity element, 0, and a multiplicative identity element, 1   .
  - Every element has an additive inverse, i.e., for any a in GF(p), there exists b in GF(p) such that a + b = 0 (mod p)   .
  - Every nonzero element has a multiplicative inverse, i.e., for any a in GF(p), there exists b in GF(p) such that a x b = 1 (mod p)   . This is also called the multiplicative inverse axiom.
  - It is a field, i.e., it satisfies all the axioms of a field   .
  - It is a cyclic group under both addition and multiplication, i.e., there exists an element g in GF(p) such that every element in GF(p) can be obtained by repeatedly adding or multiplying g by itself   . Such an element g is called a generator or a primitive element of GF(p)   .
  - For example, in