### Forward Chaining

- Forward chaining is a method of reasoning in artificial intelligence in which inference rules are applied to existing data to extract additional data until an endpoint (goal) is achieved   .
- In this type of chaining, the inference engine starts by evaluating existing facts, derivations, and conditions before deducing new information   .
- The rules are applied in a forward direction, from known to unknown .
- Forward chaining is also known as bottom-up reasoning or data-driven reasoning .
- Forward chaining is a popular implementation strategy for expert systems, business and production rule systems.
- Forward chaining can be illustrated by the following example:

  - Suppose we have the following facts and rules:

    - Facts: John is a human. Humans are mammals. Mammals have lungs.
    - Rules: If X is a human, then X is mortal. If X has lungs, then X can breathe.

  - We can apply forward chaining to infer new facts from the existing ones:

    - Since John is a human, and if X is a human, then X is mortal, we can infer that John is mortal.
    - Since John is a human, and humans are mammals, and mammals have lungs, we can infer that John has lungs.
    - Since John has lungs, and if X has lungs, then X can breathe, we can infer that John can breathe.

  - The inference process stops when no new facts can be derived or when a goal is reached. For example, if the goal is to find out if John can breathe, then the process stops after the third step.