### Induction with Nonzero Base cases

- Induction is a method of proving statements of the form $\forall n \in \mathbb{N}, P(n)$, where $P(n)$ is some predicate involving $n$.
- The basic idea of induction is to show that $P(n)$ holds for some initial value of $n$, called the base case, and then show that if $P(n)$ holds for any $n$, then it also holds for $n+1$, called the induction step.
- The base case is usually $n=0$, but sometimes it can be a different value, such as $n=1$ or $n=2$. This is called induction with nonzero base cases.
- The reason why induction with nonzero base cases works is that the induction step implies the base case, so it doesn't need to be mentioned separately. For example, if we want to prove that $\forall n \in \mathbb{N}, n \geq 1 \implies P(n)$, we can use the induction step $P(n) \implies P(n+1)$, and then show that $P(1)$ is true. This is because there is no $n < 1$ in $\mathbb{N}$, so the statement $\forall n < 1, P(n)$ is vacuously true. And therefore if the induction step has been shown true, $P(1)$ must also be true.
- However, sometimes it is easier or more natural to prove the base case separately, especially if the induction step is more complicated or involves more cases. For example, if we want to prove that $\forall n \in \mathbb{N}, n \geq 2 \implies P(n)$, where $P(n)$ is some complicated formula, we might want to show that $P(2)$ is true by direct computation, and then use the induction step $P(n) \implies P(n+1)$ for $n \geq 2$.
- The general form of induction with nonzero base cases is as follows:

  - Let $k$ be some fixed natural number, and let $P(n)$ be some predicate involving $n$.
  - To prove that $\forall n \in \mathbb{N}, n \geq k \implies P(n)$, we need to show two things:
    - Base case: $P(k)$ is true.
    - Induction step: $\forall n \in \mathbb{N}, n \geq k \implies (P(n) \implies P(n+1))$.

- Here are some examples of induction with nonzero base cases:

  - Example 1: Prove that $\forall n \in \mathbb{N}, n \geq 1 \implies 2^n > n$.

    - Base case: $n=1$. Then $2^1 > 1$, which is true.
    - Induction step: Assume that $n \geq 1$ and $2^n > n$. We want to show that $2^{n+1} > n+1$. We have:

      $$2^{n+1} = 2 \cdot 2^n > 2 \cdot n > n+1$$

      The first inequality follows from the induction hypothesis, the second inequality follows from the fact that $n \geq 1$, and the third inequality follows from the fact that $n+1 > 1$. Therefore, $2^{n+1} > n+1$, as required.

  - Example 2: Prove that $\forall n \in \mathbb{N}, n \geq 2 \implies n! > 2^n$.

    - Base case: $n=2$. Then $2! = 2 > 2^2 = 4$, which is true.
    - Induction step: Assume that $n \geq 2$ and $n! > 2^n$. We want to show that $(n+1)! > 2^{n+1}$. We have:

      $$(n+1)! = (n+1) \cdot n! > (n+1) \cdot 2^n > 2 \cdot 2^n = 2^{n+1}$$

      The first inequality follows from the induction hypothesis, the second inequality follows from the fact that $n+1 > 2$, and the third equality follows from the definition of exponent

Some possible mnemonics and learning tricks for the topic are:

- To remember the general form of induction with nonzero base cases, you can use the acronym BIKES: Base case, Induction hypothesis, k is fixed, n is greater than or equal to k, and Step.
- To remember the difference between induction with zero and nonzero base cases, you can use the analogy of climbing a ladder. In induction with zero base case, you start from the bottom rung and climb up one rung at a time. In induction with nonzero base case, you start from some higher rung and climb up one rung at a time. The higher rung is the base case, and the climbing up is the induction step.
- To remember the induction step, you can use the phrase "assume and prove". You assume that the statement is true for some value of n, and then you prove that it is true for the next value of n. You can also use the phrase "show and tell". You show that the statement is true for the next value of n, and then you tell why it follows from the induction hypothesis and other facts.