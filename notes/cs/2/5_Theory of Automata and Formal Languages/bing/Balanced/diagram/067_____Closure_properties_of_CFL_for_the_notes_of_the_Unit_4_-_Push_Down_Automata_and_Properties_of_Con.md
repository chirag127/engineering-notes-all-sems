### Closure properties of CFL

- A closure property of a class of languages is a property that says that if we apply a certain operation to the languages in the class, we get another language in the same class.
- For example, the closure property of union for CFL says that if L1 and L2 are CFLs, then L1 ∪ L2 is also a CFL.
- Closure properties are useful for proving that certain languages are or are not CFLs, and for constructing CFGs for languages that are CFLs.
- Some of the common closure properties of CFLs are:

  - **Union**: If L1 and L2 are CFLs, then L1 ∪ L2 is also a CFL. This can be proved by constructing a CFG for L1 ∪ L2 using the CFGs for L1 and L2 and a new start symbol.
  - **Concatenation**: If L1 and L2 are CFLs, then L1 L2 is also a CFL. This can be proved by constructing a CFG for L1 L2 using the CFGs for L1 and L2 and a new start symbol.
  - **Kleene closure**: If L is a CFL, then L* is also a CFL. This can be proved by constructing a CFG for L* using the CFG for L and a new start symbol.
  - **Reversal**: If L is a CFL, then LR (the reverse of L) is also a CFL. This can be proved by constructing a CFG for LR using the CFG for L and reversing the order of the symbols in the right-hand sides of the productions.
  - **Homomorphism**: If L is a CFL and h is a homomorphism (a function that maps each symbol in the alphabet to a string over another alphabet), then h(L) is also a CFL. This can be proved by constructing a CFG for h(L) using the CFG for L and applying h to the right-hand sides of the productions.
  - **Inverse homomorphism**: If L is a CFL and h is a homomorphism, then h-1(L) (the inverse image of L under h) is also a CFL. This can be proved by constructing a CFG for h-1(L) using the CFG for L and replacing each symbol in the right-hand sides of the productions with a variable that generates h(symbol).

- Some of the closure properties that CFLs do not have are:

  - **Intersection**: If L1 and L2 are CFLs, then L1 ∩ L2 may or may not be a CFL. A counterexample is L1 = {anbncn | n ≥ 0} and L2 = {anbn | n ≥ 0}, which are both CFLs, but L1 ∩ L2 = {anbncn | n ≥ 0} is not a CFL.
  - **Difference**: If L1 and L2 are CFLs, then L1 - L2 may or may not be a CFL. A counterexample is L1 = {anbncn | n ≥ 0} and L2 = {anbn | n ≥ 0}, which are both CFLs, but L1 - L2 = {anbncn | n > 0} is not a CFL.
  - **Complement**: If L is a CFL, then Lc (the complement of L) may or may not be a CFL. A counterexample is L = {anbncn | n ≥ 0}, which is a CFL, but Lc is not a CFL. However, it is known that if L is a deterministic CFL (a CFL that can be recognized by a deterministic PDA), then Lc is also a CFL. This is because the complement of a deterministic PDA is also a deterministic PDA.