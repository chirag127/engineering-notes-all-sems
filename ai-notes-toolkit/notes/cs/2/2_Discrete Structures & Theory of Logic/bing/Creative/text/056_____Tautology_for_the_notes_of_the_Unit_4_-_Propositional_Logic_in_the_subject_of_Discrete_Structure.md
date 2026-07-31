### Tautology

- A tautology is a statement of propositional logic that is always true, regardless of the truth values of the propositional variables involved .
- A tautology can be recognized by using a truth table, which shows all the possible combinations of truth values for the propositional variables and the resulting truth value of the statement. If the statement is true for every row of the truth table, then it is a tautology .
- A tautology can also be recognized by using logical equivalences, which are rules that allow us to replace one statement with another that has the same truth value. If a statement can be reduced to a single propositional variable or a constant (such as T or F), then it is a tautology.
- Some examples of tautologies are :

  - p ∨ ¬p (either p or not p)
  - p → p (if p then p)
  - (p ∧ q) → (p ∨ q) (if p and q then p or q)
  - (p ↔ q) ↔ ((p → q) ∧ (q → p)) (p is equivalent to q if and only if p implies q and q implies p)
  - T (true)

- A tautology is a rule of replacement in propositional logic, which means that it can be used to replace a statement with another that has the same truth value without changing the validity of an argument.
- The rules of replacement that are based on tautologies are:

  - Idempotency of disjunction: p ∨ p ≡ p (p or p is equivalent to p)
  - Idempotency of conjunction: p ∧ p ≡ p (p and p is equivalent to p)
  - Commutativity of disjunction: p ∨ q ≡ q ∨ p (p or q is equivalent to q or p)
  - Commutativity of conjunction: p ∧ q ≡ q ∧ p (p and q is equivalent to q and p)
  - Associativity of disjunction: (p ∨ q) ∨ r ≡ p ∨ (q ∨ r) (p or q or r is equivalent to p or q or r)
  - Associativity of conjunction: (p ∧ q) ∧ r ≡ p ∧ (q ∧ r) (p and q and r is equivalent to p and q and r)
  - Distributivity of disjunction over conjunction: p ∨ (q ∧ r) ≡ (p ∨ q) ∧ (p ∨ r) (p or q and r is equivalent to p or q and p or r)
  - Distributivity of conjunction over disjunction: p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r) (p and q or r is equivalent to p and q or p and r)
  - Double negation: ¬¬p ≡ p (not not p is equivalent to p)
  - De Morgan's laws: ¬(p ∨ q) ≡ ¬p ∧ ¬q (not p or q is equivalent to not p and not q)
  - De Morgan's laws: ¬(p ∧ q) ≡ ¬p ∨ ¬q (not p and q is equivalent to not p or not q)
  - Implication: p → q ≡ ¬p ∨ q (p implies q is equivalent to not p or q)
  - Contrapositive: p → q ≡ ¬q → ¬p (p implies q is equivalent to not q implies not p)
  - Equivalence: p ↔ q ≡ (p → q) ∧ (q → p) (p is equivalent to q is equivalent to p implies q and q implies p)
  - Negation of equivalence: ¬(p ↔ q) ≡ p ↔ ¬q (not p is equivalent to q is equivalent to p is equivalent to not q)
  - Excluded middle: p ∨ ¬p ≡ T (p or not p is equivalent to true)
  - Contradiction: p ∧ ¬p ≡ F (p and not p is equivalent to false)
  - Simplification: p ∧ q ⊢ p (p and q implies p)
  - Addition: p ⊢ p ∨ q (p implies p or q)
  - Modus ponens: p