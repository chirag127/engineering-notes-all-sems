### Induction with Nonzero Base Cases

In mathematical induction, we prove that a statement is true for all positive integers by showing that it is true for the first positive integer (i.e., the base case) and then showing that if it is true for some positive integer k, then it must also be true for k+1 (i.e., the induction step). However, sometimes we need to prove that a statement is true for all integers greater than or equal to some nonzero integer n0. In this case, we use induction with nonzero base cases.

#### Steps of Induction with Nonzero Base Cases

1. **Base Case**: We first prove that the statement is true for some integer n = n0. This is called the base case. 

2. **Induction Hypothesis**: We assume that the statement is true for all integers k such that n0 ≤ k < n.

3. **Induction Step**: We prove that the statement is true for n+1.

#### Example

Let's use induction with nonzero base cases to prove the following statement for all integers n ≥ 2:

1 + 2 + 3 + ... + n = n(n+1)/2

**Base Case**: When n = 2, the statement becomes 1 + 2 = 2(2+1)/2 = 3, which is true.

**Induction Hypothesis**: Assume that the statement is true for all integers k such that 2 ≤ k < n.

**Induction Step**: We need to show that the statement is true for n+1. 

We have:

1 + 2 + 3 + ... + n + (n+1) = [1 + 2 + 3 + ... + n] + (n+1)

By the induction hypothesis, we know that 1 + 2 + 3 + ... + n = n(n+1)/2. Substituting this into the above equation, we get:

1 + 2 + 3 + ... + n + (n+1) = n(n+1)/2 + (n+1)

Simplifying this expression, we get:

1 + 2 + 3 + ... + n + (n+1) = (n+1)(n+2)/2

This is the same as the statement with n replaced by n+1. Therefore, the statement is true for all integers n ≥ 2.

#### Conclusion

Induction with nonzero base cases is a powerful tool for proving statements about integers that are greater than or equal to some nonzero integer. The key is to carefully choose the base case and to assume that the statement is true for all integers less than the current value of n. By using this technique, we can prove many interesting and important results in mathematics.