### Backward Chaining

- Backward chaining is an inference method of reasoning in the field of artificial intelligence  .
- It refers to the process of backtracking from the goal or endpoint to previous steps which led to the goal itself .
- It is a goal-driven inference algorithm to find solutions where the end goal is defined.
- It is used in automated theorem provers, inference engines, proof assistants, and other artificial intelligence applications.
- It is based on the modus ponens inference rule, which states that if P implies Q and P is true, then Q is true.
- It is implemented in logic programming by SLD resolution, which is a method of finding substitutions that make a goal clause true given a set of clauses.
- It is one of the two most commonly used methods of reasoning with inference rules and logical implications – the other is forward chaining, which works in the opposite direction from the axioms to the goal.
- It is significantly more efficient at proof-finding problems than forward chaining, as it avoids exploring irrelevant branches of the search space.
- It can be illustrated by an example of a medical diagnosis system, where the goal is to find the disease that matches the symptoms of a patient.
- The system starts with the goal clause, such as "Patient has malaria", and tries to find a rule that implies it, such as "If patient has fever and chills, then patient has malaria".
- The system then tries to prove the antecedent of the rule, which is "Patient has fever and chills", by finding another rule that implies it, such as "If patient has headache and fatigue, then patient has fever and chills".
- The system repeats this process until it either finds a rule that has no antecedent, such as "Patient has headache", which is a fact, or fails to find a rule that implies the current goal, which means that the goal is false.
- The system can also use heuristics to guide the search, such as selecting the most specific or the most likely rule to apply at each step.