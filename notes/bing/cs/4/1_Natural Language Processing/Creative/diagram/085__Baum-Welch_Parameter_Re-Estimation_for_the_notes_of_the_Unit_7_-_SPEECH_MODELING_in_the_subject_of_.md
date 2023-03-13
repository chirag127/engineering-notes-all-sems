The Baum-Welch parameter re-estimation is a method to find the optimal parameters of a hidden Markov model (HMM) given a set of observed feature vectors. It is based on the expectation-maximization (EM) algorithm, which iteratively updates the parameters until convergence. The basic steps of the Baum-Welch algorithm are:

1. Initialize the parameters of the HMM, such as the initial state probabilities, the transition probabilities, and the emission probabilities.
2. Compute the forward and backward probabilities for each state and each observation using the current parameters. These probabilities represent the likelihood of being in a state at a time given the observations and the parameters.
3. Compute the expected number of transitions from state i to state j, and the expected number of observations from state i, using the forward and backward probabilities. These are called the sufficient statistics for the parameters.
4. Re-estimate the parameters using the sufficient statistics and the Baum-Welch formulae, which are derived from the maximum likelihood principle. The formulae are different for discrete and continuous HMMs, but they have the same general form of dividing the expected counts by the total counts.
5. Repeat steps 2 to 4 until the parameters converge or a stopping criterion is met.

The following diagram illustrates the basic architecture of a discrete HMM and the computation of the forward and backward probabilities:

```
    +---+     +---+     +---+     +---+     +---+
    | S | --> | S | --> | S | --> | S | --> | S |
    +---+     +---+     +---+     +---+     +---+
      |         |         |         |         |
      |         |         |         |         |
      v         v         v         v         v
    +---+     +---+     +---+     +---+     +---+
    | O |     | O |     | O |     | O |     | O |
    +---+     +---+     +---+     +---+     +---+
      |         |         |         |         |
      |         |         |         |         |
      v         v         v         v         v
    +---+     +---+     +---+     +---+     +---+
    | X |     | X |     | X |     | X |     | X |
    +---+     +---+     +---+     +---+     +---+

S: state
O: observation
X: feature vector

Forward probability: alpha(i, t) = P(X1, X2, ..., Xt, S_t = i | parameters)
Backward probability: beta(i, t) = P(X_t+1, X_t+2, ..., XT | S_t = i, parameters)
```