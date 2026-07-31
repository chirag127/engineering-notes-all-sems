# SOM Algorithm and its variant

- SOM stands for Self-Organizing Map, which is a type of artificial neural network that performs unsupervised learning and dimensionality reduction  .
- SOM consists of two layers: an input layer and an output layer. The input layer receives high-dimensional data, and the output layer consists of a grid of nodes, each with a weight vector of the same dimension as the input data .
- The SOM algorithm works as follows :
  - Initialize the weight vectors of the output nodes randomly or using some heuristic.
  - Select an input vector randomly from the data set and present it to the input layer.
  - Find the output node that is most similar to the input vector, based on some distance measure. This node is called the best matching unit (BMU) or the winner node.
  - Update the weight vectors of the output nodes within a certain neighborhood of the BMU, such that they become more similar to the input vector. The size of the neighborhood and the amount of update decrease over time, according to some learning rate and neighborhood function.
  - Repeat steps 2-4 until a stopping criterion is met, such as a fixed number of iterations or a convergence threshold.
- The SOM algorithm can be interpreted as a way of creating a low-dimensional representation of the input data that preserves the topological structure and the statistical distribution of the data . The output nodes form clusters that correspond to different regions or patterns in the input space .
- A variant of the SOM algorithm is the SOM-based optimization (SOMO) algorithm, which was proposed by Su and Zhao   . The SOMO algorithm is motivated by applying the SOM algorithm to continuous optimization problems, where the goal is to find the optimal solution to a given objective function .
- The SOMO algorithm works as follows :
  - Initialize the weight vectors of the output nodes randomly or using some heuristic, within the feasible region of the optimization problem.
  - Select an input vector randomly from the data set and present it to the input layer.
  - Find the output node that has the smallest objective function value among all the output nodes. This node is called the best objective node (BON) or the winner node.
  - Update the weight vectors of the output nodes within a certain neighborhood of the BON, such that they move towards the BON. The size of the neighborhood and the amount of update decrease over time, according to some learning rate and neighborhood function.
  - Repeat steps 2-4 until a stopping criterion is met, such as a fixed number of iterations or a convergence threshold.
- The SOMO algorithm can be interpreted as a way of exploring and exploiting the search space of the optimization problem, using the self-organizing process of the SOM algorithm . The output nodes form a set of candidate solutions that converge to the optimal solution or a near-optimal solution .
- The SOMO algorithm can also be regarded as a model of social influence and social learning, where the output nodes represent individuals or agents, and the input vector represents a stimulus or a situation . The BON represents the most influential or successful agent, and the other agents update their behaviors or strategies according to the BON .