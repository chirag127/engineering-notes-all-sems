### Algebra of proposition

- Algebra of proposition is the subbranch of mathematical logic that studies propositions and logical operators.
- Propositions are statements that can be either true or false, such as "It is raining" or "2 + 2 = 4".
- Logical operators are symbols that define new propositions from one or more given propositions, such as "and", "or", "not", "if...then", and "if and only if".
- The most common symbols for logical operators are:

| Symbol | Name | Meaning |
|:------:|:----:|:-------:|
| $\land$ | Conjunction | And |
| $\lor$ | Disjunction | Or |
| $\lnot$ | Negation | Not |
| $\rightarrow$ | Implication | If...then |
| $\leftrightarrow$ | Equivalence | If and only if |

- The most common symbols for propositions are $p$, $q$, $r$, etc. They are also called logical variables, because any proposition can take their place.
- The truth value of a proposition is either true (T) or false (F), depending on whether the proposition is true or false in reality.
- The truth value of a compound proposition, formed by applying logical operators to one or more propositions, depends on the truth values of the component propositions and the rules of the logical operators.
- A truth table is a table that shows the truth value of a compound proposition for all possible combinations of truth values of the component propositions.
- For example, the truth table for $p \land q$ is:

| $p$ | $q$ | $p \land q$ |
|:---:|:---:|:-----------:|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | F |

- This means that $p \land q$ is true only when both $p$ and $q$ are true, and false otherwise.
- Similarly, the truth table for $p \lor q$ is:

| $p$ | $q$ | $p \lor q$ |
|:---:|:---:|:----------:|
| T | T | T |
| T | F | T |
| F | T | T |
| F | F | F |

- This means that $p \lor q$ is true when either $p$ or $q$ is true, or both, and false only when both $p$ and $q$ are false.
- The truth tables for the other logical operators can be found in the references  .
- Two propositions are said to be equivalent if they have the same truth value for all possible truth values of their component propositions.
- For example, $p \rightarrow q$ is equivalent to $\lnot p \lor q$, as shown by their truth tables:

| $p$ | $q$ | $p \rightarrow q$ | $\lnot p \lor q$ |
|:---:|:---:|:-----------------:|:----------------:|
| T | T | T | T |
| T | F | F | F |
| F | T | T | T |
| F | F | T | T |

- Equivalence can be shown by using the symbol $\equiv$, such as $p \rightarrow q \equiv \lnot p \lor q$.
- Equivalence can also be proven by using logical laws, such as commutative, associative, distributive, identity, negation, double negation, De Morgan's, implication, and equivalence laws  .
- For example, to prove that $p \rightarrow q \equiv \lnot p \lor q$, we can use the implication law, which states that $p \rightarrow q \equiv \lnot (p \land \lnot q)$, and then use De Morgan's law, which states that $\lnot (p \land \lnot q) \equiv \lnot p \lor \lnot (\lnot q)$, and then use the double negation law, which states that $\lnot (\lnot q) \equiv q$.
- Therefore, we have:

$$
\begin{align*}
p \rightarrow q &\equiv \lnot (p \land \lnot q) && \text{(by implication law)} \\
&\equiv \lnot p \lor