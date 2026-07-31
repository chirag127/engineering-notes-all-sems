### Baum-Welch Parameter Re-Estimation

- Baum-Welch is an algorithm that uses the Expectation-Maximization (EM) method to find the maximum likelihood estimate of the parameters of a Hidden Markov Model (HMM) given a set of observed feature vectors.
- The algorithm iteratively updates the parameters of the HMM until convergence or a predefined number of iterations is reached.
- The algorithm consists of two main steps: the forward-backward procedure and the re-estimation formulae.
- The forward-backward procedure computes the probabilities of being in each state at each time step, given the observed feature vectors and the current parameters of the HMM. These probabilities are called the forward and backward variables, denoted by $\alpha_t(i)$ and $\beta_t(i)$, respectively.
- The re-estimation formulae use the forward and backward variables to compute the expected number of transitions and emissions for each state and symbol, given the observed feature vectors and the current parameters of the HMM. These expected counts are then used to update the parameters of the HMM, such as the initial state probabilities, the transition probabilities, and the emission probabilities.
- The algorithm can be summarized as follows:

  - For every parameter vector/matrix requiring re-estimation, allocate storage for the numerator and denominator accumulators.
  - For each training sequence, perform the following steps:
    - Run the forward-backward procedure to compute the forward and backward variables for the sequence.
    - For each parameter vector/matrix, use the re-estimation formulae to update the numerator and denominator accumulators, based on the forward and backward variables and the current parameter values.
  - For each parameter vector/matrix, divide the numerator accumulator by the denominator accumulator to obtain the new parameter value.
  - Repeat the above steps until convergence or a predefined number of iterations is reached.

- The algorithm can be applied to different types of HMMs, such as discrete, continuous, or mixture HMMs, by using different re-estimation formulae for the emission probabilities.
- The algorithm is also known as the Forward-Backward algorithm or the EM algorithm for HMMs.
- The algorithm is named after Leonard E. Baum and Lloyd R. Welch, who derived the re-estimation formulae for discrete HMMs in 1970.