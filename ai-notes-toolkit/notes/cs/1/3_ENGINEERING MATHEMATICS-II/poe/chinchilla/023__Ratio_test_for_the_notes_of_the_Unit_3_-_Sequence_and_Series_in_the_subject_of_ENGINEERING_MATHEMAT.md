### Ratio Test

The ratio test is a convergence test for series that are not necessarily alternating. It is a useful tool for determining whether an infinite series converges or diverges.

#### Statement of the Ratio Test

Given a series $\sum_{n=1}^{\infty} a_n$, if
$$\lim_{n\to\infty}\frac{a_{n+1}}{a_n}=L$$
exists and $L<1$, then the series converges absolutely. If $L>1$ or if the limit does not exist, then the series diverges. If $L=1$, then the ratio test is inconclusive and another test must be used.

#### Steps for Applying the Ratio Test

To apply the ratio test to a series $\sum_{n=1}^{\infty} a_n$, follow these steps:

1. Compute the limit $\lim_{n\to\infty}\frac{a_{n+1}}{a_n}$.
2. If the limit exists and is less than 1, then the series converges absolutely.
3. If the limit is greater than 1 or does not exist, then the series diverges.
4. If the limit is equal to 1, then the ratio test is inconclusive and another test must be used.

#### Examples

1. Determine whether the series $\sum_{n=1}^{\infty} \frac{n^2}{2^n}$ converges or diverges using the ratio test.

   Solution:
   
   We have
   $$\lim_{n\to\infty}\frac{(n+1)^2}{2^{n+1}}\cdot\frac{2^n}{n^2}=\lim_{n\to\infty}\frac{(n+1)^2}{2n^2}=\frac{1}{2}<1,$$
   so the series converges absolutely.

2. Determine whether the series $\sum_{n=1}^{\infty} \frac{2^n}{n!}$ converges or diverges using the ratio test.

   Solution:
   
   We have
   $$\lim_{n\to\infty}\frac{2^{n+1}}{(n+1)!}\cdot\frac{n!}{2^n}=\lim_{n\to\infty}\frac{2}{n+1}=0,$$
   so the series converges absolutely.

3. Determine whether the series $\sum_{n=1}^{\infty} \frac{n!}{n^n}$ converges or diverges using the ratio test.

   Solution:
   
   We have
   $$\lim_{n\to\infty}\frac{(n+1)!}{(n+1)^{n+1}}\cdot\frac{n^n}{n!}=\lim_{n\to\infty}\frac{(n+1)^n}{(n+1)n}=\lim_{n\to\infty}\left(1+\frac{1}{n}\right)^n=e,$$
   where $e$ is the mathematical constant approximately equal to 2.71828. Since $e>1$, the series diverges.