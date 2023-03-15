# Theory of Inference for the notes of the Unit 4 - Propositional Logic in the subject of Discrete Structures & Theory of Logic

- Propositional logic is the branch of logic that studies ways of combining or altering statements or propositions to form more complicated statements or propositions.
- A proposition is a declarative sentence that is either true or false, but not both.
- Examples of propositions are "The sky is blue", "2 + 2 = 4", "It is raining today".
- Examples of non-propositions are "What time is it?", "x + y = z", "Please close the door".
- Propositional logic uses symbols to represent propositions and logical connectives to express the relationships between them.
- Some common symbols and connectives are:

| Symbol | Meaning |
| --- | --- |
| p, q, r, ... | Propositional variables |
| ¬ | Negation |
| ∧ | Conjunction |
| ∨ | Disjunction |
| → | Implication |
| ↔ | Equivalence |
| ⊤ | Tautology |
| ⊥ | Contradiction |

- A propositional formula is a combination of propositional variables and connectives that can be assigned a truth value depending on the truth values of the variables.
- Examples of propositional formulas are "p ∧ q", "¬(p → q)", "(p ∨ q) ↔ (¬p → q)".
- A truth table is a table that shows the truth values of a propositional formula for all possible combinations of truth values of the variables.
- A truth table has one column for each variable and one column for the formula, and one row for each possible assignment of truth values to the variables.
- The truth values are usually denoted by T for true and F for false.
- Here is an example of a truth table for the formula "(p ∨ q) ↔ (¬p → q)":

| p | q | (p ∨ q) ↔ (¬p → q) |
| --- | --- | --- |
| T | T | T |
| T | F | F |
| F | T | T |
| F | F | T |

- A propositional formula is said to be satisfiable if there is at least one assignment of truth values to the variables that makes the formula true.
- A propositional formula is said to be unsatisfiable if there is no such assignment.
- A propositional formula is said to be valid or a tautology if it is true for all possible assignments of truth values to the variables.
- A propositional formula is said to be invalid or a contradiction if it is false for all possible assignments.
- A propositional formula is said to be contingent if it is neither valid nor invalid, that is, it is true for some assignments and false for others.
- Examples of valid formulas are "p ∨ ¬p", "p → p", "(p ∧ q) → p".
- Examples of invalid formulas are "p ∧ ¬p", "p → ¬p", "(p ∨ q) → ¬p".
- Examples of contingent formulas are "p", "p ∧ q", "p → q".

- A logical inference is a process of deriving a conclusion from one or more premises using rules of logic.
- A logical inference is said to be sound if the premises are true and the conclusion follows logically from the premises.
- A logical inference is said to be unsound if either the premises are false or the conclusion does not follow logically from the premises.
- A logical inference is said to be valid if the conclusion follows logically from the premises, regardless of the truth values of the premises.
- A logical inference is said to be invalid if the conclusion does not follow logically from the premises, regardless of the truth values of the premises.
- A rule of inference is a general pattern of reasoning that can be applied to any propositional formulas that match the pattern.
- A rule of inference is said to be sound if it preserves the truth value of the formulas, that is, if the premises are true, then the conclusion is also true.
- A rule of inference is said to be unsound if it does not preserve the truth value of the formulas, that is, if there is a case where the premises are true but the conclusion is false.
- Examples of sound rules of inference are modus ponens, modus tollens, and contraposition.
- Examples of unsound rules of inference are affirming the consequent, denying the antecedent, and fallacy of the inverse.

- Modus ponens is a rule of inference that