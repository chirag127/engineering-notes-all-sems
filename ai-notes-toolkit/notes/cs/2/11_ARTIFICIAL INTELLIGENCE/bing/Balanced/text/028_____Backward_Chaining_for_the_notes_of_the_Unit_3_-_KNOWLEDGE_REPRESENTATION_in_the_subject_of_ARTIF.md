### Backward Chaining

- Backward chaining is a method of reasoning in which the goal is given first and then the premises are derived from it.
- Backward chaining is also known as goal-driven reasoning or backward reasoning.
- Backward chaining is useful for solving problems that have a clear goal and a large search space.
- Backward chaining works by applying inference rules in reverse, starting from the goal and working backwards to find the facts that support it.
- Backward chaining can be implemented using a stack data structure, where the goal is pushed onto the stack and then popped off when it is either proved or disproved.
- Backward chaining can be illustrated by an example of a medical diagnosis system, where the goal is to find the disease that causes a set of symptoms.

  - Suppose the goal is to find the disease that causes fever, headache, and rash.
  - The system would look for a rule that has fever, headache, and rash as its consequent, such as:

    - If the patient has measles, then the patient has fever, headache, and rash.

  - The system would then push the antecedent of the rule, measles, onto the stack as a new goal.
  - The system would then look for a rule that has measles as its consequent, such as:

    - If the patient has been exposed to someone with measles, then the patient has measles.

  - The system would then push the antecedent of the rule, exposure to someone with measles, onto the stack as a new goal.
  - The system would then look for a fact that matches the goal, such as:

    - The patient has been exposed to someone with measles.

  - The system would then pop the goal off the stack and mark it as true.
  - The system would then pop the next goal, measles, off the stack and mark it as true, since it has been proved by the previous goal.
  - The system would then pop the original goal, fever, headache, and rash, off the stack and mark it as true, since it has been proved by the previous goal.
  - The system would then conclude that the patient has measles as the disease that causes fever, headache, and rash.