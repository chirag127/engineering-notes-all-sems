### Definition and elementary properties of Rings and Fields

#### Rings

- A **ring** is a set R with two binary operations, usually called **addition** and **multiplication**, that satisfy the following properties  :
  - **Closure**: For all a, b in R, a + b and a * b are also in R.
  - **Associativity**: For all a, b, c in R, (a + b) + c = a + (b + c) and (a * b) * c = a * (b * c).
  - **Commutativity**: For all a, b in R, a + b = b + a and a * b = b * a.
  - **Identity**: There exist two distinct elements 0 and 1 in R such that for all a in R, a + 0 = 0 + a = a and a * 1 = 1 * a = a.
  - **Inverse**: For every a in R, there exists an element -a in R such that a + (-a) = (-a) + a = 0.
  - **Distributivity**: For all a, b, c in R, a * (b + c) = (a * b) + (a * c) and (b + c) * a = (b * a) + (c * a).

- Examples of rings are the set of integers Z, the set of polynomials P, and the set of matrices M  .
- A ring is called **commutative** if its multiplication is commutative, i.e., for all a, b in R, a * b = b * a  .
- A ring is called **integral** or **integral domain** if it has no **zero divisors**, i.e., for all a, b in R, if a * b = 0, then either a = 0 or b = 0  .

#### Fields

- A **field** is a commutative ring with an additional property that every nonzero element has a **multiplicative inverse**, i.e., for every a in R, a ≠ 0, there exists an element a^-1 in R such that a * a^-1 = a^-1 * a = 1   .
- Examples of fields are the set of rational numbers Q, the set of real numbers R, and the set of complex numbers C   .
- A field is called **finite** if it has a finite number of elements, and **infinite** otherwise  .
- A field is called **algebraically closed** if every polynomial with coefficients in the field has a root in the field  .