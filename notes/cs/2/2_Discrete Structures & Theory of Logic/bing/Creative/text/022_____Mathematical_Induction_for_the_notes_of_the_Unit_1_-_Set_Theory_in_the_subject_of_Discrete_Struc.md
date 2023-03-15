### Mathematical Induction

- Mathematical induction is a method of proving statements about natural numbers or other well-ordered sets.
- The basic principle of mathematical induction is that if a statement is true for some initial value and if it remains true when the value is increased by one, then it is true for all values in the set.
- The steps of mathematical induction are as follows:
  - **Base case**: Show that the statement is true for the smallest or first value in the set, usually denoted by n = 1 or n = 0.
  - **Inductive hypothesis**: Assume that the statement is true for some arbitrary value n = k, where k is a natural number or an element of the set.
  - **Inductive step**: Show that the statement is true for the next value n = k + 1, using the inductive hypothesis and logical reasoning.
  - **Conclusion**: By the principle of mathematical induction, the statement is true for all values of n in the set.
- An example of mathematical induction is to prove that the sum of the first n natural numbers is n(n + 1) / 2 for all n ≥ 1.
  - **Base case**: When n = 1, the sum of the first natural number is 1, which is equal to 1(1 + 1) / 2. Hence, the statement is true for n = 1.
  - **Inductive hypothesis**: Assume that the statement is true for some arbitrary value n = k, that is, the sum of the first k natural numbers is k(k + 1) / 2.
  - **Inductive step**: We need to show that the statement is true for n = k + 1, that is, the sum of the first k + 1 natural numbers is (k + 1)((k + 1) + 1) / 2. Using the inductive hypothesis, we can write the sum of the first k + 1 natural numbers as follows:

    ```
    1 + 2 + ... + k + (k + 1) = (k(k + 1) / 2) + (k + 1)
                             = (k + 1)(k / 2 + 1)
                             = (k + 1)((k + 1) + 1) / 2
    ```

    Hence, the statement is true for n = k + 1.
  - **Conclusion**: By the principle of mathematical induction, the statement is true for all n ≥ 1.