### Mathematical Induction

- Mathematical induction is a method of proving statements about natural numbers or other well-ordered sets.
- The basic idea is to show that a statement is true for some initial element of the set, and then show that if it is true for any element, it is also true for the next element in the order.
- This implies that the statement is true for all elements of the set by the principle of well-ordering, which states that every non-empty subset of a well-ordered set has a least element.
- The method of mathematical induction consists of two steps: the base case and the induction step.
- The base case is to verify that the statement is true for the smallest or first element of the set, usually denoted by 1 or 0.
- The induction step is to assume that the statement is true for some element k of the set, and then show that it is also true for k+1, the next element in the order. This is called the induction hypothesis and the induction conclusion, respectively.
- An example of a statement that can be proved by mathematical induction is the following: for any natural number n, the sum of the first n natural numbers is equal to n(n+1)/2. That is, 1 + 2 + ... + n = n(n+1)/2.
- To prove this by mathematical induction, we first check the base case: for n = 1, the statement is true, since 1 = 1(1+1)/2.
- Then, we assume the induction hypothesis: for some k, the statement is true, that is, 1 + 2 + ... + k = k(k+1)/2.
- Next, we show the induction conclusion: for k+1, the statement is also true, that is, 1 + 2 + ... + (k+1) = (k+1)((k+1)+1)/2.
- To do this, we add k+1 to both sides of the induction hypothesis, and simplify the result using algebra. We get:

1 + 2 + ... + k + (k+1) = k(k+1)/2 + (k+1)

= (k+1)(k/2 + 1)

= (k+1)(k+2)/2

= (k+1)((k+1)+1)/2

- This shows that the statement is true for k+1, and completes the induction step.
- Therefore, by mathematical induction, the statement is true for all natural numbers n.