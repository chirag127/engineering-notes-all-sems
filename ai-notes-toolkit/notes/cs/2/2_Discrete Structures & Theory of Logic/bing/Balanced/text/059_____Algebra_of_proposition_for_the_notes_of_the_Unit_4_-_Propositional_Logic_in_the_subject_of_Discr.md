### Algebra of proposition

- Algebra of proposition is the subbranch of mathematical logic that studies propositions and logical operators.
- Propositions are statements that can be either true or false, such as "It is raining" or "2 + 2 = 4".
- Logical operators are symbols that define new propositions from one or more given propositions, such as "and", "or", "not", "if...then", "if and only if".
- The most common symbols for logical operators are:

| Symbol | Name | Meaning |
| --- | --- | --- |
| $\land$ | Conjunction | And |
| $\lor$ | Disjunction | Or |
| $\lnot$ | Negation | Not |
| $\rightarrow$ | Implication | If...then |
| $\leftrightarrow$ | Equivalence | If and only if |

- The most common symbols for propositions are $p$, $q$, $r$, etc. They are called logical variables because any proposition can take their place.
- The truth value of a proposition is either true (T) or false (F). The truth value of a compound proposition (one that involves logical operators) depends on the truth values of the component propositions and the rules of the logical operators.
- A truth table is a table that shows the truth value of a compound proposition for all possible combinations of truth values of the component propositions. For example, the truth table for $p \land q$ is:

| $p$ | $q$ | $p \land q$ |
| --- | --- | --- |
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | F |

- Two propositions are said to be equivalent if they have the same truth value for all possible truth values of their component propositions. For example, $p \rightarrow q$ is equivalent to $\lnot p \lor q$.
- An algebraic identity is a statement that expresses the equivalence of two propositions. For example, one of the algebraic identities for conjunction is:

$$p \land q \equiv q \land p$$

- This means that the order of the propositions does not matter when using the "and" operator. There are many other algebraic identities for different logical operators, such as:

$$p \lor q \equiv q \lor p$$
$$p \lor (q \land r) \equiv (p \lor q) \land (p \lor r)$$
$$\lnot (p \land q) \equiv \lnot p \lor \lnot q$$
$$p \rightarrow q \equiv \lnot p \lor q$$
$$p \leftrightarrow q \equiv (p \rightarrow q) \land (q \rightarrow p)$$

- These algebraic identities can be used to simplify or transform propositions, just like the algebraic identities for numbers can be used to simplify or transform equations.
- A proposition is said to be a tautology if it is always true, regardless of the truth values of its component propositions. For example, $p \lor \lnot p$ is a tautology, because it is true whether $p$ is true or false.
- A proposition is said to be a contradiction if it is always false, regardless of the truth values of its component propositions. For example, $p \land \lnot p$ is a contradiction, because it is false whether $p$ is true or false.
- A proposition is said to be contingent if it is neither a tautology nor a contradiction, meaning that it can be true or false depending on the truth values of its component propositions. For example, $p \land q$ is contingent, because it is true when both $p$ and $q$ are true, and false otherwise.
- Every propositional formula is equivalent to a sum-of-products or disjunctive form, which is an OR of AND-terms, where each AND-term is an AND of variables or negations of variables. For example, the disjunctive form of $p \rightarrow q$ is:

$$(\lnot p \land \lnot q) \lor (\lnot p \land q) \lor (p \land q)$$

- The disjunctive form can be simplified by using the algebraic identities and eliminating redundant terms. For example, the simplified disjunctive form of $p \rightarrow q$ is:

$$\lnot p \lor q$$

- The algebra of proposition