# Tautology for the notes of the Unit 4 - Propositional Logic in the subject of Discrete Structures & Theory of Logic

- A tautology is a propositional formula that is always true, regardless of the truth values of the propositional variables in it .
- A tautology can be verified by using a truth table, which shows all the possible combinations of truth values for the propositional variables and the resulting truth value of the formula. If the formula is true in every row of the truth table, it is a tautology .
- Examples of tautologies are:

  - p ∨ ¬p (either p or not p)
  - p → p (p implies p)
  - (p ∧ q) → p (if p and q, then p)
  - (p ∨ q) ∨ ¬(p ∧ q) (either p or q, or neither p nor q)
  - (p → q) ↔ (¬q → ¬p) (p implies q if and only if not q implies not p)

- A tautology can be used as a rule of replacement in logical proofs, which allows us to replace a propositional formula with an equivalent one without changing the validity of the argument. There are two commonly used rules of replacement based on tautologies:

  - The principle of idempotency of disjunction: p ∨ p ≡ p (p or p is equivalent to p)
  - The principle of idempotency of conjunction: p ∧ p ≡ p (p and p is equivalent to p)

- A tautology can also be used as a premise or a conclusion in a logical argument, since it is always true and does not depend on any assumptions. For example, the following argument is valid, because the premise and the conclusion are both tautologies:

  - Premise: p ∨ ¬p
  - Conclusion: (p → q) ↔ (¬q → ¬p)

- A tautology is different from a contradiction, which is a propositional formula that is always false, regardless of the truth values of the propositional variables in it. For example, p ∧ ¬p (p and not p) is a contradiction. A contradiction can also be used as a rule of replacement in logical proofs, which allows us to replace a propositional formula with an equivalent one without changing the validity of the argument. There are two commonly used rules of replacement based on contradictions:

  - The principle of explosion: p ∧ ¬p ≡ q (p and not p is equivalent to any proposition q)
  - The principle of contradiction: ¬(p ∧ ¬p) ≡ ⊤ (not (p and not p) is equivalent to the truth value true)

- A tautology is also different from a contingency, which is a propositional formula that is sometimes true and sometimes false, depending on the truth values of the propositional variables in it. For example, p ∧ q (p and q) is a contingency, since it is true when both p and q are true, and false otherwise. A contingency cannot be used as a premise or a conclusion in a logical argument, since it does not guarantee the validity of the argument. For example, the following argument is invalid, because the premise and the conclusion are both contingencies:

  - Premise: p ∧ q
  - Conclusion: p ∨ q