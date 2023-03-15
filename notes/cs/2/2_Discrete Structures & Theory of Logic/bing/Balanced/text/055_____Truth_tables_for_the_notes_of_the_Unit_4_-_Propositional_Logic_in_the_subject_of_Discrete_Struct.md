### Truth tables for the notes of the Unit 4 - Propositional Logic in the subject of Discrete Structures & Theory of Logic

- A truth table is a mathematical table used in logic that shows the truth values of logical expressions for each possible combination of values of their variables.
- A truth table can be used to solve various problems in propositional logic, such as showing the semantics of logical operators, proving equivalences, solving satisfiability problems, etc.
- A truth table has one column for each variable and one column for the logical expression. The rows of the table correspond to all possible assignments of truth values to the variables. The truth value of the expression for each row is calculated using the rules of propositional logic.
- The following table shows the basic logical operators and their truth tables:

| Operator | Symbol | Example | Truth table |
| --- | --- | --- | --- |
| Negation | ¬ | ¬p | p ¬p<br>T F<br>F T |
| Conjunction | ∧ | p ∧ q | p q p ∧ q<br>T T T<br>T F F<br>F T F<br>F F F |
| Disjunction | ∨ | p ∨ q | p q p ∨ q<br>T T T<br>T F T<br>F T T<br>F F F |
| Implication | → | p → q | p q p → q<br>T T T<br>T F F<br>F T T<br>F F T |
| Biconditional | ↔ | p ↔ q | p q p ↔ q<br>T T T<br>T F F<br>F T F<br>F F T |

- The following table shows some common logical equivalences and their truth tables:

| Equivalence | Symbol | Example | Truth table |
| --- | --- | --- | --- |
| Commutativity | ≡ | p ∧ q ≡ q ∧ p | p q p ∧ q q ∧ p<br>T T T T<br>T F F F<br>F T F F<br>F F F F |
| Associativity | ≡ | (p ∧ q) ∧ r ≡ p ∧ (q ∧ r) | p q r (p ∧ q) ∧ r p ∧ (q ∧ r)<br>T T T T T<br>T T F F F<br>T F T F F<br>T F F F F<br>F T T F F<br>F T F F F<br>F F T F F<br>F F F F F |
| Distributivity | ≡ | p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r) | p q r p ∧ (q ∨ r) (p ∧ q) ∨ (p ∧ r)<br>T T T T T<br>T T F T T<br>T F T T T<br>T F F F F<br>F T T F F<br>F T F F F<br>F F T F F<br>F F F F F |
| De Morgan's laws | ≡ | ¬(p ∧ q) ≡ ¬p ∨ ¬q | p q ¬(p ∧ q) ¬p ¬q ¬p ∨ ¬q<br>T T F F F F<br>T F T F T T<br>F T T T F T<br>F F T T T T |
| Identity laws | ≡ | p ∧ T ≡ p | p p ∧ T<br>T T<br>F F |
| Domination laws | ≡ | p ∨ T ≡ T | p p ∨ T<br>T T<br>F T |
| Double negation | ≡ | ¬¬p ≡ p | p ¬¬p<br>T T<br>F F |
| Contrapositive | ≡ | p → q ≡ ¬q → ¬p | p q p → q ¬q ¬p ¬q → ¬p<br>T T T F F T<br>T F F T F F<br>F T T F T T<br>F F T T T T |

: Truth table - Wikipedia
: Truth Tables - Propositional Logic | CodeGuage
: Propositional Logic Truth Table - Boolean Algebra - DYclassroom