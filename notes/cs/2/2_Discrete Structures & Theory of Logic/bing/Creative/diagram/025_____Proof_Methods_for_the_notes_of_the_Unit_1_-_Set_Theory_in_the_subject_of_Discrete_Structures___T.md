### Proof Methods

A proof is a logical argument that establishes the validity of a statement or a theorem. There are different methods of proof, depending on the type of statement and the context of the problem. Some of the common proof methods are:

- **Direct proof**: A direct proof shows that a statement of the form "if p, then q" is true by assuming that p is true and then using logical rules and definitions to derive q. For example, to prove that if n is an even integer, then n^2 is also even, we can assume that n is even and write n = 2k for some integer k. Then, n^2 = (2k)^2 = 4k^2 = 2(2k^2), which is also even by definition.

- **Indirect proof**: An indirect proof shows that a statement of the form "if p, then q" is true by assuming that q is false and then using logical rules and definitions to derive a contradiction. This implies that q cannot be false, and hence p implies q. For example, to prove that if n is an odd integer, then n^2 is also odd, we can assume that n^2 is even and write n^2 = 2k for some integer k. Then, n = sqrt(2k), which is not an integer by the irrationality of sqrt(2), contradicting the assumption that n is odd.

- **Contrapositive proof**: A contrapositive proof shows that a statement of the form "if p, then q" is true by proving that its contrapositive, "if not q, then not p", is true. This is valid because p implies q is logically equivalent to not q implies not p. For example, to prove that if n is a prime number, then n is not divisible by 4, we can prove that if n is divisible by 4, then n is not a prime number. This is obvious because n = 4k for some integer k, and n has a factor other than 1 and itself.

- **Proof by cases**: A proof by cases shows that a statement is true by considering all the possible cases that can occur and proving the statement for each case. For example, to prove that the absolute value of any integer is non-negative, we can consider two cases: n >= 0 and n < 0. In the first case, |n| = n, which is non-negative by assumption. In the second case, |n| = -n, which is also non-negative because -n >= 0.

- **Proof by contradiction**: A proof by contradiction shows that a statement is true by assuming that it is false and then using logical rules and definitions to derive a contradiction. This implies that the statement cannot be false, and hence it is true. For example, to prove that there is no largest natural number, we can assume that there is a largest natural number, say N. Then, N + 1 is also a natural number, and N + 1 > N, contradicting the assumption that N is the largest.

- **Proof by induction**: A proof by induction shows that a statement is true for all natural numbers by proving two steps: the base case and the induction step. The base case shows that the statement is true for some initial value, usually 0 or 1. The induction step shows that if the statement is true for some value k, then it is also true for k + 1. By applying the induction step repeatedly, we can conclude that the statement is true for all natural numbers. For example, to prove that the sum of the first n natural numbers is n(n + 1) / 2, we can use induction as follows:

  - Base case: When n = 1, the sum of the first natural number is 1, and 1(1 + 1) / 2 = 1, so the statement is true for n = 1.
  - Induction step: Assume that the statement is true for some k, that is, the sum of the first k natural numbers is k(k + 1) / 2. Then, the sum of the first k + 1 natural numbers is (k + 1) + the sum of the first k natural numbers, which is (k + 1) + k(k + 1) / 2 by the induction hypothesis. Simplifying, we get (k + 1)(k + 2) / 2, which is the same as (k + 1)((k + 1) + 1) / 2, so the statement is true for k + 1.

  - Conclusion: By induction, the