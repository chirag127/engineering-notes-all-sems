### Forward Chaining

- Forward chaining is a method of reasoning in artificial intelligence in which inference rules are applied to existing data to extract additional data until an endpoint (goal) is achieved   .
- In this type of chaining, the inference engine starts by evaluating existing facts, derivations, and conditions before deducing new information   .
- The rules are applied in a forward direction, from known to unknown  .
- Forward chaining is also known as bottom-up reasoning or data-driven reasoning .
- Forward chaining is a popular implementation strategy for expert systems, business and production rule systems.
- Forward chaining can be illustrated by the following example:

  - Suppose we have the following facts and rules:

    - Facts: John is a human. Humans are mortal.
    - Rules: If X is a human, then X is an animal. If X is an animal, then X can breathe.

  - We can apply forward chaining to infer new facts from the existing ones:

    - Fact 1: John is a human.
    - Rule 1: If X is a human, then X is an animal.
    - New fact: John is an animal.
    - Fact 2: Humans are mortal.
    - Rule 2: If X is an animal, then X can breathe.
    - New fact: John can breathe.
    - New fact: John is mortal.

  - The inference engine can stop when no more new facts can be derived or when a specific goal is reached. For example, if the goal is to find out if John is mortal, the inference engine can stop after deriving the fact that John is mortal.