# Algebra of Proposition

- Algebra of proposition is the subbranch of mathematical logic that studies propositions and logical operators.
- A proposition is a declarative sentence that has a truth value, either true or false.
- A logical operator is a symbol that defines a new proposition from one or more given propositions.
- The most common logical operators are negation (NOT), conjunction (AND), disjunction (OR), implication (IF ... THEN), and equivalence (IF AND ONLY IF).
- Each logical operator has a truth table that shows the truth value of the new proposition for every possible combination of truth values of the given propositions.
- For example, the truth table for the conjunction operator (AND) is:

| p | q | p AND q |
|---|---|---------|
| T | T | T       |
| T | F | F       |
| F | T | F       |
| F | F | F       |

- This means that p AND q is true only when both p and q are true, and false otherwise.
- Algebra of proposition also studies the properties and rules of logical operators, such as commutativity, associativity, distributivity, identity, complement, idempotence, absorption, De Morgan's laws, etc .
- For example, the commutative property states that p AND q is equivalent to q AND p, and p OR q is equivalent to q OR p.
- Algebra of proposition also uses logical equivalence and logical implication to compare and simplify propositions .
- Two propositions are logically equivalent if they have the same truth value for every possible assignment of truth values to their variables .
- For example, p AND q is logically equivalent to NOT (NOT p OR NOT q), as shown by the following truth table:

| p | q | p AND q | NOT p | NOT q | NOT p OR NOT q | NOT (NOT p OR NOT q) |
|---|---|---------|-------|-------|-----------------|----------------------|
| T | T | T       | F     | F     | F               | T                    |
| T | F | F       | F     | T     | T               | F                    |
| F | T | F       | T     | F     | T               | F                    |
| F | F | F       | T     | T     | T               | F                    |

- Logical equivalence can be used to transform a proposition into a simpler or more convenient form without changing its meaning.
- A proposition p logically implies a proposition q if q is true whenever p is true .
- For example, p OR q logically implies p, as shown by the following truth table:

| p | q | p OR q | p OR q implies p |
|---|---|--------|------------------|
| T | T | T      | T                |
| T | F | T      | T                |
| F | T | T      | F                |
| F | F | F      | T                |

- Logical implication can be used to deduce new propositions from existing ones or to prove the validity of arguments .
- Algebra of proposition is useful for analyzing and manipulating logical expressions, such as those used in computer programming, circuit design, cryptography, artificial intelligence, etc .