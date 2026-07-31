### Leibnitz Theorem

- Leibnitz theorem is a generalization of the product rule of differentiation.
- It states that if there are two functions a(x) and b(x) that are both n times differentiable, then their product a(x)b(x) is also n times differentiable and its nth derivative is given by

$$
\frac{d^n}{dx^n}(a(x)b(x)) = \sum_{k=0}^n \binom{n}{k} \frac{d^k}{dx^k}a(x) \frac{d^{n-k}}{dx^{n-k}}b(x)
$$

- where $\binom{n}{k}$ is the binomial coefficient.
- The theorem can be proved by induction on n, using the product rule and the binomial theorem.
- The theorem can be used to find the derivatives of products of functions, such as polynomials, trigonometric functions, exponential functions, etc.
- For example, if a(x) = $x^2$ and b(x) = $\sin x$, then the fourth derivative of their product is

$$
\frac{d^4}{dx^4}(x^2 \sin x) = \sum_{k=0}^4 \binom{4}{k} \frac{d^k}{dx^k}x^2 \frac{d^{4-k}}{dx^{4-k}}\sin x
$$

$$
= \binom{4}{0} \frac{d^0}{dx^0}x^2 \frac{d^4}{dx^4}\sin x + \binom{4}{1} \frac{d^1}{dx^1}x^2 \frac{d^3}{dx^3}\sin x + \binom{4}{2} \frac{d^2}{dx^2}x^2 \frac{d^2}{dx^2}\sin x + \binom{4}{3} \frac{d^3}{dx^3}x^2 \frac{d^1}{dx^1}\sin x + \binom{4}{4} \frac{d^4}{dx^4}x^2 \frac{d^0}{dx^0}\sin x
$$

$$
= 1 \cdot x^2 \cdot (-\sin x) + 4 \cdot 2x \cdot (-\cos x) + 6 \cdot 2 \cdot (\sin x) + 4 \cdot 6x \cdot (\cos x) + 1 \cdot 12 \cdot (-\sin x)
$$

$$
= -12x^2 \sin x - 8x \cos x + 12 \sin x
$$

- The theorem can also be extended to functions of several variables, partial derivatives, and integrals. See  and  for more details.