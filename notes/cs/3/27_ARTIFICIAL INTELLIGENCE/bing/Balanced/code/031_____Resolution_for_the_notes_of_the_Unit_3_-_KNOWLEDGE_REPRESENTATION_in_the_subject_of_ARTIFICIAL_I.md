Hello, I am Sydney, your AI assistant. I can help you with your notes on the topic of resolution for the unit 3 - knowledge representation in the subject of artificial intelligence KCS. Here is the content in markdown format:

### Resolution

- Resolution is a method of automated reasoning that uses the principle of inference by contradiction.
- Resolution is based on the idea that if a set of clauses is unsatisfiable, then there exists a refutation, which is a derivation of the empty clause from the set of clauses.
- Resolution can be applied to propositional logic, first-order logic, and other logics that have a clausal form.
- Resolution can be used for various tasks, such as theorem proving, query answering, and logic programming.

#### Resolution in propositional logic

- A clause is a disjunction of literals, where a literal is an atomic formula or its negation.
- A clause can be written as a set of literals, such as {p, q, ¬r}.
- A clause is said to be resolved with another clause if they have a complementary literal, that is, a literal and its negation.
- The resolvent of two clauses is the clause obtained by removing the complementary literals and taking the union of the remaining literals.
- For example, the resolvent of {p, q, ¬r} and {¬p, s, t} is {q, ¬r, s, t}.
- A resolution proof is a sequence of clauses, where each clause is either an initial clause (given in the input) or a resolvent of two previous clauses, and the last clause is the empty clause.
- A resolution proof shows that the set of initial clauses is unsatisfiable, and thus any formula that is logically equivalent to the conjunction of the initial clauses is unsatisfiable.
- For example, the following is a resolution proof for the set of clauses {p, ¬q}, {q, ¬r}, {r, ¬p}, {p, r}:

  - {p, ¬q} (initial)
  - {q, ¬r} (initial)
  - {r, ¬p} (initial)
  - {p, r} (initial)
  - {p, ¬r} (resolvent of 1 and 2)
  - {r, ¬q} (resolvent of 2 and 3)
  - {p, ¬q} (resolvent of 3 and 4)
  - {¬r} (resolvent of 5 and 6)
  - {¬q} (resolvent of 6 and 7)
  - {} (resolvent of 8 and 9)

- Resolution is sound and complete for propositional logic, meaning that a set of clauses is unsatisfiable if and only if there exists a resolution proof for it.
- Resolution is also refutation-complete, meaning that if a formula is valid, then its negation is unsatisfiable and has a resolution proof.
- Resolution can be used to test the validity of a formula by negating it and converting it to clausal form, and then applying resolution to the resulting set of clauses.
- Resolution can also be used to test the satisfiability of a formula by converting it to clausal form and applying resolution to the resulting set of clauses. If resolution fails to derive the empty clause, then the formula is satisfiable.