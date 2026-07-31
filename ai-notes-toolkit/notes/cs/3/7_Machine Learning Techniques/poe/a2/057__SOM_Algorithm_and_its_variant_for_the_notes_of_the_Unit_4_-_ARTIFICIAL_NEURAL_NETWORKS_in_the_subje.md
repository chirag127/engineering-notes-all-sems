 Here is the content in markdown format without any emojis or external links, written in points and in a formal tone:

### SOM Algorithm and its variant for the notes of the Unit 4 - ARTIFICIAL NEURAL NETWORKS in the subject of Machine Learning Techniques

1. Self-Organizing Map (SOM) is a type of artificial neural network that is trained using unsupervised learning to produce a low-dimensional, discretized representation of the input space of the training samples, called a map.

2. SOM converts complex, nonlinear statistical relationships in high-dimensional data into simple geometric relationships on a low-dimensional display.

3. The key steps in SOM are:

(a) Initialize the weights of the neurons randomly
(b) Select a random input vector from the input data
(c) Determine the winning neuron i.e. the neuron whose weight vector is closest to the input vector
(d) Update the weights of the winning neuron and its neighboring neurons
(e) Repeat steps #2 through #4 until convergence is reached

4. After training, input vectors that are nearby in the high-dimensional input space produce activation in nearby neurons on the map. This results in a topology-preserving mapping that can be useful for visualization.

5. Some variants of SOM are:

(a) Growing SOM: Starts with a small map size and grows dynamically.
(b) Gradient SOM: Uses a gradient-descent based approach to updating neuron weights.
(c) Batch SOM: Processes input vectors in batches rather than individually.
(d) Encoder SOM: The map dimensions are specified and a decoding mechanism is used to estimate input vectors from map responses.