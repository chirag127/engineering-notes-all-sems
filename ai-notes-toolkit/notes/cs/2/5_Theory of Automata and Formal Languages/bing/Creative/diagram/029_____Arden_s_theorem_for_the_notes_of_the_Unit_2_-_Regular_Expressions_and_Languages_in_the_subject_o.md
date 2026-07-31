### Arden's theorem

- Arden's theorem is a mathematical statement that relates regular expressions and languages.
- Arden's theorem can be used to find a regular expression that represents the language accepted by a finite automaton.
- Arden's theorem states that if P and Q are two regular expressions over an alphabet Σ, and if P does not contain the empty string ε, then the following equation in R has a unique solution:

  R = Q + RP

  The solution is:

  R = QP*

- The proof of Arden's theorem is based on the following steps:

  - Assume that R is a solution of the equation R = Q + RP.
  - Show that R ⊆ QP* by using induction on the length of strings in R.
  - Show that QP* ⊆ R by using the closure properties of regular languages.
  - Conclude that R = QP* by the double inclusion principle.

- An example of applying Arden's theorem to find a regular expression for a finite automaton is given below:

  ![Finite automaton](https://www.geeksforgeeks.org/wp-content/uploads/FA-1.png)

  The equations for the states are:

  q0 = q0a + q1b + ε

  q1 = q0a + q2b

  q2 = q2a + q2b

  To find the regular expression for the language accepted by the automaton, we need to solve for q0, since it is the initial and final state. We can use Arden's theorem to eliminate q1 and q2 from the equations as follows:

  q1 = q0a + q2b

  q1 = (q0a + q2b)a*

  q1 = (q0 + q2b)a*

  q2 = q2(a + b)

  q2 = (a + b)*

  q1 = (q0 + (a + b)*b)a*

  q0 = q0a + q1b + ε

  q0 = q0a + (q0 + (a + b)*b)a*b + ε

  q0 = (q0 + (a + b)*b)a*b + ε

  q0 = ε + (q0 + (a + b)*b)a*b

  q0 = (q0 + (a + b)*b)a*b*

  q0 = ((a + b)*b)a*b*

  Therefore, the regular expression for the language accepted by the automaton is ((a + b)*b)a*b*.