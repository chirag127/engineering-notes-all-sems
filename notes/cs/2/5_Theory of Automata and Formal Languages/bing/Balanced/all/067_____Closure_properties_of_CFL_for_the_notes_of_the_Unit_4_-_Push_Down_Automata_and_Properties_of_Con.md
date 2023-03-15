# Closure properties of CFL

- A closure property of a class of languages is a property that says that if we apply a certain operation to the languages in the class, we get another language in the same class.
- For example, the closure property of union for CFLs says that if we take the union of two CFLs, we get another CFL.
- Closure properties are useful for proving that certain languages are or are not CFLs, and for constructing CFGs for languages that are CFLs.
- Some of the common closure properties of CFLs are:

  - **Union**: If L1 and L2 are CFLs, then L1 ∪ L2 is also a CFL. To prove this, we can construct a CFG for L1 ∪ L2 by adding a new start symbol S and two new productions S → S1 | S2, where S1 and S2 are the start symbols of the CFGs for L1 and L2, respectively   .
  - **Concatenation**: If L1 and L2 are CFLs, then L1 L2 is also a CFL. To prove this, we can construct a CFG for L1 L2 by adding a new start symbol S and a new production S → S1 S2, where S1 and S2 are the start symbols of the CFGs for L1 and L2, respectively   .
  - **Kleene closure**: If L is a CFL, then L* is also a CFL. To prove this, we can construct a CFG for L* by adding a new start symbol S and two new productions S → ε | S1 S, where S1 is the start symbol of the CFG for L   .
  - **Reversal**: If L is a CFL, then LR is also a CFL, where LR is the language obtained by reversing the strings in L. To prove this, we can construct a CFG for LR by reversing the right-hand sides of all the productions in the CFG for L .
  - **Homomorphism**: If L is a CFL and h is a homomorphism, then h(L) is also a CFL, where h(L) is the language obtained by applying h to each string in L. A homomorphism is a function that maps each symbol in an alphabet to a string over another alphabet. To prove this, we can construct a CFG for h(L) by replacing each symbol in the right-hand sides of the productions in the CFG for L with the corresponding string given by h .
  - **Inverse homomorphism**: If L is a CFL and h is a homomorphism, then h-1(L) is also a CFL, where h-1(L) is the language obtained by applying the inverse of h to each string in L. The inverse of h is a function that maps each string over the target alphabet of h to a string over the source alphabet of h, such that h(h-1(x)) = x for all x in the target alphabet. To prove this, we can construct a CFG for h-1(L) by replacing each string in the right-hand sides of the productions in the CFG for L with the corresponding symbol given by h-1 .

- Some of the properties that CFLs are not closed under are:

  - **Intersection**: If L1 and L2 are CFLs, then L1 ∩ L2 may or may not be a CFL. A counterexample is L1 = {an bn cn | n ≥ 0} and L2 = {an bn | n ≥ 0}, which are both CFLs, but their intersection L1 ∩ L2 = {an bn bn | n ≥ 0} is not a CFL .
  - **Difference**: If L1 and L2 are CFLs, then L1 - L2 may or may not be a CFL. A counterexample is L1 = {an bn cn | n ≥ 0} and L2 = {an bn | n ≥ 0}, which are both CFLs, but their difference L1 - L2 = {an bn cn | n > 0} is not a CFL .
  - **Complement**: If