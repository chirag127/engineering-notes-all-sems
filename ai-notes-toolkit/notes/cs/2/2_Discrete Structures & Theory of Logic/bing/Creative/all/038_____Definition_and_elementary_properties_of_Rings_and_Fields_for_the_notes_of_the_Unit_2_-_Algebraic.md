# Definition and elementary properties of Rings and Fields

## Rings

- A ring is a set R together with two binary operations, usually called addition (+) and multiplication (·), that satisfy the following properties :

  - (R,+) is an abelian group, i.e., addition is associative, commutative, has an identity element (denoted by 0), and every element has an additive inverse.
  - Multiplication is associative and has an identity element (denoted by 1).
  - Multiplication distributes over addition, i.e., for any a, b, c in R, we have a · (b + c) = (a · b) + (a · c) and (a + b) · c = (a · c) + (b · c).

- Examples of rings are the set of integers (Z), the set of polynomials (Z[x]), and the set of matrices (Mn(Z)) with integer entries .
- A ring is called commutative if multiplication is also commutative, i.e., for any a, b in R, we have a · b = b · a . All the examples above are commutative rings.
- A ring is called a field if every nonzero element has a multiplicative inverse, i.e., for any a in R, a ≠ 0, there exists b in R such that a · b = b · a = 1 . A field is also a commutative ring.

## Fields

- A field is a set F together with two binary operations, usually called addition (+) and multiplication (·), that satisfy the following properties :

  - (F,+) is an abelian group, i.e., addition is associative, commutative, has an identity element (denoted by 0), and every element has an additive inverse.
  - (F \ {0}, ·) is an abelian group, i.e., multiplication is associative, commutative, has an identity element (denoted by 1), and every nonzero element has a multiplicative inverse.
  - Multiplication distributes over addition, i.e., for any a, b, c in F, we have a · (b + c) = (a · b) + (a · c) and (a + b) · c = (a · c) + (b · c).

- Examples of fields are the set of rational numbers (Q), the set of real numbers (R), and the set of complex numbers (C) .
- A field is a special case of a ring, where every nonzero element is a unit, i.e., has a multiplicative inverse .
- A field is also a vector space over itself, i.e., it has a scalar multiplication that is compatible with the field operations .