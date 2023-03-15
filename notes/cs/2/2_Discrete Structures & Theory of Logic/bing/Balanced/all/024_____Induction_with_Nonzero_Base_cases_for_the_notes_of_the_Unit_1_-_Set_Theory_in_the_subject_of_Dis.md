# Induction with Nonzero Base Cases

- Induction is a method of proving statements about natural numbers or other well-ordered sets by showing that a base case holds and that the statement is preserved by successor operations.
- The base case is the smallest or simplest instance of the statement that we want to prove. Usually, the base case is n = 0, but sometimes it can be a different value, such as n = 1 or n = 5.
- When the base case is not zero, we need to adjust the induction hypothesis and the induction step accordingly. For example, if we want to prove a statement for all n ≥ 5, we need to show that it holds for n = 5 (the base case) and that if it holds for some n ≥ 5, then it also holds for n + 1 (the induction step).
- Here is an example of a proof by induction with a nonzero base case:

  - Claim: For all n ≥ 5, n^2 < 2^n.
  - Proof: By induction on n.
    - Base case: If n = 5, then we have that 5^2 = 25 < 32 = 2^5, so the claim holds.
    - Induction step: Assume that for some n ≥ 5, n^2 < 2^n. Then we have that (n + 1)^2 = n^2 + 2n + 1. Since n ≥ 5, we have (n + 1)^2 = n^2 + 2n + 1 < n^2 + 2n + n (since 1 < 5 ≤ n) = n^2 + 3n < n^2 + n^2 (since 3n < 5n ≤ n^2) = 2n^2 < 2^n * 2 = 2^(n + 1). Therefore, the claim also holds for n + 1. By induction, the claim holds for all n ≥ 5. QED.