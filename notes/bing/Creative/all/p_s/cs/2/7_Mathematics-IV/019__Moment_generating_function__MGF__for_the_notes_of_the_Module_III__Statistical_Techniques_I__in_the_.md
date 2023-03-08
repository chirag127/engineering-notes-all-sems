### Moment generating function (MGF)

- A moment generating function (MGF) is a function that can be used to characterize the distribution of a random variable.
- The MGF of a random variable X is defined as M(t) = E(e^tX), where t is any real number and E is the expected value operator.
- The MGF exists if there is a positive constant c such that M(t) is finite for all |t| < c.
- The MGF has the following properties:
  - M(0) = 1, since E(e^0X) = E(1) = 1.
  - The coefficient of t^n/n! in the Taylor expansion of M(t) around t = 0 is the nth moment of X, i.e., M^(n)(0) = E(X^n), where M^(n) denotes the nth derivative of M.
  - The MGF is unique, meaning that if two random variables have the same MGF, then they have the same distribution.
  - The MGF of a linear transformation of X is M(at + b) = e^bt M(a), where a and b are constants.
  - The MGF of a sum of independent random variables is the product of their MGFs, i.e., if X and Y are independent, then M_X+Y(t) = M_X(t) M_Y(t).
- The MGF can be used to find the distribution, moments, and other properties of a random variable, as well as to prove some theorems and inequalities in probability theory.

Some possible mnemonics and learning tricks for the topic are:

- To remember the definition of MGF, think of M as "mean" and G as "growth". The MGF is the mean growth rate of e^tX as t changes.
- To remember the property of MGF of a linear transformation, think of M as "move" and G as "grow". The MGF moves by b and grows by a when X is transformed by at + b.
- To remember the property of MGF of a sum of independent random variables, think of M as "multiply" and G as "generate". The MGF multiplies the MGFs of the individual random variables to generate the MGF of the sum.