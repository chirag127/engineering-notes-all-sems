### Baum-Welch Parameter Re-Estimation

- Baum-Welch is an algorithm that uses the Expectation-Maximization (EM) method to find the maximum likelihood estimate of the parameters of a Hidden Markov Model (HMM) given a set of observed feature vectors.
- The algorithm iteratively updates the parameters of the HMM until convergence or a predefined number of iterations is reached.
- The algorithm consists of two main steps: the forward-backward procedure and the re-estimation formulae.
- The forward-backward procedure computes the posterior probabilities of the hidden states given the observations using dynamic programming. These probabilities are denoted by $\alpha_t(i)$ and $\beta_t(i)$, where $t$ is the time index and $i$ is the state index.
- The re-estimation formulae update the parameters of the HMM using the posterior probabilities computed by the forward-backward procedure. The parameters include the initial state probabilities $\pi_i$, the state transition probabilities $a_{ij}$, and the emission probabilities $b_i(o_t)$, where $o_t$ is the observation at time $t$.
- The re-estimation formulae are derived by applying the principle of maximum likelihood, which states that the parameters should maximize the probability of the observations given the model.
- The re-estimation formulae are as follows :

$$\hat{\pi}_i = \frac{\gamma_1(i)}{N}$$

$$\hat{a}_{ij} = \frac{\sum_{t=1}^{T-1}\xi_t(i,j)}{\sum_{t=1}^{T-1}\gamma_t(i)}$$

$$\hat{b}_i(o_t) = \frac{\sum_{t=1}^{T}\gamma_t(i) \delta(o_t,v_k)}{\sum_{t=1}^{T}\gamma_t(i)}$$

where $N$ is the number of observation sequences, $\gamma_t(i)$ is the probability of being in state $i$ at time $t$, $\xi_t(i,j)$ is the probability of being in state $i$ at time $t$ and state $j$ at time $t+1$, $\delta(o_t,v_k)$ is 1 if $o_t = v_k$ and 0 otherwise, and $v_k$ is the $k$-th symbol in the observation alphabet.
- The algorithm can be summarized as follows:

  - For every parameter vector/matrix requiring re-estimation, allocate storage for the numerator and denominator accumulators.
  - For each observation sequence in the training set, do the following:
    - Run the forward-backward procedure to compute the posterior probabilities $\alpha_t(i)$ and $\beta_t(i)$.
    - For each parameter vector/matrix, update the numerator and denominator accumulators using the re-estimation formulae.
  - For each parameter vector/matrix, divide the numerator accumulator by the denominator accumulator to obtain the new estimate.
  - Repeat the above steps until convergence or a predefined number of iterations is reached.