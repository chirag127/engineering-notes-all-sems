### Proof by counter – example for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic

- A proof by counterexample is a method of disproving a general statement by finding a specific case where the statement is false.
- A counterexample is a specific instance that contradicts a conjecture or a hypothesis.
- To prove a statement by counterexample, we need to find one example that makes the statement false. We do not need to check all possible cases or provide a general argument.
- A proof by counterexample has the following form:

  - Suppose we want to disprove a statement of the form "For all x, P(x) is true", where x is a variable and P(x) is a predicate.
  - We find a specific value of x, say a, such that P(a) is false.
  - We conclude that the statement "For all x, P(x) is true" is false, because it does not hold for x = a.

- Example: Prove by counterexample that the statement "For all natural numbers n, n^2 + n + 41 is prime" is false.

  - To find a counterexample, we need to find a natural number n such that n^2 + n + 41 is not prime.
  - One possible counterexample is n = 40. Then n^2 + n + 41 = 40^2 + 40 + 41 = 1681, which is not prime, because it is divisible by 41.
  - Therefore, the statement "For all natural numbers n, n^2 + n + 41 is prime" is false, because it does not hold for n = 40.