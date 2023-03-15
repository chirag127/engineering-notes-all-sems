# Algebraic Method Using Arden’s Theorem

Arden’s Theorem is used to find the regular expression of a Finite Automaton. The theorem states that if P and Q are two regular expressions over an alphabet Σ, and if P does not contain the null string, then the equation R = Q + RP has a unique solution, which is R = QP*  .

## Proof of Arden’s Theorem

Let us consider the equation R = Q + RP. Substituting the value of R in the equation, we get R = Q + (Q + RP)P. This can be further simplified as R = Q + QP + RPP. Since P*P = P*, we can write the equation as R = Q + QP + RP*. Replacing R with QP* in the equation, we get R = Q + QP + QP*P*. Since P*P = P*, the equation can be simplified as R = Q + QP + QP*. This can be further simplified as R = Q + QP*. Hence, the unique solution to the equation R = Q + RP is R = QP* .

## Application of Arden’s Theorem

Arden’s Theorem can be used to find the regular expression for a given Finite Automaton. To do this, we need to write the equations for the final state of the Finite Automaton using the transitions. Then, we can apply Arden’s Theorem to solve the equations and find the regular expression .

For example, consider the following Finite Automaton:

[Insert image of Finite Automaton here]

The equations for the final state q2 can be written as follows:

q2 = q0b + q1b + q2b

Since the equation is in the form of R = Q + RP, we can apply Arden’s Theorem to find the regular expression. The unique solution to the equation is q2 = (q0 + q1) b*.

Hence, the regular expression for the given Finite Automaton is (q0 + q1) b*.