### Backward Chaining

- Backward chaining is an inference method of reasoning in the field of artificial intelligence  .
- It refers to the process of backtracking from the goal or endpoint to previous steps which led to the goal itself .
- It is used in automated theorem provers, inference engines, proof assistants, and other artificial intelligence applications.
- It is a goal-driven inference algorithm to find solutions where the end goal is defined.
- It is based on the modus ponens inference rule, which states that if P implies Q and P is true, then Q is true.
- It is one of the two most commonly used methods of reasoning with inference rules and logical implications – the other is forward chaining.
- Forward chaining is a method of reasoning in which inference rules are applied in a forward direction, starting from the known facts and deriving new facts.
- Backward chaining is more efficient at proof-finding problems, as it avoids exploring irrelevant facts and rules.
- Backward chaining is implemented in logic programming by SLD resolution, which is a method of finding substitutions that make a goal clause true given a set of clauses.
- An example of backward chaining is the following:

  - Goal: John is a bachelor
  - Rule: A person is a bachelor if they are male and unmarried
  - Subgoals: John is male and John is unmarried
  - Facts: John is male, John is unmarried
  - Solution: John is a bachelor (true)