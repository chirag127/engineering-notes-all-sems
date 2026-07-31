# Mathematical Induction

Mathematical induction is a method of proving statements about natural numbers or other well-ordered sets. It is based on two principles:

- **Base case:** The statement is true for the smallest or first element of the set, usually denoted by 1 or 0.
- **Inductive step:** If the statement is true for some element of the set, then it is also true for the next element of the set, usually denoted by n+1.

Using these two principles, we can show that the statement is true for all elements of the set, by starting from the base case and applying the inductive step repeatedly.

## Example

Let us use mathematical induction to prove that the sum of the first n natural numbers is n(n+1)/2, for all n ≥ 1.

- **Base case:** When n = 1, the sum of the first natural number is 1, and 1(1+1)/2 = 1, so the statement is true for n = 1.
- **Inductive step:** Assume that the statement is true for some n ≥ 1, that is, the sum of the first n natural numbers is n(n+1)/2. We want to show that the statement is also true for n+1, that is, the sum of the first n+1 natural numbers is (n+1)(n+2)/2. To do this, we add n+1 to both sides of the equation:

  n(n+1)/2 + n+1 = (n+1)(n+2)/2

  Simplifying the left-hand side, we get:

  (n^2 + n + 2n + 2)/2 = (n+1)(n+2)/2

  Factoring out 2 from the numerator, we get:

  2(n^2 + 3n + 2)/2 = (n+1)(n+2)/2

  Cancelling out 2 from both sides, we get:

  n^2 + 3n + 2 = (n+1)(n+2)

  Expanding the right-hand side, we get:

  n^2 + 3n + 2 = n^2 + 3n + 2

  This shows that the statement is true for n+1, if it is true for n.

Therefore, by mathematical induction, the statement is true for all n ≥ 1.