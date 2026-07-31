### Induction with Nonzero Base cases

Induction is a powerful mathematical tool that can be used to prove statements about infinite sets of natural numbers. The principle of induction states that if a statement is true for the first natural number (usually 1), and if the statement being true for any natural number implies that it is true for the next natural number, then the statement is true for all natural numbers.

However, sometimes the base case for induction is not 1, but some other natural number. In such cases, we can still use induction to prove the statement, but we need to modify the base case accordingly.

For example, let's say we want to prove that the statement "n^2 > 2n + 1" is true for all natural numbers n greater than or equal to 3. In this case, the base case is not 1, but 3. So, we need to first prove that the statement is true for n = 3. This can be done by direct calculation: 3^2 = 9, and 2 * 3 + 1 = 7, so 9 > 7, and the statement is true for n = 3.

Next, we need to show that if the statement is true for some natural number k greater than or equal to 3, then it is also true for k + 1. This is done by assuming that k^2 > 2k + 1, and then showing that (k + 1)^2 > 2(k + 1) + 1. This can be done by expanding the left-hand side and simplifying: (k + 1)^2 = k^2 + 2k + 1 > 2k + 1 + 2k + 1 = 2(k + 1) + 1.

Thus, by induction, we have shown that the statement "n^2 > 2n + 1" is true for all natural numbers n greater than or equal to 3.

In summary, when using induction with a nonzero base case, we need to first prove that the statement is true for the base case, and then show that if the statement is true for some natural number greater than or equal to the base case, then it is also true for the next natural number. This allows us to use induction to prove statements about infinite sets of natural numbers, even when the base case is not 1.