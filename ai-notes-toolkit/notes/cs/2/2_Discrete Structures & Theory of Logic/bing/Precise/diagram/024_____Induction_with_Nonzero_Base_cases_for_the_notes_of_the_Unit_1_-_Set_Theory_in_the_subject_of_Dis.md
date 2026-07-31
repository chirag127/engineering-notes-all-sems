### Induction with Nonzero Base cases

Induction is a powerful mathematical tool used to prove statements about infinite sets of natural numbers. It is based on the principle of mathematical induction, which states that if a statement is true for the first natural number and if the statement is true for any natural number, then it is true for all natural numbers.

However, sometimes the base case for induction is not zero. In such cases, the principle of mathematical induction can still be applied, but with a slight modification. The base case is changed to the first natural number for which the statement is true, and the induction step is modified to show that if the statement is true for any natural number greater than or equal to the base case, then it is true for the next natural number.

Here is an example to illustrate this concept:

**Example:** Prove that for all integers n greater than or equal to 4, the following statement is true: `n^2 >= 3n + 4`

**Proof:**

1. **Base case:** When n = 4, the statement is true because `4^2 = 16` and `3 * 4 + 4 = 16`.
2. **Induction step:** Assume that the statement is true for some integer k greater than or equal to 4. That is, `k^2 >= 3k + 4`. We must show that the statement is also true for k + 1.
3. `k^2 >= 3k + 4` (by assumption)
4. `k^2 + 2k + 1 >= 3k + 4 + 2k + 1` (adding 2k + 1 to both sides)
5. `(k + 1)^2 >= 5k + 5` (simplifying)
6. `(k + 1)^2 >= 3(k + 1) + 4` (simplifying further)

Thus, by the principle of mathematical induction, the statement is true for all integers n greater than or equal to 4.

This is an example of how induction can be used with a nonzero base case to prove statements about sets of natural numbers. It is important to carefully choose the base case and modify the induction step accordingly to ensure that the proof is valid.