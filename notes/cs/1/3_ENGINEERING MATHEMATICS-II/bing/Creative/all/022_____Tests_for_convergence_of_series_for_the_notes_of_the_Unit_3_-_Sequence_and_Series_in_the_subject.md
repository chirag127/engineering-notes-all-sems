Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of Tests for convergence of series for the notes of the Unit 3 - Sequence and Series in the subject of ENGINEERING MATHEMATICS-II.

# Tests for convergence of series

A series is a sum of an infinite sequence of terms, such as

$$
\sum_{n=1}^{\infty} a_n = a_1 + a_2 + a_3 + \cdots
$$

A series is said to be convergent if the sum of the terms approaches a finite limit as the number of terms increases. Otherwise, the series is divergent.

There are various tests that can be used to determine whether a series is convergent or divergent. Some of the common tests are:

- **The nth term test**: This test states that if the limit of the nth term of a series is not zero, then the series is divergent. That is,

$$
\lim_{n \to \infty} a_n \neq 0 \implies \sum_{n=1}^{\infty} a_n \text{ is divergent}
$$

- **The integral test**: This test states that if a series has positive, decreasing terms and is related to a continuous, positive, decreasing function $f(x)$, then the series and the improper integral of $f(x)$ over the interval $[1, \infty)$ have the same convergence behavior. That is,

$$
\sum_{n=1}^{\infty} a_n \text{ and } \int_{1}^{\infty} f(x) dx \text{ are both convergent or both divergent}
$$

- **The comparison test**: This test states that if a series has positive terms and is smaller than a convergent series, then the series is also convergent. Similarly, if a series has positive terms and is larger than a divergent series, then the series is also divergent. That is,

$$
0 \leq a_n \leq b_n \text{ and } \sum_{n=1}^{\infty} b_n \text{ is convergent} \implies \sum_{n=1}^{\infty} a_n \text{ is convergent}
$$

$$
0 \leq b_n \leq a_n \text{ and } \sum_{n=1}^{\infty} b_n \text{ is divergent} \implies \sum_{n=1}^{\infty} a_n \text{ is divergent}
$$

- **The limit comparison test**: This test states that if a series has positive terms and is related to another series with positive terms by a finite limit, then the series have the same convergence behavior. That is,

$$
\lim_{n \to \infty} \frac{a_n}{b_n} = L \text{ where } 0 < L < \infty \implies \sum_{n=1}^{\infty} a_n \text{ and } \sum_{n=1}^{\infty} b_n \text{ are both convergent or both divergent}
$$

- **The ratio test**: This test states that if the limit of the ratio of the absolute values of consecutive terms of a series exists and is less than one, then the series is absolutely convergent. If the limit is greater than one, then the series is divergent. If the limit is equal to one, then the test is inconclusive. That is,

$$
\lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right| = L \text{ where } L < 1 \implies \sum_{n=1}^{\infty} a_n \text{ is absolutely convergent}
$$

$$
\lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right| = L \text{ where } L > 1 \implies \sum_{n=1}^{\infty} a_n \text{ is divergent}
$$

$$
\lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right| = 1 \implies \sum_{n=1}^{\infty} a_n \text{ may be convergent or divergent}
$$

- **The root test**: This test states that if the limit of