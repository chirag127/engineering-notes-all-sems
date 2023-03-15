 Here is the content in markdown format:

### A Probabilistic Theory of Deep Learning for the notes of the Unit 2 - DEEP NETWORKS in the subject of Deep Learning

- Deep Learning models are probabilistic graphical models i.e. they specify a joint probability distribution over the inputs and outputs.
- The layers of a deep network define a hierarchical factorization of this joint distribution.
- The parameters of the network represent the conditional probabilities in this factorization.
- Training the network is equivalent to adjusting these parameters to match the observed data.
- Viewing deep networks as probabilistic models provides insight into issues like overfitting, and suggests principled regularization techniques.

Advantages:
- Provides a unifying view of deep networks and connects them to a large body of work on probabilistic models.
- Suggests new regularization techniques based on Bayesian methods.
- Highlights the possibility of "black-box" inference and learning in deep probabilistic models.

Disadvantages:
- The probabilistic view makes strong assumptions about the functional forms and independence structures.
- Scales poorly with the depth of the network due to "posteriors collapse".
- Training can be slower than standard techniques.

Examples:
- Classification: Predicting the class of an input based on the posterior distribution over classes.
- Regression: Predicting the mean of a target distribution conditioned on the input.
- Generative Models: Sampling from the joint distribution to generate new inputs.

Applications:
- Computer Vision: Object recognition, semantic segmentation, depth estimation, etc.
- Natural Language Processing: Machine translation, syntactic parsing, sentiment analysis, etc.
- Robotics: Planning and control, imitation learning, etc.
- Recommendation Systems
- Medical Diagnosis
- And many more!