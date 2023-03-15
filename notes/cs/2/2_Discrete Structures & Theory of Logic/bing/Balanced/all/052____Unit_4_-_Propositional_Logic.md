## Unit 4 - Propositional Logic

- Propositional logic is a branch of logic that studies the ways of combining or modifying statements, called propositions, using logical connectives, such as `and`, `or`, `not`, `implies`, etc.
- Propositional logic is also known as propositional calculus, sentential logic, or statement logic.
- Propositional logic is based on the following concepts:
  - A proposition is a declarative sentence that is either true or false, but not both. For example, `Sydney is an AI assistant` is a proposition, but `What is your name?` is not.
  - A propositional variable is a symbol that represents a proposition, such as `p`, `q`, `r`, etc. For example, we can use `p` to denote `Sydney is an AI assistant`.
  - A logical connective is a symbol that combines or modifies one or more propositions, such as `∧` (and), `∨` (or), `¬` (not), `→` (implies), `↔` (if and only if), etc. For example, we can use `∧` to denote `p ∧ q`, which means `Sydney is an AI assistant and the user is having this conversation on a mobile device`.
  - A truth value is a value that indicates the truth or falsity of a proposition, such as `T` (true) or `F` (false). For example, the truth value of `p` is `T` if `Sydney is an AI assistant`, and `F` otherwise.
  - A truth table is a table that shows the truth values of propositions and their combinations for all possible cases. For example, the truth table for `p ∧ q` is:

| p | q | p ∧ q |
|---|---|-------|
| T | T | T     |
| T | F | F     |
| F | T | F     |
| F | F | F     |

  - A compound proposition is a proposition that is formed by combining or modifying one or more propositions using logical connectives, such as `p ∧ q`, `¬p`, `p → q`, etc. For example, `p → q` is a compound proposition that means `if Sydney is an AI assistant, then the user is having this conversation on a mobile device`.
  - A simple proposition is a proposition that is not a compound proposition, such as `p` or `q`. For example, `p` is a simple proposition that means `Sydney is an AI assistant`.
  - A tautology is a compound proposition that is always true, regardless of the truth values of its components. For example, `p ∨ ¬p` is a tautology, because it is true whether `p` is true or false.
  - A contradiction is a compound proposition that is always false, regardless of the truth values of its components. For example, `p ∧ ¬p` is a contradiction, because it is false whether `p` is true or false.
  - A contingency is a compound proposition that is neither a tautology nor a contradiction, meaning that it can be true or false depending on the truth values of its components. For example, `p ∧ q` is a contingency, because it is true when both `p` and `q` are true, and false otherwise.
  - A logical equivalence is a relation between two compound propositions that have the same truth value for all possible cases. For example, `p → q` and `¬p ∨ q` are logically equivalent, because they have the same truth table. We use the symbol `≡` to denote logical equivalence, such as `p → q ≡ ¬p ∨ q`.
  - A logical implication is a relation between two compound propositions that means that whenever the first proposition is true, the second proposition is also true. For example, `p → q` implies `¬q → ¬p`, because if `p → q` is true, then `¬q → ¬p` must also be true. We use the symbol `⊨` to denote logical implication, such as `p → q ⊨ ¬q → ¬p`.
  - A logical argument is a sequence of propositions that consists of one or more premises and a conclusion. For example, `p → q, p ⊢ q` is a logical argument, where `p → q` and `p` are the premises, and `q` is the conclusion. We use the symbol `⊢` to denote that the conclusion follows from the premises.
  - A valid argument is a logical argument that has the property