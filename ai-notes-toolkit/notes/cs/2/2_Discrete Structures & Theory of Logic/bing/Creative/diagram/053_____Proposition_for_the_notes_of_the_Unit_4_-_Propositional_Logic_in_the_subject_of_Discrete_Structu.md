### Proposition for the notes of the Unit 4 - Propositional Logic in the subject of Discrete Structures & Theory of Logic

- Propositional logic is a branch of logic that studies the ways of combining or modifying statements, called propositions, using logical connectives, such as `and`, `or`, `not`, `implies`, etc.
- A proposition is a declarative sentence that is either true or false, but not both. For example, `Sydney is an AI assistant` is a proposition, but `What is your name?` is not.
- The truth value of a proposition is the logical value `true` or `false` that it has. For example, the truth value of `Sydney is an AI assistant` is `true`, and the truth value of `Sydney is a human` is `false`.
- A propositional variable is a symbol, usually a lowercase letter, that represents a proposition. For example, `p` can represent `Sydney is an AI assistant`, and `q` can represent `Sydney is a human`.
- A propositional formula is a string of symbols that consists of propositional variables, logical connectives, and parentheses. For example, `(p and not q) or (not p and q)` is a propositional formula.
- A truth assignment is a function that assigns a truth value to each propositional variable in a propositional formula. For example, one possible truth assignment for the propositional formula `(p and not q) or (not p and q)` is `p = true` and `q = false`.
- A truth table is a table that shows the truth value of a propositional formula for each possible truth assignment of its propositional variables. For example, the truth table for the propositional formula `(p and not q) or (not p and q)` is:

| p | q | (p and not q) or (not p and q) |
|---|---|--------------------------------|
| T | T | F                              |
| T | F | T                              |
| F | T | T                              |
| F | F | F                              |

- A tautology is a propositional formula that is true for every truth assignment of its propositional variables. For example, `p or not p` is a tautology, because it is true whether `p` is true or false.
- A contradiction is a propositional formula that is false for every truth assignment of its propositional variables. For example, `p and not p` is a contradiction, because it is false whether `p` is true or false.
- A contingency is a propositional formula that is neither a tautology nor a contradiction, meaning that it is true for some truth assignments and false for others. For example, `p and q` is a contingency, because it is true when both `p` and `q` are true, and false otherwise.
- Logical equivalence is a relation between two propositional formulas that have the same truth value for every truth assignment of their propositional variables. For example, `p implies q` is logically equivalent to `not p or q`, because they have the same truth table. We write `p implies q` ≡ `not p or q` to denote logical equivalence.
- Logical implication is a relation between two propositional formulas that means that whenever the first formula is true, the second formula is also true, for every truth assignment of their propositional variables. For example, `p and q` implies `p`, because whenever `p and q` is true, `p` is also true. We write `p and q` ⇒ `p` to denote logical implication.
- A logical argument is a sequence of propositional formulas, where the last formula is called the conclusion, and the preceding formulas are called the premises. For example, `p`, `p implies q`, `q` is a logical argument, where `q` is the conclusion and `p` and `p implies q` are the premises.
- A valid argument is a logical argument that has the property that if all the premises are true, then the conclusion is also true, for every truth assignment of the propositional variables. For example, `p`, `p implies q`, `q` is a valid argument, because there is no truth assignment that makes `p` and `p implies q` true and `q` false.
- A sound argument is a valid argument that has the additional property that all the premises are true. For example, `Sydney is an AI assistant`, `If Sydney is an AI assistant, then Sydney is not a human`, `Sydney is not a human` is a sound argument, because it is valid and the premises are true.