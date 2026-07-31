# SOM Algorithm and its variant

- SOM stands for Self-Organizing Map, which is a type of artificial neural network that can perform unsupervised learning and dimensionality reduction  .
- SOM consists of two layers: an input layer and an output layer. The input layer receives high-dimensional data, and the output layer consists of a grid of nodes, each with a weight vector of the same dimension as the input data .
- The learning process of SOM involves four steps: initialization, competition, cooperation, and adaptation .
  - Initialization: The weight vectors of the output nodes are randomly assigned or sampled from the input data .
  - Competition: For each input data, the output node that has the most similar weight vector to the input data is selected as the winner or the best matching unit (BMU) .
  - Cooperation: The winner node and its neighboring nodes on the grid are updated to become more similar to the input data. The degree of similarity depends on the distance from the winner node and a learning rate parameter .
  - Adaptation: The learning rate and the neighborhood size are gradually decreased over time to fine-tune the weight vectors .
- The result of SOM is a low-dimensional representation of the input data that preserves the topological features of the original data. The output nodes can be visualized as a map that shows the clusters and patterns of the input data  .
- A variant of the SOM algorithm is the SOM-based optimization (SOMO) algorithm, which was proposed by Su and Zhao   . The SOMO algorithm can be used to solve continuous optimization problems by exploring and exploiting good solutions through the self-organizing process   .
- The SOMO algorithm differs from the conventional SOM algorithm in the following aspects   :
  - The input data are randomly generated within the feasible region of the optimization problem, and the objective function value of each input data is used as the similarity measure for the competition step   .
  - The cooperation step is modified to update the weight vectors of the output nodes according to the gradient information of the objective function   .
  - The adaptation step is modified to adjust the learning rate and the neighborhood size based on the improvement of the objective function value   .
- The SOMO algorithm can be interpreted as a model of social influence and social learning, where the output nodes represent individuals or agents, and the input data represent external stimuli or information sources   .
- The SOMO algorithm has been shown to be effective in solving some benchmark optimization problems and real-world applications   .