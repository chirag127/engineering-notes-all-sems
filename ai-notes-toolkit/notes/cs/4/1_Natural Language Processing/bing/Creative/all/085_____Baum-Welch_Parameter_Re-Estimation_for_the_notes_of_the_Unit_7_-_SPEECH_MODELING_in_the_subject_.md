# Baum-Welch Parameter Re-Estimation

- Baum-Welch is an algorithm that uses the Expectation-Maximization (EM) method to find the maximum likelihood estimate of the parameters of a hidden Markov model (HMM) given a set of observed feature vectors.
- The algorithm iteratively updates the parameters of the HMM until convergence or a predefined number of iterations is reached.
- The algorithm consists of two main steps: the forward-backward procedure and the re-estimation formulae.
- The forward-backward procedure computes the posterior probabilities of the hidden states given the observations using dynamic programming. These probabilities are also called the forward and backward variables, denoted by $\alpha_t(i)$ and $\beta_t(i)$, respectively, where $t$ is the time index and $i$ is the state index.
- The re-estimation formulae use the forward and backward variables to compute the expected counts of the state transitions and the state emissions, denoted by $\xi_t(i,j)$ and $\gamma_t(i)$, respectively, where $j$ is another state index.
- The expected counts are then used to update the parameters of the HMM, namely the initial state probabilities $\pi_i$, the state transition probabilities $a_{ij}$, and the state emission probabilities $b_i(o_t)$, where $o_t$ is the observation at time $t$.
- The re-estimation formulae are derived by applying the principle of maximum likelihood and using the Lagrange multipliers to enforce the constraints on the probabilities.
- The re-estimation formulae are as follows :

$$
\pi_i = \frac{\gamma_1(i)}{N}
$$

$$
a_{ij} = \frac{\sum_{t=1}^{T-1} \xi_t(i,j)}{\sum_{t=1}^{T-1} \gamma_t(i)}
$$

$$
b_i(o_t) = \frac{\sum_{t=1}^T \gamma_t(i) \delta(o_t, v_k)}{\sum_{t=1}^T \gamma_t(i)}
$$

where $N$ is the number of observation sequences, $T$ is the length of each sequence, $v_k$ is the $k$-th symbol in the observation alphabet, and $\delta(o_t, v_k)$ is the Kronecker delta function that equals 1 if $o_t = v_k$ and 0 otherwise.

- The algorithm can be summarized as follows:

  - Initialize the parameters of the HMM randomly or with some prior knowledge.
  - Repeat until convergence or a predefined number of iterations:
    - For each observation sequence, perform the forward-backward procedure to compute the forward and backward variables.
    - For each observation sequence, use the forward and backward variables to compute the expected counts of the state transitions and the state emissions.
    - Use the expected counts to update the parameters of the HMM using the re-estimation formulae.
    - Evaluate the log-likelihood of the observation sequences given the updated parameters and check for convergence.