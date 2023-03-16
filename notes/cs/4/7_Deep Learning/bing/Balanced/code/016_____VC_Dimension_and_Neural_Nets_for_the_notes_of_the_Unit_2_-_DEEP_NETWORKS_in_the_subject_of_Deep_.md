### VC Dimension and Neural Nets

- VC dimension is a measure of the complexity or expressive power of a learning model. It is defined as the maximum number of points that can be shattered (classified in all possible ways) by the model.
- Neural nets are learning models that consist of layers of nodes connected by weights, where each node computes a function of its input, called the activation function.
- The VC dimension of a neural net depends on the number of nodes, the number of edges, and the activation function used in the network .
- The VC dimension formula for neural nets ranges from O(E) to O(E^2), with O(E^2 V^2) in the worst case, where E is the number of edges and V is the number of nodes .
- The number of training samples needed to have a strong guarantee of generalization is linear with the VC dimension.
- Neural nets with superlinear VC dimension can be constructed by using nonlinear activation functions and exploiting symmetries in the network structure.
- The VC dimension of graph and recursive neural nets, which are neural nets that can process structured data, can be bounded by the number of parameters and the depth of the network.