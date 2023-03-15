### Algebraic Method Using Arden’s Theorem

Arden’s theorem is a mathematical statement that can be used to find a regular expression for a given finite automaton. It is also called Arden’s lemma. The theorem is stated as follows:

**Theorem:** If P and Q are two regular expressions over Σ, and if P does not contain ε, then the following equation in R given by R = Q + RP has a unique solution i.e., R = QP*.

**Proof:** R = Q + RP

R = Q + (Q + RP)P [After putting the value R = Q + RP]

R = Q + QP*P [By Arden’s theorem]

R = Q( + P*P)

R = QP* ( P*P = ε, + ε = P*)

Hence, R = QP* is the unique solution.

**Example:** Find a regular expression for the following finite automaton using Arden’s theorem.

![Finite automaton](https://www.geeksforgeeks.org/wp-content/uploads/Arden-1.png)

**Solution:** We can write the following equations for each state:

q0 = q0a + q1b + ε

q1 = q0a + q2b

q2 = q2a + q2b

We can solve these equations using Arden’s theorem as follows:

q0 = q0a + q1b + ε

q0 = (q0a + q1b + ε)a*

q0 = (q1b + ε)a*

q0 = q1ba* + a*

q1 = q0a + q2b

q1 = (q1ba* + a*)a + q2b

q1 = q1ba*a + a*a + q2b

q1 = (a*a + q2b)ba*

q1 = (a* + q2b)ba*

q2 = q2a + q2b

q2 = (q2a + q2b)(a + b)*

q2 = (a + b)*

Now, we can substitute the value of q2 in q1 and get:

q1 = (a* + (a + b)*)ba*

q1 = (a* + a* + b*)ba*

q1 = (a + b*)ba*

Finally, we can substitute the value of q1 in q0 and get:

q0 = (a + b*)ba*ba* + a*

q0 = (a + b*)ba* + a*

This is the regular expression for the given finite automaton.