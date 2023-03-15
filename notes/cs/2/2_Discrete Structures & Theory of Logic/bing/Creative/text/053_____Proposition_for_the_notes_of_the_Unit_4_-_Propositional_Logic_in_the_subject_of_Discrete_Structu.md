### Proposition for the notes of the Unit 4 - Propositional Logic in the subject of Discrete Structures & Theory of Logic

- Propositional logic is a branch of logic that studies the ways of combining and modifying statements, called propositions, using logical connectives and operators.
- A proposition is a declarative sentence that is either true or false, but not both. For example, "Sydney is an AI assistant" is a proposition, but "What is your name?" is not.
- Logical connectives are symbols that are used to form compound propositions from simpler ones. The main logical connectives are:
  - Negation (¬): It reverses the truth value of a proposition. For example, if p is "It is raining", then ¬p is "It is not raining".
  - Conjunction (∧): It joins two propositions and is true only when both of them are true. For example, if p is "It is raining" and q is "It is cold", then p ∧ q is "It is raining and it is cold".
  - Disjunction (∨): It joins two propositions and is true when at least one of them is true. For example, if p is "It is raining" and q is "It is cold", then p ∨ q is "It is raining or it is cold".
  - Conditional (→): It represents an implication or a cause-effect relationship between two propositions. It is true when the antecedent (the proposition before the arrow) is false or the consequent (the proposition after the arrow) is true. For example, if p is "It is raining" and q is "The ground is wet", then p → q is "If it is raining, then the ground is wet".
  - Biconditional (↔): It represents an equivalence or a necessary and sufficient condition between two propositions. It is true when both propositions have the same truth value. For example, if p is "It is raining" and q is "The ground is wet", then p ↔ q is "It is raining if and only if the ground is wet".
- Logical operators are symbols that are used to modify propositions or perform operations on them. The main logical operators are:
  - Parentheses ( ): They are used to group propositions and indicate the order of evaluation. For example, (p ∧ q) ∨ r is different from p ∧ (q ∨ r).
  - Truth tables: They are tables that show the truth value of a compound proposition for every possible combination of truth values of its components. For example, the truth table for p ∧ q is:

| p | q | p ∧ q |
|---|---|-------|
| T | T | T     |
| T | F | F     |
| F | T | F     |
| F | F | F     |

  - Logical equivalence: Two propositions are logically equivalent if they have the same truth value for every possible assignment of truth values to their components. For example, p ∧ q is logically equivalent to q ∧ p, and ¬(p ∧ q) is logically equivalent to ¬p ∨ ¬q. Logical equivalence can be proved using truth tables or logical laws.
  - Logical laws: They are rules or principles that can be used to simplify or manipulate propositions. For example, some of the logical laws are:
    - Commutative laws: p ∧ q ≡ q ∧ p and p ∨ q ≡ q ∨ p
    - Associative laws: (p ∧ q) ∧ r ≡ p ∧ (q ∧ r) and (p ∨ q) ∨ r ≡ p ∨ (q ∨ r)
    - Distributive laws: p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r) and p ∨ (q ∧ r) ≡ (p ∨ q) ∧ (p ∨ r)
    - Identity laws: p ∧ T ≡ p and p ∨ F ≡ p
    - Negation laws: ¬(¬p) ≡ p and p ∧ ¬p ≡ F and p ∨ ¬p ≡ T
    - Double negation law: ¬(¬p) ≡ p
    - De Morgan's laws: ¬(p ∧ q) ≡ ¬p ∨ ¬q and ¬(p ∨ q) ≡ ¬p ∧ ¬q
    - Implication law: p → q ≡ ¬p ∨ q
    - Contrapositive law: p → q ≡ ¬q → ¬p
    - Biconditional law: p ↔ q ≡ (p → q) ∧ (q → p)
- Propositional