### D’ Alembert’s test for the notes of the Unit 3 - Sequence and Series in the subject of ENGINEERING MATHEMATICS-II

D’ Alembert’s test, also known as the ratio test, is a method used to determine the convergence or divergence of a series. Here are the important points to understand about this test:

- The test is applied to a series of positive terms only.
- The test compares the ratio of consecutive terms to a limit.
- If the limit is less than 1, the series converges absolutely.
- If the limit is greater than 1, the series diverges.
- If the limit is equal to 1, the test is inconclusive, and another test should be used.

Let's take an example and apply D’ Alembert’s test to it:

**Example:**

Consider the series `∑(n=1 to infinity) (n^2)/(2^n)`

**Solution:**

1. Find the ratio of consecutive terms:

```
a(n+1)/a(n) = [(n+1)^2]/[2^(n+1)] * [2^n]/[n^2]
            = (n+1)^2 / [2n^2]
```

2. Take the limit of the ratio as n approaches infinity:

```
lim n->∞ [(n+1)^2 / 2n^2] = 1/2 < 1
```

Since the limit is less than 1, the series converges absolutely.

In conclusion, D’ Alembert’s test is a powerful tool for determining the convergence or divergence of a series. It is important to remember that the test can only be applied to series of positive terms, and that an inconclusive result means that another test should be used.