### Baum-Welch Parameter Re-Estimation

- Baum-Welch is an algorithm that uses the Expectation-Maximization (EM) method to find the maximum likelihood estimate of the parameters of a Hidden Markov Model (HMM) given a set of observed feature vectors.
- The algorithm iteratively updates the parameters of the HMM until convergence or a predefined number of iterations is reached.
- The algorithm consists of two main steps: the forward-backward procedure and the re-estimation formulae.
- The forward-backward procedure computes the posterior probabilities of the hidden states given the observations using dynamic programming. These probabilities are also called the forward and backward variables, denoted by $\alpha_t(i)$ and $\beta_t(i)$, respectively.
- The re-estimation formulae update the parameters of the HMM using the forward and backward variables and the observed feature vectors. The parameters include the initial state probabilities $\pi_i$, the state transition probabilities $a_{ij}$, and the emission probabilities $b_j(k)$.
- The re-estimation formulae are derived by applying the principle of maximum likelihood and using the Lagrange multipliers to enforce the constraints on the probabilities.
- The re-estimation formulae are as follows :

$$\hat{\pi}_i = \frac{\alpha_1(i)\beta_1(i)}{\sum_{j=1}^N \alpha_1(j)\beta_1(j)}$$

$$\hat{a}_{ij} = \frac{\sum_{t=1}^{T-1} \alpha_t(i) a_{ij} b_j(x_{t+1}) \beta_{t+1}(j)}{\sum_{t=1}^{T-1} \alpha_t(i) \beta_t(i)}$$

$$\hat{b}_j(k) = \frac{\sum_{t=1}^T \alpha_t(j) \beta_t(j) \delta(x_t, k)}{\sum_{t=1}^T \alpha_t(j) \beta_t(j)}$$

where $\delta(x_t, k)$ is 1 if $x_t = k$ and 0 otherwise.

- The algorithm starts with an initial guess of the parameters and repeats the following steps until convergence or a predefined number of iterations is reached :

  - Step 1: For each observation sequence, compute the forward and backward variables using the current parameters.
  - Step 2: For each parameter, compute the re-estimation using the forward and backward variables and the observation sequences.
  - Step 3: Replace the current parameters with the re-estimated ones.

- The algorithm is guaranteed to increase the likelihood of the observation sequences at each iteration, and converges to a local maximum of the likelihood function.
- The algorithm can be applied to discrete or continuous HMMs, depending on the type of the emission probabilities.