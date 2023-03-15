### Definition and elementary properties of Rings and Fields

A ring is a set R with two binary operations, usually called addition (+) and multiplication (·), that satisfy the following properties  :

- (R,+) is an abelian group, meaning that:
  - + is associative: (a+b)+c = a+(b+c) for all a,b,c in R
  - + is commutative: a+b = b+a for all a,b in R
  - There is an additive identity element 0 in R such that a+0 = a for all a in R
  - For every a in R, there is an additive inverse element -a in R such that a+(-a) = 0
- · is associative: (a·b)·c = a·(b·c) for all a,b,c in R
- · is distributive over +: a·(b+c) = (a·b)+(a·c) and (a+b)·c = (a·c)+(b·c) for all a,b,c in R

Some examples of rings are:

- The set of integers Z with the usual addition and multiplication
- The set of polynomials with coefficients in a ring R, denoted by R[x], with the usual addition and multiplication of polynomials
- The set of matrices with entries in a ring R, denoted by M_n(R), with the usual addition and multiplication of matrices

A ring is called commutative if · is also commutative: a·b = b·a for all a,b in R  . All the examples above are commutative rings.

A ring is called a ring with unity or a unitary ring if it has a multiplicative identity element 1 in R such that a·1 = 1·a = a for all a in R  . The examples above are also rings with unity.

A ring is called an integral domain if it is a commutative ring with unity and has no zero divisors, meaning that if a·b = 0 for some a,b in R, then either a = 0 or b = 0   . The first two examples above are integral domains, but the third one is not, since there are non-zero matrices that multiply to zero.

A field is a commutative ring with unity that also satisfies the following property   :

- For every non-zero a in R, there is a multiplicative inverse element a^-1 in R such that a·a^-1 = a^-1·a = 1

Some examples of fields are:

- The set of rational numbers Q with the usual addition and multiplication
- The set of real numbers R with the usual addition and multiplication
- The set of complex numbers C with the usual addition and multiplication
- The set of integers modulo a prime p, denoted by Z_p, with the addition and multiplication defined by the remainder after division by p

Fields are special cases of integral domains, and integral domains are special cases of rings. Fields have the most structure and the most properties among these algebraic structures.