### Chinese Remainder Theorem

- The Chinese remainder theorem is a theorem that gives a unique solution to a system of simultaneous linear congruences with coprime moduli.
- In other words, it allows us to find an integer that has a given remainder when divided by several given divisors, as long as the divisors are pairwise coprime (no two divisors share a common factor other than 1).
- For example, if we want to find an integer that has a remainder of 2 when divided by 3, a remainder of 3 when divided by 5, and a remainder of 2 when divided by 7, we can use the Chinese remainder theorem to find that the answer is 23 (modulo 105, the product of 3, 5, and 7).
- The Chinese remainder theorem has many applications in cryptography, number theory, and computer science, as it allows us to work with large numbers by breaking them down into smaller ones.
- The theorem was first stated by the Chinese mathematician Sun-tzu in the 3rd century CE, and later generalized and proved by other mathematicians such as Aryabhata, Brahmagupta, Fibonacci, Qin Jiushao, and Gauss.

#### Statement and Proof

- The Chinese remainder theorem can be stated as follows:

Given pairwise coprime positive integers $n_1, n_2, \ldots, n_k$ and arbitrary integers $a_1, a_2, \ldots, a_k$, the system of simultaneous congruences
\begin{align*}
  x &\equiv a_1 \pmod {n_1}\\
  x &\equiv a_2 \pmod {n_2}\\
  & \vdots\\
  x &\equiv a_k \pmod {n_k}
\end{align*}
has a solution, and the solution is unique modulo $N = n_1n_2\cdots n_k$.

- The proof of the theorem is based on the following steps:

1. Compute $N = n_1 \times n_2 \times \cdots \times n_k$.
2. For each $i = 1, 2, \ldots, k$, compute $y_i = \frac{N}{n_i} = n_1n_2 \cdots n_{i-1}n_{i+1} \cdots n_k$.
3. For each $i = 1, 2, \ldots, k$, compute $z_i \equiv y_i^{-1} \bmod {n_i}$ using the extended Euclidean algorithm ($z_i$ exists since $n_1, n_2, \ldots, n_k$ are pairwise coprime).
4. The integer $x = \sum_{i=1}^k a_i y_i z_i$ is a solution to the system of congruences, and $x \bmod N$ is the unique solution modulo $N$.

- To see why $x$ is a solution, for each $i = 1, 2, \ldots, k$, we have
\begin{align*}
x & \equiv (a_1 y_1 z_1 + a_2y_2z_2 + \cdots+ a_k y_k z_k) \pmod {n_i}\\
& \equiv a_i y_i z_i \pmod {n_i} \\
& \equiv a_i \pmod {n_i},
\end{align*}
where the second line follows since $y_j \equiv 0 \bmod {n_i}$ for each $j \neq i$, and the third line follows since $y_i z_i \equiv 1 \bmod {n_i}$.

- Now, suppose there are two solutions $u$ and $v$ to the system of congruences. Then $n_1 \mid (u -v), n_2 \mid (u-v), \ldots, n_k \mid (u-v)$, and since $n_1, n_2, \ldots, n_k$ are relatively prime, we have that $n_1n_2\cdots n_k$ divides $u-v$, or $u \equiv v \pmod {n_1n_2\cdots n_k}$. Thus, the solution is unique modulo $n_1n_2\cdots n_k$.

#### Example