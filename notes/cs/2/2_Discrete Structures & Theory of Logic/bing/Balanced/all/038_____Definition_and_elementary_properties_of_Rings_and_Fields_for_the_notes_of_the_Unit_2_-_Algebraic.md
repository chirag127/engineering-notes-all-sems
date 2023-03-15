# Definition and elementary properties of Rings and Fields

## Rings

- A ring is a set R together with two binary operations, usually called addition (+) and multiplication (·), that satisfy the following properties :

  - (R,+) is an abelian group, i.e.,

    - R is closed under addition: for any a,b in R, a+b is also in R.
    - Addition is associative: for any a,b,c in R, (a+b)+c = a+(b+c).
    - Addition is commutative: for any a,b in R, a+b = b+a.
    - There exists an additive identity, denoted by 0, such that for any a in R, a+0 = 0+a = a.
    - For any a in R, there exists an additive inverse, denoted by -a, such that a+(-a) = (-a)+a = 0.

  - R is closed under multiplication: for any a,b in R, a·b is also in R.
  - Multiplication is associative: for any a,b,c in R, (a·b)·c = a·(b·c).
  - Multiplication is distributive over addition: for any a,b,c in R, a·(b+c) = (a·b)+(a·c) and (a+b)·c = (a·c)+(b·c).

- Examples of rings are the set of integers (Z), the set of polynomials (Z[x]), and the set of matrices (Mn(Z)) with addition and multiplication defined in the usual way .

- A ring is called commutative if multiplication is also commutative, i.e., for any a,b in R, a·b = b·a . All the examples above are commutative rings.

- A ring is called a ring with unity or a unitary ring if there exists a multiplicative identity, denoted by 1, such that for any a in R, a·1 = 1·a = a . The rings Z and Z[x] are rings with unity, but Mn(Z) is not for n > 1.

- A nonzero element a in a ring with unity is called a unit if there exists a multiplicative inverse, denoted by a^-1, such that a·a^-1 = a^-1·a = 1 . For example, in Z, the units are ±1, and in Z[x], the units are the nonzero constant polynomials.

- A nonzero element a in a commutative ring is called a zero divisor if there exists a nonzero element b in R such that a·b = 0 . For example, in Z6, 2 and 3 are zero divisors, since 2·3 = 0.

- A commutative ring with unity is called an integral domain if it has no zero divisors  . For example, Z and Z[x] are integral domains, but Z6 is not.

- A subring of a ring (R,+,·) is a subset S of R that is also a ring under the same operations . For example, the set of even integers is a subring of Z.

- A ring homomorphism is a function f from one ring (R,+,·) to another ring (S,⊕,⊗) that preserves the ring operations, i.e.,

  - f(a+b) = f(a) ⊕ f(b) for any a,b in R.
  - f(a·b) = f(a) ⊗ f(b) for any a,b in R.
  - f(0) = 0 and f(1) = 1 if R and S are rings with unity .

- Examples of ring homomorphisms are the evaluation map from Z[x] to Z, defined by f(p(x)) = p(2) for any polynomial p(x), and the determinant map from Mn(Z) to Z, defined by f(A) = det(A) for any matrix A.

## Fields

- A field is a commutative ring with unity that satisfies the following additional property[^2^