### Closure properties of CFL

- A closure property of a class of languages is a property that says that if we apply a certain operation to the languages in the class, we get another language in the same class.
- For example, the closure property of union for CFL says that if L1 and L2 are two CFLs, then L1 ∪ L2 is also a CFL.
- Closure properties are useful for proving that certain languages are or are not CFLs, and for designing algorithms for CFLs.
- Some of the common closure properties of CFLs are:

  - **Union**: CFLs are closed under union, which means that if L1 and L2 are two CFLs, then L1 ∪ L2 is also a CFL. To prove this, we can construct a CFG for L1 ∪ L2 by adding a new start symbol S and two new productions S → S1 | S2, where S1 and S2 are the start symbols of the CFGs for L1 and L2, respectively   .
  - **Concatenation**: CFLs are closed under concatenation, which means that if L1 and L2 are two CFLs, then L1L2 is also a CFL. To prove this, we can construct a CFG for L1L2 by adding a new start symbol S and a new production S → S1S2, where S1 and S2 are the start symbols of the CFGs for L1 and L2, respectively   .
  - **Kleene closure**: CFLs are closed under Kleene closure, which means that if L is a CFL, then L* is also a CFL. To prove this, we can construct a CFG for L* by adding a new start symbol S and two new productions S → ε | SS1, where S1 is the start symbol of the CFG for L   .
  - **Reversal**: CFLs are closed under reversal, which means that if L is a CFL, then LR is also a CFL, where LR is the language obtained by reversing the strings in L. To prove this, we can construct a CFG for LR by reversing the right-hand sides of all the productions in the CFG for L .
  - **Homomorphism**: CFLs are closed under homomorphism, which means that if L is a CFL and h is a homomorphism, then h(L) is also a CFL, where h(L) is the language obtained by applying h to each string in L. A homomorphism is a function that maps each symbol in an alphabet to a string over another alphabet. To prove this, we can construct a CFG for h(L) by replacing each terminal symbol in the CFG for L with the corresponding string given by h .
  - **Inverse homomorphism**: CFLs are closed under inverse homomorphism, which means that if L is a CFL and h is a homomorphism, then h-1(L) is also a CFL, where h-1(L) is the language obtained by applying the inverse of h to each string in L. The inverse of h is a function that maps each string over the target alphabet of h to a string over the source alphabet of h, such that h(h-1(x)) = x for all x. To prove this, we can construct a CFG for h-1(L) by replacing each terminal symbol in the CFG for L with a nonterminal symbol that generates the corresponding string given by h-1 .
  - **Intersection with regular languages**: CFLs are closed under intersection with regular languages, which means that if L1 is a CFL and L2 is a regular language, then L1 ∩ L2 is also a CFL. To prove this, we can construct a PDA for L1 ∩ L2 by simulating the PDA for L1 and the DFA for L2 in parallel, and accepting only when both machines accept .

- Some of the closure properties that CFLs do not have are:

  - **Intersection**: CFLs are not closed under intersection, which means that there exist two CFLs L1 and L2 such that L1 ∩ L2 is not a CFL. A counterexample is L1