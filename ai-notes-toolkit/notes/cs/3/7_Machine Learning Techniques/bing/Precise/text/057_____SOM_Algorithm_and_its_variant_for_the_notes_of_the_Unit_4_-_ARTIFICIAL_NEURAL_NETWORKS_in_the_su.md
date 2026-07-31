### SOM Algorithm and its variant for the notes of the Unit 4 - ARTIFICIAL NEURAL NETWORKS in the subject of Machine Learning Techniques

- SOM (Self-Organizing Map) is an unsupervised learning algorithm that is used for data visualization, dimensionality reduction, and clustering.
- SOM is a type of artificial neural network that is trained using competitive learning.
- The algorithm maps high-dimensional data onto a low-dimensional grid of neurons, usually two-dimensional.
- Each neuron in the grid is associated with a weight vector of the same dimension as the input data.
- During training, the algorithm iteratively adjusts the weight vectors of the neurons to better represent the input data.
- The SOM algorithm consists of the following steps:
  1. Initialization: The weight vectors of the neurons are initialized, usually with small random values.
  2. Competition: For each input vector, the neuron with the weight vector closest to the input vector is determined. This neuron is called the Best Matching Unit (BMU).
  3. Cooperation: The weight vectors of the neurons in the neighborhood of the BMU are adjusted to be closer to the input vector. The size of the neighborhood decreases over time.
  4. Adaptation: The weight vectors of the neurons are updated according to a learning rule.
  5. Repeat steps 2-4 until convergence or a stopping criterion is met.
- A common variant of the SOM algorithm is the Growing Self-Organizing Map (GSOM), which dynamically adds neurons to the grid during training to better represent the input data.
- Another variant is the Neural Gas algorithm, which uses a similar competitive learning rule but does not impose a grid structure on the neurons.