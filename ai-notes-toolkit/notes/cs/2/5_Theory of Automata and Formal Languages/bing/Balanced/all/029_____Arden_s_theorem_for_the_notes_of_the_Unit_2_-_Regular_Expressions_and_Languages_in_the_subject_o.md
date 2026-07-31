# Arden's Theorem for the notes of the Unit 2 - Regular Expressions and Languages in the subject of Theory of Automata and Formal Languages

- Arden's Theorem is a mathematical statement that helps to find the regular expression equivalent to a given finite automaton  .
- Arden's Theorem states that, if P and Q are two regular expressions over an alphabet , and if P does not contain the empty string , then the following equation in R given by R = Q + RP has a unique solution, that is, R = QP*  .
- The proof of Arden's Theorem is based on the following steps:
  - Show that R = QP* is a solution of R = Q + RP by substituting R = QP* in the equation and simplifying it.
  - Show that R = QP* is the only solution of R = Q + RP by assuming that there is another solution S and deriving a contradiction.
- Arden's Theorem can be used to find the regular expression of a finite automaton by following these steps :
  - Convert the finite automaton into a system of equations, where each equation corresponds to a state and has the form R = Q + RP, where R is the regular expression for the language accepted by that state, Q is the regular expression for the transitions from that state to itself, and P is the regular expression for the transitions from that state to other states.
  - Solve the system of equations using Arden's Theorem, starting from the final states and moving backwards to the initial state.
  - The regular expression for the language accepted by the finite automaton is the regular expression for the initial state.
- An example of using Arden's Theorem to find the regular expression of a finite automaton is given below:

![Finite automaton](https://media.geeksforgeeks.org/wp-content/uploads/20210920101130/ardens-theorem-1.png)

The system of equations for this finite automaton is:

q1 = q1.0 + q2.1

q2 = q1.1 + q2.0 + q3.0

q3 = q2.1 + q3.0 + q3.1

Using Arden's Theorem, we can solve the equations as follows:

q3 = (q2.1 + q3.0 + q3.1)*

q2 = (q1.1 + q2.0 + q3.0)*

q1 = q1.0 + q2.1

q1 = (q1.0 + q2.1)*

q1 = (0 + (q1.1 + q2.0 + q3.0)*.1)*

q1 = (0 + (0 + (q1.1 + q2.0 + q3.0)*.1)*.1 + (q2.1 + q3.0 + q3.1)*.0)*

q1 = (0 + 1(0 + 1)*.1 + (1(0 + 1)*.1 + 0 + 1)*.0)*

The regular expression for the language accepted by the finite automaton is q1, which is:

(0 + 1(0 + 1)*.1 + (1(0 + 1)*.1 + 0 + 1)*.0)*