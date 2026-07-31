### Definition and elementary properties of Rings and Fields

- A **ring** is a set R with two binary operations, usually called **addition** and **multiplication**, that satisfy the following properties  :

  - (R,+) is an **abelian group**, meaning that:
    - Addition is **associative**: (a+b)+c = a+(b+c) for all a,b,c in R
    - Addition is **commutative**: a+b = b+a for all a,b in R
    - There is an **additive identity** element 0 in R such that a+0 = a for all a in R
    - There is an **additive inverse** element -a in R for each a in R such that a+(-a) = 0
  - Multiplication is **associative**: (a·b)·c = a·(b·c) for all a,b,c in R
  - Multiplication is **distributive** over addition: a·(b+c) = a·b + a·c and (a+b)·c = a·c + b·c for all a,b,c in R
  - Optionally, multiplication may also be **commutative**: a·b = b·a for all a,b in R. A ring with this property is called a **commutative ring**.

- A **field** is a ring with additional properties that make it behave like the set of rational, real or complex numbers  :

  - Multiplication is **commutative**: a·b = b·a for all a,b in R. A field is always a commutative ring.
  - There is a **multiplicative identity** element 1 in R such that a·1 = a for all a in R and 1 is not equal to 0
  - There is a **multiplicative inverse** element a^-1^ in R for each a in R that is not 0 such that a·a^-1^ = 1
  - A field has no **zero divisors**, meaning that if a·b = 0 for some a,b in R, then either a = 0 or b = 0

- Some examples of rings are:

  - The set of integers Z with the usual addition and multiplication
  - The set of polynomials with coefficients in a field F with the usual addition and multiplication of polynomials
  - The set of 2x2 matrices with entries in a field F with the usual matrix addition and multiplication
  - The set of even integers 2Z with the usual addition and multiplication

- Some examples of fields are:

  - The set of rational numbers Q with the usual addition and multiplication
  - The set of real numbers R with the usual addition and multiplication
  - The set of complex numbers C with the usual addition and multiplication
  - The set of integers modulo a prime p, denoted by Z_p, with the addition and multiplication defined by taking the remainder after dividing by p

- Some elementary properties of rings and fields are:

  - The additive identity 0 and the additive inverse -a are unique for each a in R
  - The multiplicative identity 1 and the multiplicative inverse a^-1^ are unique for each a in R that is not 0
  - The additive identity 0 and the multiplicative identity 1 are the same in any ring or field
  - The additive inverse -a and the multiplicative inverse a^-1^ are not the same in general, unless a = -1
  - The distributive law implies that 0·a = a·0 = 0 for all a in R
  - The distributive law also implies that (-a)·b = a·(-b) = -(a·b) and (-a)·(-b) = a·b for all a,b in R
  - If R is a commutative ring, then (a+b)^2^ = a^2^ + 2ab + b^2^ and (a-b)^2^ = a^2^ - 2ab + b^2^ for all a,b in R
  - If R is a field, then (a+b)^-1^ = a^-1^ + b^-1^ - a^-1^b^-1^ and (a-b)^-1^ = a^-