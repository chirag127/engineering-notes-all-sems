### Tests for Convergence of Series

In the study of sequence and series, one of the most important concepts is the convergence of a series. The convergence of a series is the property that determines whether the series has a finite sum or not. In this section, we will discuss the various tests for convergence of series.

1. **Divergence Test**: The divergence test is the simplest test for convergence of series. If the limit of the nth term of a series does not approach zero, then the series diverges. Mathematically, we can express the divergence test as follows:

   ```
   If lim(n->∞) an ≠ 0, then the series ∑an diverges.
   ```

2. **Comparison Test**: The comparison test is used to determine the convergence or divergence of a series by comparing it with another series that is known to converge or diverge. The comparison test can be expressed as follows:

   ```
   Let ∑an and ∑bn be two series such that 0 ≤ an ≤ bn for all n ≥ N, where N is some fixed positive integer. If ∑bn converges, then ∑an also converges. If ∑an diverges, then ∑bn also diverges.
   ```

3. **Limit Comparison Test**: The limit comparison test is a variation of the comparison test. It is used when the comparison test fails to provide conclusive results. The limit comparison test can be expressed as follows:

   ```
   Let ∑an and ∑bn be two series such that an, bn > 0 for all n. If lim(n->∞) an/bn = c, where c is a finite positive constant, then both series converge or both series diverge.
   ```

4. **Integral Test**: The integral test is used to determine the convergence or divergence of a series by comparing it with an integral. The integral test can be expressed as follows:

   ```
   Let f(x) be a continuous, positive, and decreasing function on [1, ∞) such that f(n) = an for all n. If the integral ∫1^∞ f(x) dx converges, then the series ∑an also converges. If the integral diverges, then the series also diverges.
   ```

5. **Alternating Series Test**: The alternating series test is used to determine the convergence of an alternating series. An alternating series is a series in which the signs of the terms alternate between positive and negative. The alternating series test can be expressed as follows:

   ```
   Let ∑(-1)^n-1 an be an alternating series such that an > 0 for all n. If lim(n->∞) an = 0 and an+1 ≤ an for all n, then the series converges.
   ```

These are some of the common tests for convergence of series. It is important to note that these tests do not provide the value of the sum of the series, but only determine whether the series converges or diverges.