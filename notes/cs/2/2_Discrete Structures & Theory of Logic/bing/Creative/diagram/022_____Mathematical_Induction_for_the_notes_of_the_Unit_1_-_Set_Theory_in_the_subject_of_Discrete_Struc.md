Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of mathematical induction for the notes of the unit 1 - set theory in the subject of discrete structures and theory of logic.

### Mathematical Induction

Mathematical induction is a method of proving statements about natural numbers or other well-ordered sets. It is based on two principles:

- **Base case**: The statement is true for the smallest or first element of the set, usually denoted by 1 or 0.
- **Inductive step**: If the statement is true for some element of the set, then it is also true for the next element of the set, usually denoted by n+1.

The idea is to show that the statement holds for all elements of the set by starting from the base case and applying the inductive step repeatedly.

#### Example

Let us use mathematical induction to prove that the sum of the first n natural numbers is n(n+1)/2. That is, we want to show that for all n >= 1,

1 + 2 + ... + n = n(n+1)/2

**Base case**: When n = 1, the left-hand side is 1 and the right-hand side is 1(1+1)/2 = 1, so the statement is true.

**Inductive step**: Assume that the statement is true for some n >= 1, that is,

1 + 2 + ... + n = n(n+1)/2

We want to show that it is also true for n+1, that is,

1 + 2 + ... + n + (n+1) = (n+1)(n+2)/2

To do this, we can add (n+1) to both sides of the assumed equation and simplify:

1 + 2 + ... + n + (n+1) = n(n+1)/2 + (n+1)

= (n+1)(n/2 + 1)

= (n+1)(n+2)/2

This is exactly what we wanted to show. Therefore, by mathematical induction, the statement is true for all n >= 1.