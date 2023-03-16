### Backward Chaining

- Backward chaining is a method of reasoning in artificial intelligence that involves backtracking from the goal or endpoint to the steps that led to the goal .
- Backward chaining is used to find the conditions and rules by which a logical result or conclusion was reached.
- Backward chaining is based on the modus ponens inference rule, which states that if P implies Q and P is true, then Q is true.
- Backward chaining is implemented in logic programming by SLD resolution, which is a procedure for finding substitutions that make a goal clause true given a set of clauses.
- Backward chaining is a goal-driven inference algorithm, which means that it starts from the goal and tries to find evidence or support for it in the knowledge base .
- Backward chaining is useful for solving problems where the goal is well-defined and the search space is large .
- Backward chaining can be illustrated by an example of a medical diagnosis system, where the goal is to find the disease that causes a set of symptoms .
- The algorithm for backward chaining is as follows :

  - Start with the goal clause and try to match it with a clause in the knowledge base.
  - If there is a match, then check if the clause is a fact or a rule.
  - If the clause is a fact, then the goal is proved and the algorithm terminates.
  - If the clause is a rule, then add the antecedent of the rule to the list of subgoals and repeat the process for each subgoal.
  - If there is no match, then the goal is not proved and the algorithm fails.
  - If the list of subgoals is empty, then the goal is proved and the algorithm terminates.