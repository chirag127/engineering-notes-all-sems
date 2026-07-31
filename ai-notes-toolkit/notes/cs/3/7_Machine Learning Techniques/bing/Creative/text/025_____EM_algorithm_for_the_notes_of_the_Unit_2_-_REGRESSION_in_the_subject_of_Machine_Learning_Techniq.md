### EM algorithm

The EM (Expectation-Maximization) algorithm is one of the most commonly used terms in machine learning to obtain maximum likelihood estimates of variables that are sometimes observable and sometimes not. However, it is also applicable to unobserved data or sometimes called latent.

The EM algorithm is the combination of various unsupervised ML algorithms, such as the k-means clustering algorithm. Being an iterative approach, it consists of two modes. In the first mode, we estimate the missing or latent variables. Hence it is referred to as the Expectation/estimation step (E-step). In the second mode, we optimize the parameters of the model to best explain the data. Hence it is referred to as the Maximization step (M-step) .

The EM algorithm is used to find (local) maximum likelihood parameters of a statistical model in cases where the equations cannot be solved directly. Typically these models involve latent variables in addition to unknown parameters and known data observations.

The EM algorithm (and its faster variant ordered subset expectation maximization) is also widely used in medical image reconstruction, especially in positron emission tomography, single-photon emission computed tomography, and x-ray computed tomography.

The EM algorithm can be summarized as follows :

- Initialize the parameters of the model, usually randomly.
- Repeat until convergence:
  - E-step: Estimate the latent variables given the current parameters and the observed data.
  - M-step: Update the parameters given the current latent variables and the observed data.
- Return the final parameters and the latent variables.

The EM algorithm is guaranteed to increase the likelihood function at each iteration, and converges to a local optimum. The convergence rate depends on the initialization and the complexity of the model.

Some examples of applications of the EM algorithm are:

- Gaussian mixture models: The latent variables are the cluster assignments of each data point, and the parameters are the means, variances, and weights of each cluster.
- Hidden Markov models: The latent variables are the hidden states of the Markov chain, and the parameters are the transition and emission probabilities of each state.
- Latent Dirichlet allocation: The latent variables are the topic assignments of each word in a document, and the parameters are the topic distributions of each document and the word distributions of each topic.