### Definition and elementary properties of Rings and Fields

- A **ring** is a set R with two binary operations, usually called **addition** and **multiplication**, that satisfy the following properties   :

  - (R,+) is an **abelian group**, meaning that:
    - **Closure**: For all a,b in R, a+b is also in R.
    - **Associativity**: For all a,b,c in R, (a+b)+c = a+(b+c).
    - **Commutativity**: For all a,b in R, a+b = b+a.
    - **Identity**: There exists an element 0 in R such that for all a in R, a+0 = a.
    - **Inverse**: For every a in R, there exists an element -a in R such that a+(-a) = 0.
  - (R,.) is a **semigroup**, meaning that:
    - **Closure**: For all a,b in R, a.b is also in R.
    - **Associativity**: For all a,b,c in R, (a.b).c = a.(b.c).
  - **Distributivity**: For all a,b,c in R, a.(b+c) = (a.b)+(a.c) and (a+b).c = (a.c)+(b.c).

- A ring is called **commutative** if its multiplication is also commutative, that is, for all a,b in R, a.b = b.a   .

- A ring is called **unital** or **unitary** if it has a **multiplicative identity**, that is, there exists an element 1 in R such that for all a in R, a.1 = 1.a = a   .

- A ring is called an **integral domain** if it is commutative, unital, and has no **zero divisors**, that is, for all a,b in R, if a.b = 0, then either a = 0 or b = 0   .

- A **field** is a ring that is commutative, unital, and has **multiplicative inverses**, that is, for every nonzero a in R, there exists an element a^-1 in R such that a.a^-1 = a^-1.a = 1   .

- Examples of rings are the integers Z, the rational numbers Q, the real numbers R, the complex numbers C, the polynomials R[x], and the matrices M_n(R) with n rows and columns and entries from R   .

- Examples of fields are the rational numbers Q, the real numbers R, the complex numbers C, and the finite fields F_p with p elements, where p is a prime number   .

- Some elementary properties of rings and fields are:

  - In any ring, 0.a = a.0 = 0 for all a in R   .
  - In any ring, (-a).b = a.(-b) = -(a.b) for all a,b in R   .
  - In any ring, (-a).(-b) = a.b for all a,b in R   .
  - In any ring, if 1 exists, then 1 = -1 if and only if R has exactly two elements   .
  - In any ring, if a.b = a.c and a is not a zero divisor, then b = c for all a,b,c in R   .
  - In any field, every nonzero element is a unit, and every unit is nonzero [