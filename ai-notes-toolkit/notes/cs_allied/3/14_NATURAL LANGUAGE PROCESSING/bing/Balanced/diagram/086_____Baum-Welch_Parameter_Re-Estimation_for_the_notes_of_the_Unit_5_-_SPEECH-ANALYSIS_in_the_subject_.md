### Baum-Welch Parameter Re-Estimation

- Baum-Welch is an algorithm that uses the Expectation-Maximization (EM) method to find the maximum likelihood estimate of the parameters of a Hidden Markov Model (HMM) given a set of observed feature vectors.
- The algorithm iteratively updates the parameters of the HMM until convergence or a predefined number of iterations is reached.
- The algorithm consists of two main steps: the forward-backward procedure and the re-estimation formulae.
- The forward-backward procedure computes the posterior probabilities of the hidden states given the observations using dynamic programming. These probabilities are also called the forward and backward variables, denoted by $\alpha_t(i)$ and $\beta_t(i)$, respectively.
- The re-estimation formulae use the forward and backward variables to compute the expected counts of the state transitions and the state emissions, denoted by $\xi_t(i,j)$ and $\gamma_t(i)$, respectively. These expected counts are then used to update the parameters of the HMM, namely the initial state distribution $\pi$, the state transition matrix $A$, and the state emission matrix $B$.
- The re-estimation formulae are derived by applying the principle of maximum likelihood and using the Lagrange multipliers to enforce the constraints on the parameters.
- The re-estimation formulae are as follows:

$$
\pi_i = \frac{\gamma_1(i)}{N}
$$

$$
A_{ij} = \frac{\sum_{t=1}^{T-1} \xi_t(i,j)}{\sum_{t=1}^{T-1} \gamma_t(i)}
$$

$$
B_{ij} = \frac{\sum_{t=1}^T \gamma_t(i) \delta(O_t, v_j)}{\sum_{t=1}^T \gamma_t(i)}
$$

where $N$ is the number of observation sequences, $T$ is the length of each sequence, $O_t$ is the observation at time $t$, $v_j$ is the $j$-th symbol in the observation alphabet, and $\delta(x,y)$ is the Kronecker delta function that equals 1 if $x=y$ and 0 otherwise.