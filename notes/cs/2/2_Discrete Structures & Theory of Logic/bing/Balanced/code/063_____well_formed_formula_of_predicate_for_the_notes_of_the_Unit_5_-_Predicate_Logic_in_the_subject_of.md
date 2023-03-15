Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of well formed formula of predicate logic.

```markdown
### Well formed formula of predicate logic

- A well formed formula (wff) of predicate logic is a string of symbols that can be assigned a truth value, i.e., it can be evaluated as true or false.
- A wff of predicate logic consists of one or more of the following components:
  - **Constants**: symbols that represent specific objects in the domain of discourse, such as a, b, c, ...
  - **Variables**: symbols that can stand for any object in the domain of discourse, such as x, y, z, ...
  - **Predicates**: symbols that represent properties or relations of objects, such as P, Q, R, ...
  - **Quantifiers**: symbols that express how many objects satisfy a given predicate, such as ∀ (for all) and ∃ (there exists)
  - **Connectives**: symbols that connect two or more wffs, such as ¬ (not), ∧ (and), ∨ (or), → (implies), and ↔ (if and only if)
  - **Parentheses**: symbols that group wffs together, such as ( and )
- A wff of predicate logic must follow certain rules of syntax, i.e., how the symbols can be combined. The rules are:
  - **Rule 1**: If P is an n-ary predicate and t1, t2, ..., tn are terms (constants or variables), then P(t1, t2, ..., tn) is a wff. This is called an **atomic formula**.
  - **Rule 2**: If A is a wff, then ¬A is a wff. This is called a **negation**.
  - **Rule 3**: If A and B are wffs, then (A ∧ B), (A ∨ B), (A → B), and (A ↔ B) are wffs. These are called **conjunctions**, **disjunctions**, **implications**, and **biconditionals**, respectively.
  - **Rule 4**: If A is a wff and x is a variable, then ∀x A and ∃x A are wffs. These are called **universal quantification** and **existential quantification**, respectively.
  - **Rule 5**: Nothing else is a wff.
- A wff of predicate logic can be interpreted semantically, i.e., what it means in a given domain of discourse. The interpretation depends on the following components:
  - **Domain**: a non-empty set of objects that the constants and variables can refer to, such as {1, 2, 3, 4, 5}
  - **Assignment**: a function that assigns a value from the domain to each constant and variable, such as a = 1, b = 2, x = 3, y = 4, z = 5
  - **Interpretation**: a function that assigns a meaning to each predicate, such as P(x) means "x is even", Q(x, y) means "x is less than y", R(x, y, z) means "x + y = z"
  - **Truth value**: a value that indicates whether a wff is true or false in a given domain, assignment, and interpretation, such as T (true) or F (false)
- A wff of predicate logic can be evaluated recursively, i.e., by applying the rules of syntax and semantics from the innermost to the outermost components. The rules are:
  - **Rule 1**: An atomic formula P(t1, t2, ..., tn) is true if and only if the interpretation of P holds for the values of t1, t2, ..., tn assigned by the assignment. For example, P(a) is true if and only if a is even, Q(x, y) is true if and only if x is less than y, R(b, x, z) is true if and only if b + x = z.
  - **Rule 2**: A negation ¬A is true if and only if A is false. For example, ¬P(a) is true if and only if P(a) is false, i.e., a is not even.
  - **Rule 3**: A conjunction (A ∧ B) is true if and only if both A and B are true. A disjunction (A ∨ B) is true if and only if either A or B is true. An implication (A → B) is true if and