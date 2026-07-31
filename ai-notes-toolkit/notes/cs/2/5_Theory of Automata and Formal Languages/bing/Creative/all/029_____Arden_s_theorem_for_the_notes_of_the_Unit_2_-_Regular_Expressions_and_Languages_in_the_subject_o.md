# Arden's Theorem for the notes of the Unit 2 - Regular Expressions and Languages in the subject of Theory of Automata and Formal Languages

- Arden's Theorem is a mathematical statement that is used to find out a regular expression that represents the language accepted by a finite automaton  .
- Arden's Theorem states that, if P and Q are two regular expressions over an alphabet , and if P does not contain the empty string , then the following equation in R given by R = Q + RP has a unique solution; R = QP*  .
- The proof of Arden's Theorem is based on the following steps:
  - Show that R = QP* is a solution of R = Q + RP by substituting R = QP* in the equation and simplifying it.
  - Show that R = QP* is the only solution of R = Q + RP by assuming that there is another solution S and deriving a contradiction.
- Arden's Theorem can be applied to convert a finite automaton into a regular expression by following these steps  :
  - Construct a system of equations for each state of the finite automaton, where the equation for a state q is of the form q = Q + RP, where Q is the set of symbols that lead to a final state from q, and R is the set of symbols that lead to another state from q.
  - Solve the system of equations using Arden's Theorem, starting from the final states and moving backwards to the initial state.
  - The solution for the initial state is the regular expression that represents the language accepted by the finite automaton.
- An example of applying Arden's Theorem to convert a finite automaton into a regular expression is given below:

![Finite automaton](https://media.geeksforgeeks.org/wp-content/uploads/20210920152754/ardens-theorem-1.png)

- The system of equations for this finite automaton is:

q1 = q1.0 + q2.1 + q2.0

q2 = q1.1 + q2.0 + q3.0 + q3.1

q3 = q2.1 + q3.0 + q3.1

- Solving the system of equations using Arden's Theorem, we get:

q3 = (q2.1 + q3.0 + q3.1)*

q2 = (q1.1 + q2.0 + q3.0 + q3.1)*

q1 = (q1.0 + q2.1 + q2.0)*

q1 = (q1.0 + (q1.1 + q2.0 + q3.0 + q3.1)*.1 + (q1.1 + q2.0 + q3.0 + q3.1)*.0)*

q1 = (q1.0 + (q1.1 + q2.0 + (q2.1 + q3.0 + q3.1)*.0 + (q2.1 + q3.0 + q3.1)*.1)*.1 + (q1.1 + q2.0 + (q2.1 + q3.0 + q3.1)*.0 + (q2.1 + q3.0 + q3.1)*.1)*.0)*

q1 = (q1.0 + (q1.1 + q2.0 + (q2.1 + q3.0 + q3.1)*.0 + (q2.1 + q3.0 + q3.1)*.1)*.1 + (q1.1 + q2.0 + (q2.1 + q3.0 + q3.1)*.0 + (q2.1 + q3.0 + q3.1)*.1)*.0)*

q1 = (q1.0 + (q1.1 + q2.0 + (q2.1 + (q2.1 + q3.0 + q3.1)*.0 + (q2.1 + q3.0 + q3.1)*.1)*.0 + (q2.