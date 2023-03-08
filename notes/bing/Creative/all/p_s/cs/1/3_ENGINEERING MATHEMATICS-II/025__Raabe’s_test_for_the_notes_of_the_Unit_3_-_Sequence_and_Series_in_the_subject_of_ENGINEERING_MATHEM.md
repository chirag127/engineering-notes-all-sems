### Raabe's test

Raabe's test is a test for the convergence of a series of the form

$$\sum_{n=1}^{\infty} a_n$$

where each term is a real or complex number. The test was developed by Swiss mathematician Joseph Ludwig Raabe.

The test is based on the ratio of consecutive terms of the series, and the limit of a certain expression involving this ratio. The test states that:

- If $$\lim_{n \to \infty} n \left(\left|\frac{a_n}{a_{n+1}}\right| - 1\right) = R$$ and $$R > 1$$, then the series converges.
- If $$\lim_{n \to \infty} n \left(\left|\frac{a_n}{a_{n+1}}\right| - 1\right) = R$$ and $$R < 1$$, then the series diverges.
- If $$\lim_{n \to \infty} n \left(\left|\frac{a_n}{a_{n+1}}\right| - 1\right) = 1$$, then the test is inconclusive and another test is needed.

The test can be derived from Kummer's test, which is a more general test for the convergence of series.

An example of a series that can be tested by Raabe's test is

$$\sum_{n=1}^{\infty} \frac{n!}{n^n}$$

The ratio of consecutive terms is

$$\left|\frac{a_n}{a_{n+1}}\right| = \frac{(n+1)^n}{n^{n+1}} = \left(\frac{n+1}{n}\right)^n \frac{1}{n} = \frac{e^n}{n^2} \left(1 + \frac{1}{n}\right)^{-n}$$

Using L'Hopital's rule, we can find the limit of this ratio as

$$\lim_{n \to \infty} \left|\frac{a_n}{a_{n+1}}\right| = \lim_{n \to \infty} \frac{e^n}{n^2} \left(1 + \frac{1}{n}\right)^{-n} = \lim_{n \to \infty} \frac{e}{n} \left(1 + \frac{1}{n}\right)^{-n} = 0$$

Therefore, the limit of the expression in Raabe's test is

$$\lim_{n \to \infty} n \left(\left|\frac{a_n}{a_{n+1}}\right| - 1\right) = \lim_{n \to \infty} n \left(0 - 1\right) = -\infty$$

Since this limit is less than 1, the series diverges by Raabe's test.

One possible mnemonic to remember Raabe's test is:

- R for Raabe
- R for Ratio
- R for Result

If the result of the limit is greater than 1, the series converges. If the result is less than 1, the series diverges. If the result is equal to 1, the test is inconclusive.

Another possible learning trick is to compare Raabe's test with the ratio test, which is another test for the convergence of series. The ratio test states that:

- If $$\lim_{n \to \infty} \left|\frac{a_{n+1}}{a_n}\right| = L$$ and $$L < 1$$, then the series converges.
- If $$\lim_{n \to \infty} \left|\frac{a_{n+1}}{a_n}\right| = L$$ and $$L > 1$$, then the series diverges.
- If $$\lim_{n \to \infty} \left|\frac{a_{n+1}}{a_n}\right| = 1$$, then the test is inconclusive and another test is needed.

The difference between Raabe's test and the ratio test is that Raabe's test uses the inverse ratio and multiplies it by n, and then subtracts 1 from it. This makes Raabe's test more sensitive to the behavior of the series, and sometimes allows it to give a conclusive answer when the ratio test fails. However, Raabe's test also fails when the limit is equal to 1, so another test is needed in that case.