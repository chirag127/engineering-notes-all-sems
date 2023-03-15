### Leibnitz Theorem

- Leibnitz theorem is a generalization of the product rule of differentiation. It states that if two functions, say u(x) and v(x), are differentiable n times, then their product u(x).v(x) is also differentiable n times .
- The formula for the nth derivative of the product of two functions is given by :

$$
(uv)^{(n)} = \sum_{k=0}^n {n \choose k} u^{(n-k)}v^{(k)}
$$

where ${n \choose k}$ is the binomial coefficient and $u^{(n)}$ and $v^{(n)}$ denote the nth derivatives of u and v respectively.

- The proof of the Leibnitz theorem is based on induction and the product rule of differentiation. The base case is when n = 1, which is just the product rule:

$$
(uv)^{(1)} = u^{(1)}v + uv^{(1)}
$$

Assuming that the formula holds for n = m, we can prove it for n = m + 1 by applying the product rule again:

$$
\begin{aligned}
(uv)^{(m+1)} &= \frac{d}{dx} (uv)^{(m)} \\
&= \frac{d}{dx} \left( \sum_{k=0}^m {m \choose k} u^{(m-k)}v^{(k)} \right) \\
&= \sum_{k=0}^m {m \choose k} \left( u^{(m-k+1)}v^{(k)} + u^{(m-k)}v^{(k+1)} \right) \\
&= \sum_{k=0}^m {m \choose k} u^{(m-k+1)}v^{(k)} + \sum_{k=0}^m {m \choose k} u^{(m-k)}v^{(k+1)} \\
&= \sum_{k=0}^{m+1} {m \choose k} u^{(m-k+1)}v^{(k)} + \sum_{k=1}^{m+1} {m \choose k-1} u^{(m-k+1)}v^{(k)} \\
&= {m \choose 0} u^{(m+1)}v^{(0)} + \sum_{k=1}^m \left( {m \choose k} + {m \choose k-1} \right) u^{(m-k+1)}v^{(k)} + {m \choose m} u^{(0)}v^{(m+1)} \\
&= {m+1 \choose 0} u^{(m+1)}v^{(0)} + \sum_{k=1}^m {m+1 \choose k} u^{(m-k+1)}v^{(k)} + {m+1 \choose m+1} u^{(0)}v^{(m+1)} \\
&= \sum_{k=0}^{m+1} {m+1 \choose k} u^{(m-k+1)}v^{(k)}
\end{aligned}
$$

where we have used the identity ${m \choose k} + {m \choose k-1} = {m+1 \choose k}$ and the convention that ${n \choose k} = 0$ if k < 0 or k > n.

- Some examples of applying the Leibnitz theorem are:

  - If u(x) = sin x and v(x) = cos x, then

    $$
    \begin{aligned}
    (uv)^{(n)} &= \sum_{k=0}^n {n \choose k} u^{(n-k)}v^{(k)} \\
    &= \sum_{k=0}^n {n \choose k} (\sin x)^{(n-k)} (\cos x)^{(k)} \\
    &= \sum_{k=0}^n {n \choose k} \sin \left( x + \frac{(n-k)\pi}{2} \right) \cos \left( x + \frac{k\pi}{2} \right) \\
    &= \sum_{k=0}^n {