### VC Dimension and Neural Nets

- The Vapnik–Chervonenkis (VC) dimension is a measure of the capacity of a statistical classification algorithm, defined as the cardinality of the largest set of points that the algorithm can shatter.
- The VC-dimension formula for neural networks ranges from O(E) to O(E^2), with O(E^2V^2) in the worst case, where E is the number of edges and V is the number of nodes.
- The number of training samples needed to have a strong guarantee of generalization is linear with the VC-dimension.
- The VC-dimension of a feedforward neural net with linear threshold gates is at most O(w · log w), where w is the total number of weights in the neural net.
- The VC-dimension of a machine learning architecture is defined as the largest number of examples that can be shattered by the model.
- The VC-dim is useful in machine learning because it defines a probabilistic upper bound on the generalization error achieved on the testing dataset by a trained model.
- If the activation function is the sign function and the weights are general, then the VC dimension is at most O(w · log w).
- If the activation function is the sigmoid function and the weights are general, then the VC dimension is at least O(w) and at most O(w · log w).
