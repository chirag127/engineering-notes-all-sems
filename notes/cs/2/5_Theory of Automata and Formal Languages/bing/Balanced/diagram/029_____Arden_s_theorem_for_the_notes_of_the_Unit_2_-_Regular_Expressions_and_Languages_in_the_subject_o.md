### Arden's Theorem

- Arden's theorem is a mathematical statement that relates regular expressions and languages.
- Arden's theorem can be used to find a regular expression that represents the language accepted by a finite automaton.
- Arden's theorem states that if P and Q are two regular expressions over an alphabet , and if P does not contain the empty string , then the following equation in R has a unique solution:

  R = Q + RP

  The solution is:

  R = QP*

- The proof of Arden's theorem is based on the following steps:

  - Assume that R is a solution of the equation R = Q + RP.
  - Show that R is a subset of QP* by induction on the length of strings in R.
  - Show that QP* is a subset of R by induction on the number of occurrences of P in strings in QP*.
  - Conclude that R = QP*.

- An example of applying Arden's theorem to find a regular expression for a finite automaton is given below:

  - Consider the following finite automaton:

    ![Finite automaton](https://www.geeksforgeeks.org/wp-content/uploads/FA-1.png)

  - Write the equations for the final states q1 and q3 in terms of regular expressions:

    q1 = q1.0 + q2

    q3 = q2.1 + q3.0 + q3.1

  - Solve for q2 using Arden's theorem:

    q2 = q1.1 + q2.0

    q2 = (q1.1 + q2.0)0*

    q2 = q1.10*

  - Substitute q2 in the equations for q1 and q3:

    q1 = q1.0 + q1.10*

    q3 = q1.10*.1 + q3.0 + q3.1

  - Solve for q1 and q3 using Arden's theorem:

    q1 = (q1.0 + q1.10*)0*

    q1 = 0* + 0*10*

    q1 = (0 + 10)*

    q3 = (q1.10*.1 + q3.0 + q3.1)0*

    q3 = (0 + 10)*10*.10* + (q3.0 + q3.1)0*

    q3 = (0 + 10)*10*.10* + (q3.0 + q3.1)0*0*

    q3 = (0 + 10)*10*.10* + q3(0 + 1)0*

    q3 = (0 + 10)*10*.10*(0 + 1)0*

  - The regular expression for the language accepted by the finite automaton is the union of the regular expressions for the final states:

    L = q1 + q3

    L = (0 + 10)* + (0 + 10)*10*.10*(0 + 1)0*