### Forward Chaining

- Forward chaining is a method of reasoning in artificial intelligence in which inference rules are applied to existing data to extract additional data until an endpoint (goal) is achieved   .
- In this type of chaining, the inference engine starts by evaluating existing facts, derivations, and conditions before deducing new information   .
- The rules are applied in a forward direction, from known to unknown  .
- Forward chaining is also known as bottom-up reasoning or data-driven reasoning .
- Forward chaining is a popular implementation strategy for expert systems, business and production rule systems.
- Forward chaining can be illustrated by the following example:

  - Suppose we have the following facts and rules:

    - Facts: John is hungry. John has money.
    - Rules: If X is hungry, then X will buy food. If X buys food, then X will eat food.

  - The inference engine can apply the rules to the facts in a forward direction, as follows:

    - Fact: John is hungry.
    - Rule: If X is hungry, then X will buy food.
    - Conclusion: John will buy food.
    - New fact: John will buy food.
    - Rule: If X buys food, then X will eat food.
    - Conclusion: John will eat food.
    - New fact: John will eat food.
    - Goal: John will not be hungry.

  - The inference engine can stop when the goal is reached or no more rules can be applied.