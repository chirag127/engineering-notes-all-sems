### Proposition for the notes of the Unit 4 - Propositional Logic in the subject of Discrete Structures & Theory of Logic

- Propositional logic is a branch of logic that studies the ways of combining and modifying statements, called propositions, using logical connectives and operators.
- A proposition is a declarative sentence that is either true or false, but not both. For example, "Sydney is an AI assistant" is a proposition, but "What is your name?" is not.
- The truth value of a proposition is the logical value assigned to it, either true (T) or false (F). The truth value of a proposition may depend on the context or the state of the world. For example, the truth value of "It is raining" may vary depending on the location and time.
- A propositional variable is a symbol that represents a proposition. Usually, propositional variables are denoted by lowercase letters, such as p, q, r, etc. For example, we can use p to represent "It is raining" and q to represent "It is cold".
- A logical connective is a symbol that combines two or more propositions to form a new proposition. The most common logical connectives are:

  - Negation (¬): It reverses the truth value of a proposition. For example, ¬p means "It is not raining".
  - Conjunction (∧): It produces a true value only when both propositions are true. For example, p ∧ q means "It is raining and it is cold".
  - Disjunction (∨): It produces a true value when at least one of the propositions is true. For example, p ∨ q means "It is raining or it is cold".
  - Conditional (→): It produces a false value only when the first proposition is true and the second proposition is false. For example, p → q means "If it is raining, then it is cold".
  - Biconditional (↔): It produces a true value only when both propositions have the same truth value. For example, p ↔ q means "It is raining if and only if it is cold".

- A logical operator is a symbol that modifies a proposition to form a new proposition. The most common logical operator is:

  - Exclusive or (⊕): It produces a true value only when the propositions have different truth values. For example, p ⊕ q means "It is raining or it is cold, but not both".

- A truth table is a table that shows the truth value of a proposition or a combination of propositions for all possible combinations of truth values of the propositional variables. For example, the truth table for p ∧ q is:

| p | q | p ∧ q |
|---|---|-------|
| T | T | T     |
| T | F | F     |
| F | T | F     |
| F | F | F     |

- A tautology is a proposition that is always true, regardless of the truth values of the propositional variables. For example, p ∨ ¬p is a tautology, because it is true for both p = T and p = F.
- A contradiction is a proposition that is always false, regardless of the truth values of the propositional variables. For example, p ∧ ¬p is a contradiction, because it is false for both p = T and p = F.
- A contingency is a proposition that is neither a tautology nor a contradiction, meaning that it can be true or false depending on the truth values of the propositional variables. For example, p ∧ q is a contingency, because it is true for p = T and q = T, but false for other combinations of truth values.
- Logical equivalence is a relation between two propositions that have the same truth value for all possible combinations of truth values of the propositional variables. For example, p → q and ¬p ∨ q are logically equivalent, because they have the same truth table. We use the symbol ≡ to denote logical equivalence. For example, p → q ≡ ¬p ∨ q.
- Logical implication is a relation between two propositions that means that whenever the first proposition is true, the second proposition is also true. For example, p → q implies q → p, because if it is true that if it is raining, then it is cold, then it is also true that if it is cold, then it is raining. We use the symbol ⊢ to denote logical implication. For example, p → q ⊢ q → p.