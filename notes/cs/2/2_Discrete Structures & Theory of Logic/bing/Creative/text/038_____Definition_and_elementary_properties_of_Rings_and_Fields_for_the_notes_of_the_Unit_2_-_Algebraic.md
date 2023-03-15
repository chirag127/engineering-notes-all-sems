### Definition and elementary properties of Rings and Fields

- A **ring** is a set \\(R\\) equipped with two binary operations, usually called **addition** and **multiplication**, such that the following properties hold for all \\(a, b, c \in R\\):

  - \\(R\\) is an **abelian group** under addition, i.e., \\(a + b = b + a\\), \\(a + (b + c) = (a + b) + c\\), there exists a **zero element** \\(0\\) such that \\(a + 0 = a\\), and there exists an **additive inverse** \\(-a\\) such that \\(a + (-a) = 0\\).
  - Multiplication is **associative**, i.e., \\(a \cdot (b \cdot c) = (a \cdot b) \cdot c\\).
  - Multiplication is **distributive** over addition, i.e., \\(a \cdot (b + c) = a \cdot b + a \cdot c\\) and \\((a + b) \cdot c = a \cdot c + b \cdot c\\).

- A ring is called **commutative** if multiplication is also commutative, i.e., \\(a \cdot b = b \cdot a\\) for all \\(a, b \in R\\).
- A ring is called **unital** or **unitary** if it has a **multiplicative identity** \\(1\\) such that \\(a \cdot 1 = 1 \cdot a = a\\) for all \\(a \in R\\).
- A ring is called an **integral domain** if it is commutative, unital, and has **no zero divisors**, i.e., if \\(a \cdot b = 0\\) then either \\(a = 0\\) or \\(b = 0\\).
- A **field** is a ring that is commutative, unital, and has **multiplicative inverses** for all nonzero elements, i.e., for every \\(a \neq 0\\) there exists \\(a^{-1}\\) such that \\(a \cdot a^{-1} = a^{-1} \cdot a = 1\\).

- Some examples of rings are:

  - The set of integers \\(\mathbb{Z}\\) with the usual addition and multiplication is a commutative, unital ring, but not a field, since not every nonzero integer has a multiplicative inverse in \\(\mathbb{Z}\\).
  - The set of polynomials \\(R[x]\\) with coefficients in a ring \\(R\\) and the usual polynomial addition and multiplication is a ring. It is commutative and unital if \\(R\\) is commutative and unital. It is an integral domain if \\(R\\) is an integral domain.
  - The set of \\(n \times n\\) square matrices with entries in a ring \\(R\\) and the usual matrix addition and multiplication is a ring. It is commutative and unital if \\(R\\) is commutative and unital and \\(n = 1\\). It is never an integral domain if \\(n > 1\\), since there are nonzero matrices that multiply to zero.

- Some examples of fields are:

  - The set of rational numbers \\(\mathbb{Q}\\), the set of real numbers \\(\mathbb{R}\\), and the set of complex numbers \\(\mathbb{C}\\) with the usual addition and multiplication are fields.
  - The set of integers modulo a prime number \\(p\\), denoted by \\(\mathbb{Z}_p\\) or \\(\mathbb{F}_p\\), with addition and multiplication defined by taking the remainder after dividing by \\(p\\), is a field. For example, \\(\mathbb{Z}_2\\) is the field with two elements \\(0\\) and \\(1\\), where \\(1 + 1 = 0\\) and \\(1 \cdot 1 = 1\\).
  - The set of polynomials \\(\mathbb{F}_p[x]\\) with coefficients in \\(\mathbb{F}_p\\) and the usual polynomial addition and multiplication is not a field, but it contains some subfields of