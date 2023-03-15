Hello, I am Sydney, your AI assistant. I can help you with your notes for Unit 4 - Propositional Logic in the subject of Discrete Structures & Theory of Logic. Here is a possible outline for your notes:

# Unit 4 - Propositional Logic

## Introduction

- Propositional logic is a branch of logic that deals with statements that can be either true or false.
- A statement is a declarative sentence that has a truth value, such as "It is raining" or "2 + 2 = 4".
- A proposition is the meaning or content of a statement, regardless of the words or symbols used to express it.
- Propositional logic uses symbols and rules to manipulate propositions and determine their truth values.

## Syntax and Semantics

- The basic symbols of propositional logic are called propositional variables or propositional atoms. They are usually denoted by lowercase letters such as p, q, r, etc.
- A propositional variable can represent any proposition that can be either true or false, such as "The sky is blue" or "Sydney is an AI assistant".
- The truth value of a propositional variable is either T (true) or F (false), depending on the proposition it represents.
- A propositional formula or well-formed formula (wff) is a string of symbols that is constructed from propositional variables and logical connectives using the following rules:
  - A propositional variable is a wff.
  - If A and B are wffs, then so are (A ∧ B), (A ∨ B), (A → B), (A ↔ B), and (¬A), where ∧, ∨, →, ↔, and ¬ are logical connectives that represent conjunction, disjunction, implication, equivalence, and negation, respectively.
  - Nothing else is a wff.
- A wff can be interpreted as a complex proposition that is composed of simpler propositions using logical connectives.
- The truth value of a wff depends on the truth values of its propositional variables and the meanings of its logical connectives, as defined by the following truth tables:

| A | B | A ∧ B | A ∨ B | A → B | A ↔ B | ¬A |
|---|---|-------|-------|-------|-------|----|
| T | T | T     | T     | T     | T     | F  |
| T | F | F     | T     | F     | F     | F  |
| F | T | F     | T     | T     | F     | T  |
| F | F | F     | F     | T     | T     | T  |

- A wff is said to be satisfiable if there is an assignment of truth values to its propositional variables that makes it true, and unsatisfiable otherwise.
- A wff is said to be valid or a tautology if it is true for all possible assignments of truth values to its propositional variables, and invalid or a contradiction otherwise.
- A wff is said to be contingent if it is neither valid nor invalid, i.e., it is true for some assignments and false for others.

## Equivalence and Normal Forms

- Two wffs are said to be logically equivalent if they have the same truth value for all possible assignments of truth values to their propositional variables. This is denoted by A ≡ B.
- Logical equivalence can be established by showing that the two wffs have the same truth table, or by using a set of equivalence laws that are derived from the truth tables of the logical connectives. Some common equivalence laws are:

| Name | Law |
|------|-----|
| Commutativity | A ∧ B ≡ B ∧ A, A ∨ B ≡ B ∨ A |
| Associativity | (A ∧ B) ∧ C ≡ A ∧ (B ∧ C), (A ∨ B) ∨ C ≡ A ∨ (B ∨ C) |
| Distributivity | A ∧ (B ∨ C) ≡ (A ∧ B) ∨ (A ∧ C), A ∨ (B ∧ C) ≡ (A ∨ B) ∧ (A ∨ C) |
| Identity | A ∧ T ≡ A, A ∨ F ≡ A |
| Domination | A ∧ F ≡ F, A ∨ T ≡ T |
| Idempotence | A ∧ A ≡ A, A ∨ A ≡ A |
| Double Negation | ¬(¬A) ≡ A |
| De Morgan's Laws | ¬(A ∧ B) ≡ ¬A ∨ ¬B, ¬(A