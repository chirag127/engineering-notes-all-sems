Hello, I am Sydney, your AI assistant. I can help you with your study material for Discrete Structures & Theory of Logic. Here is the content for the topic of Mathematical Induction:

### Mathematical Induction

Mathematical induction is a method of proving statements about natural numbers or other well-ordered sets. It is based on two principles:

- **Basis step**: The statement is true for the smallest element in the set, usually 1 or 0.
- **Inductive step**: If the statement is true for some element k in the set, then it is also true for the next element k+1.

Using these two steps, we can show that the statement is true for all elements in the set, by starting from the smallest element and applying the inductive step repeatedly.

#### Example

Let us use mathematical induction to prove that the sum of the first n natural numbers is n(n+1)/2, for all n >= 1.

- **Basis step**: When n = 1, the sum of the first natural number is 1, which is equal to 1(1+1)/2. So the statement is true for n = 1.
- **Inductive step**: Assume that the statement is true for some n = k, that is, the sum of the first k natural numbers is k(k+1)/2. We want to show that the statement is also true for n = k+1, that is, the sum of the first k+1 natural numbers is (k+1)(k+2)/2. To do this, we add k+1 to both sides of the equation:

  k(k+1)/2 + (k+1) = (k+1)(k+2)/2

  Simplifying, we get:

  (k+1)(k+1)/2 = (k+1)(k+2)/2

  Which is true for all k >= 1. Therefore, the statement is true for n = k+1, if it is true for n = k.

By the principle of mathematical induction, the statement is true for all n >= 1.