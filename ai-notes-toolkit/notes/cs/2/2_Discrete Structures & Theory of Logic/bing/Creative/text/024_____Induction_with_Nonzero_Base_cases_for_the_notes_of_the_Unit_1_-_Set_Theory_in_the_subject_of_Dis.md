### Induction with Nonzero Base cases

- Induction is a method of mathematical proof that can be used to show that a statement is true for all natural numbers, or for all elements of a well-ordered set.
- The basic idea of induction is to start with a base case, where the statement is true for some initial value, and then show that if the statement is true for any value, it is also true for the next value. This is called the inductive step.
- By applying the inductive step repeatedly, we can conclude that the statement is true for all values that come after the base case.
- Sometimes, the base case is not zero, but some other value. For example, we may want to prove a statement for all natural numbers greater than or equal to 10, or for all positive integers that are multiples of 3.
- In such cases, we can still use induction, but we need to adjust the base case and the inductive step accordingly.
- The general form of induction with nonzero base cases is as follows:

  - Let P(n) be a statement involving a natural number n.
  - Let k be a fixed natural number, such that P(k) is true. This is the base case.
  - Assume that P(n) is true for some arbitrary natural number n ≥ k. This is the induction hypothesis.
  - Show that P(n+1) is true, using the induction hypothesis. This is the inductive step.
  - Conclude that P(n) is true for all natural numbers n ≥ k, by the principle of mathematical induction.

- Here is an example of induction with nonzero base cases:

  - Let P(n) be the statement that 2^n > n + 10, for any natural number n.
  - We want to prove that P(n) is true for all natural numbers n ≥ 4.
  - The base case is n = 4. We can check that P(4) is true, since 2^4 = 16 > 4 + 10 = 14.
  - The inductive step is to assume that P(n) is true for some arbitrary natural number n ≥ 4, and show that P(n+1) is true.
  - We have P(n) : 2^n > n + 10, by the induction hypothesis.
  - We want to show P(n+1) : 2^(n+1) > (n+1) + 10.
  - We can start from the left-hand side of P(n+1) and manipulate it as follows:

    - 2^(n+1) = 2 * 2^n > 2 * (n + 10), by P(n)
    - 2 * (n + 10) = 2n + 20 > n + 11, by simple algebra
    - n + 11 = (n + 1) + 10, by simple algebra

  - Therefore, 2^(n+1) > (n + 1) + 10, which is P(n+1).
  - We have shown the inductive step, so we can conclude that P(n) is true for all natural numbers n ≥ 4, by the principle of mathematical induction.