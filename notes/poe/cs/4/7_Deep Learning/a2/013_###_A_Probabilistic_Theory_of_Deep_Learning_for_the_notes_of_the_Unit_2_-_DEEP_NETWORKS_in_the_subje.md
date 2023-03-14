 Here is the content in markdown format:

### A Probabilistic Theory of Deep Learning for the notes of the Unit 2 - DEEP NETWORKS in the subject of Deep Learning

- Deep Learning models are opaque, black-box models. A probabilistic approach provides insight into why they work and how they can be improved.
- A probabilistic model assumes all variables are random and associated with a probability distribution. We can infer the distribution of hidden variables from observed variables.
- In deep networks, we can view the activations as probabilities of the data given the parameters. The loss function measures how poorly the model fits the data distribution. Training increases the likelihood of the data, improving the fit.
- Viewing deep networks as probabilistic models gives insights:
-- Overfitting occurs when the model fits the noise in the training data, not the true data distribution. Regularization decreases the flexibility of the model, focusing on the true distribution.
-- Bayesian methods can incorporate prior beliefs about appropriate parameter values. This often leads to better generalization.
-- Generative models can generate new data instances from the learned distribution. Sampling can generate artificial data for training or applications like image generation.

MNEMONICS:
- "Deep in probability" - A probabilistic view provides insight into deep networks
- "Noise killer regularizer" - Regularization reduces overfitting to noise
- "Belief in parameters" - Bayesian methods use prior beliefs to generalize better
- "Generate data, don't wait" - Sampling can generate new data from the learned distribution

ADVANTAGES: Probabilistic insight; overfitting reduction; Bayesian methods; data generation

DISADVANTAGES: Increased complexity; choosing appropriate distributions and priors is difficult;

EXAMPLES: Autoencoders; GANs; Bayesian neural networks

APPLICATIONS: Generative models; semi-supervised learning; reinforcement learning; medical diagnosis