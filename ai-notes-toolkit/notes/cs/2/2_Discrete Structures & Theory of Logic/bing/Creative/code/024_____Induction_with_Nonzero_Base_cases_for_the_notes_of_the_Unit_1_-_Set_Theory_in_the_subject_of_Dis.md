### Induction with Nonzero Base cases

- Induction is a method of mathematical proof that is used to show that a statement is true for all natural numbers, or for a subset of natural numbers.
- The basic idea of induction is to prove the statement for a base case, and then assume that it is true for some arbitrary number k, and show that it implies that the statement is also true for k+1. This is called the inductive step.
- Sometimes, the base case is not zero, but some other natural number, such as 1, 2, or 3. In this case, we need to modify the induction method slightly.
- The general form of induction with nonzero base cases is as follows:

  - Let P(n) be a statement involving a natural number n.
  - Let b be a nonzero natural number, such as 1, 2, or 3.
  - To prove that P(n) is true for all natural numbers n ≥ b, we need to do two things:
    - Prove that P(b) is true. This is the base case.
    - Assume that P(k) is true for some arbitrary natural number k ≥ b, and show that P(k+1) is also true. This is the inductive step.

- For example, suppose we want to prove that the sum of the first n odd natural numbers is n^2, for all natural numbers n ≥ 1. That is, we want to prove that P(n) is true, where P(n) is the statement:

  - 1 + 3 + 5 + ... + (2n-1) = n^2

- To prove this by induction with nonzero base cases, we do the following:

  - Base case: When n = 1, we have:

    - 1 = 1^2

    - which is true. So, P(1) is true.

  - Inductive step: Assume that P(k) is true for some arbitrary natural number k ≥ 1. That is, assume that:

    - 1 + 3 + 5 + ... + (2k-1) = k^2

    - We need to show that P(k+1) is also true. That is, we need to show that:

    - 1 + 3 + 5 + ... + (2k-1) + (2k+1) = (k+1)^2

    - To do this, we can use the assumption and some algebra. We have:

    - 1 + 3 + 5 + ... + (2k-1) + (2k+1) = k^2 + (2k+1) (by the assumption)

    - = k^2 + 2k + 1

    - = (k+1)^2 (by factoring)

    - which is what we wanted to show. So, P(k+1) is true.

- Therefore, by induction with nonzero base cases, we have proved that P(n) is true for all natural numbers n ≥ 1.