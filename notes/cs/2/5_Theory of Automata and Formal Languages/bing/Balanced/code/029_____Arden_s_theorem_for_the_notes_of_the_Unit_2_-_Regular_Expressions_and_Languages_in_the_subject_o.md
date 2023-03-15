# Arden's Theorem for the notes of the Unit 2 - Regular Expressions and Languages in the subject of Theory of Automata and Formal Languages

- Arden's Theorem is a mathematical statement that relates regular expressions and finite automata.
- Arden's Theorem can be used to find a regular expression that represents the language accepted by a finite automaton, or to find a finite automaton that accepts a language represented by a regular expression.
- Arden's Theorem states that if P and Q are two regular expressions over an alphabet , and if P does not contain the empty string , then the following equation in R has a unique solution:

  R = Q + RP

  The solution is:

  R = QP*

- The proof of Arden's Theorem is based on the following observations:

  - If R is a solution of the equation, then R must contain all the strings in Q, and all the strings that can be obtained by concatenating a string in Q with a string in P, and so on. This is equivalent to saying that R contains QP*.
  - If R contains QP*, then R is a solution of the equation, because QP* = Q + QP*P, and P*P = P*.
  - Therefore, QP* is the unique solution of the equation.

- To apply Arden's Theorem to find a regular expression for a finite automaton, we can follow these steps:

  - Assign a variable to each state of the finite automaton, such as Q1, Q2, Q3, etc.
  - Write an equation for each variable, based on the transitions of the finite automaton. For example, if Q1 has transitions to Q2 on input 0 and to Q3 on input 1, then the equation for Q1 is:

    Q1 = Q2.0 + Q3.1

  - If a state is a final state, then add the empty string to its equation. For example, if Q3 is a final state, then the equation for Q3 is:

    Q3 = Q2.1 + Q3.0 + Q3.1 + 

  - Solve the system of equations using Arden's Theorem, starting from the final states and moving backwards. For example, to solve the equation for Q3, we can use Arden's Theorem to get:

    Q3 = (Q2.1 + Q3.0 + Q3.1)*

  - Substitute the solutions of the variables into the equations of the other variables, until we get the solution for the initial state. For example, to solve the equation for Q1, we can substitute the solution of Q3 into the equation of Q1 and get:

    Q1 = Q2.0 + (Q2.1 + Q3.0 + Q3.1)*.1

  - The solution for the initial state is the regular expression that represents the language accepted by the finite automaton. For example, the regular expression for Q1 is:

    Q1 = Q2.0 + (Q2.1 + Q3.0 + Q3.1)*.1

- To apply Arden's Theorem to find a finite automaton for a regular expression, we can follow these steps:

  - Write the regular expression in the form of an equation, such as R = Q + RP, where Q and P are simpler regular expressions.
  - Construct a finite automaton with two states, Q and R, and transitions according to the equation. For example, if the equation is R = Q + RP, then the finite automaton has transitions from Q to R on input P, and from R to R on input P, and a self-loop on Q on input Q.
  - Make Q the initial state and R the final state of the finite automaton.
  - Simplify the finite automaton by eliminating redundant states and transitions, and by applying the rules of regular expressions. For example, if Q and P are both , then the finite automaton can be reduced to a single state R with a self-loop on input .