### Baum-Welch Parameter Re-Estimation

- Baum-Welch is an algorithm that uses the Expectation-Maximization (EM) method to find the maximum likelihood estimate of the parameters of a hidden Markov model (HMM) given a set of observed feature vectors.
- The algorithm iteratively updates the parameters of the HMM until convergence or a predefined number of iterations is reached.
- The algorithm consists of two main steps: the forward-backward procedure and the re-estimation formulae.
- The forward-backward procedure computes the posterior probabilities of the hidden states given the observations using dynamic programming. These probabilities are denoted by $\alpha_t(i)$ and $\beta_t(i)$, where $t$ is the time index and $i$ is the state index.
- The re-estimation formulae update the parameters of the HMM using the posterior probabilities computed by the forward-backward procedure. The parameters include the initial state probabilities $\pi_i$, the state transition probabilities $a_{ij}$, and the emission probabilities $b_i(o_t)$, where $o_t$ is the observation at time $t$.
- The re-estimation formulae are derived by applying the principle of maximum likelihood, which maximizes the log-likelihood function of the HMM given the observations. The log-likelihood function is given by
$$
\log P(O|\lambda) = \sum_{t=1}^T \log \sum_{i=1}^N \alpha_t(i) \beta_t(i)
$$
where $O$ is the observation sequence, $\lambda$ is the parameter set of the HMM, $T$ is the length of the sequence, and $N$ is the number of states.
- The re-estimation formulae for the parameters are given by
$$
\hat{\pi}_i = \frac{\alpha_1(i) \beta_1(i)}{\sum_{j=1}^N \alpha_1(j) \beta_1(j)}
$$
$$
\hat{a}_{ij} = \frac{\sum_{t=1}^{T-1} \alpha_t(i) a_{ij} b_j(o_{t+1}) \beta_{t+1}(j)}{\sum_{t=1}^{T-1} \alpha_t(i) \beta_t(i)}
$$
$$
\hat{b}_i(o_t) = \frac{\sum_{t=1}^T \alpha_t(i) \beta_t(i) \delta(o_t, v_k)}{\sum_{t=1}^T \alpha_t(i) \beta_t(i)}
$$
where $v_k$ is the $k$-th symbol in the observation alphabet, and $\delta(o_t, v_k)$ is the Kronecker delta function, which is 1 if $o_t = v_k$ and 0 otherwise.
- The algorithm can be summarized as follows :
  - For every parameter vector/matrix requiring re-estimation, allocate storage for the numerator and denominator accumulators.
  - Set all accumulators to zero.
  - For each observation sequence in the training set, do the following:
    - Perform the forward-backward procedure to compute the posterior probabilities of the hidden states.
    - For each parameter vector/matrix, use the re-estimation formulae to update the corresponding accumulators.
  - For each parameter vector/matrix, divide the numerator accumulator by the denominator accumulator to obtain the new estimate.
  - Repeat the above steps until convergence or a predefined number of iterations is reached.