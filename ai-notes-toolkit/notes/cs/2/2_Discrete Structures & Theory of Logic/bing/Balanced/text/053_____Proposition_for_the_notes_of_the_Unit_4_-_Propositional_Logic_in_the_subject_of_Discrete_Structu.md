### Proposition for the notes of the Unit 4 - Propositional Logic in the subject of Discrete Structures & Theory of Logic

- Propositional logic is a branch of logic that studies the ways of combining and modifying statements, called propositions, using logical connectives and operators.
- A proposition is a declarative sentence that is either true or false, but not both. For example, "Sydney is an AI assistant" is a proposition, but "What is your name?" is not.
- The truth value of a proposition is the logical value assigned to it, either true (T) or false (F). The truth value of a proposition may depend on the context or the state of affairs in the world.
- A propositional variable is a symbol that can represent any proposition. Usually, propositional variables are denoted by lowercase letters such as p, q, r, etc.
- A propositional formula is a string of symbols that consists of propositional variables, logical connectives, and parentheses. For example, (p ∧ q) → r is a propositional formula.
- A logical connective is a symbol that is used to form new propositions from existing ones. The most common logical connectives are:
  - Negation (¬): It reverses the truth value of a proposition. For example, if p is true, then ¬p is false, and vice versa.
  - Conjunction (∧): It joins two propositions and is true only if both of them are true. For example, p ∧ q is true only if both p and q are true.
  - Disjunction (∨): It joins two propositions and is true if at least one of them is true. For example, p ∨ q is true if either p or q is true, or both.
  - Conditional (→): It expresses a logical implication between two propositions. For example, p → q means "if p, then q". It is false only if p is true and q is false, otherwise it is true.
  - Biconditional (↔): It expresses a logical equivalence between two propositions. For example, p ↔ q means "p if and only if q". It is true only if p and q have the same truth value, otherwise it is false.
- A truth table is a tabular representation of the truth values of a propositional formula for all possible combinations of truth values of its propositional variables. For example, the truth table for p → q is:

| p | q | p → q |
|---|---|-------|
| T | T | T     |
| T | F | F     |
| F | T | T     |
| F | F | T     |

- A tautology is a propositional formula that is always true, regardless of the truth values of its propositional variables. For example, p ∨ ¬p is a tautology.
- A contradiction is a propositional formula that is always false, regardless of the truth values of its propositional variables. For example, p ∧ ¬p is a contradiction.
- A contingency is a propositional formula that is neither a tautology nor a contradiction, meaning that it can be true or false depending on the truth values of its propositional variables. For example, p ∧ q is a contingency.
- Logical equivalence is a relation between two propositional formulas that have the same truth value for every possible assignment of truth values to their propositional variables. For example, p → q and ¬p ∨ q are logically equivalent, denoted by p → q ≡ ¬p ∨ q.
- Logical implication is a relation between two propositional formulas that means that whenever the first formula is true, the second formula is also true. For example, p → q implies ¬p ∨ q, denoted by p → q ⇒ ¬p ∨ q.
- A logical argument is a sequence of propositions that are intended to establish the truth of a conclusion from a set of premises. For example, the following is a logical argument:

  - Premise 1: If it rains, then the grass is wet.
  - Premise 2: It rains.
  - Conclusion: The grass is wet.

- A valid argument is a logical argument that has the property that if all the premises are true, then the conclusion must also be true. For example, the above argument is valid, because the conclusion follows logically from the premises.
- A sound argument is a valid argument that has the additional property that all the premises are actually true. For example, the above argument is sound, assuming that the premises are true in the real world.
- A fallacy is a common error in reasoning that makes an argument invalid or unsound. For example, the following is a fallacious