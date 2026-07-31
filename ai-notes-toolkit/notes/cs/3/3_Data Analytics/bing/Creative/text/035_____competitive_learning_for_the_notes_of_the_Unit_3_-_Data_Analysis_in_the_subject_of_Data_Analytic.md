### Competitive Learning

- Competitive learning is a form of **unsupervised learning** in artificial neural networks, in which nodes compete for the right to respond to a subset of the input data .
- Competitive learning is a variant of **Hebbian learning**, which is based on the principle that neurons that fire together wire together.
- Competitive learning works by increasing the **specialization** of each node in the network, so that different nodes become sensitive to different patterns or features in the data .
- Competitive learning is usually implemented with neural networks that contain a hidden layer which is commonly known as the **competitive layer**.
- Every competitive neuron is described by a **vector of weights** and calculates the **similarity measure** between the input data and the weight vector.
- The competitive neuron with the highest similarity measure is declared the **winner** and its weight vector is updated to become more similar to the input data. This is known as the **winner-takes-all** rule .
- The competitive learning algorithm can be summarized as follows:

  - Initialize the weight vectors of the competitive neurons randomly.
  - Present an input data to the network and calculate the similarity measure for each competitive neuron.
  - Find the winner neuron with the highest similarity measure and update its weight vector according to a learning rule, such as:

    - `w_new = w_old + alpha * (x - w_old)`, where `w` is the weight vector, `x` is the input data, and `alpha` is the learning rate.
  - Repeat steps 2 and 3 until convergence or a predefined number of iterations.

- Competitive learning is well suited to finding **clusters** within data, as the competitive neurons tend to form a **codebook** of representative vectors for the input data distribution .
- Competitive learning can also be used for **dimensionality reduction**, **feature extraction**, **data compression**, **pattern recognition**, and **self-organization**.
- Some examples of competitive learning models are:

  - **K-means clustering**, which partitions the data into k clusters by minimizing the sum of squared distances between each data point and its nearest cluster center.
  - **Learning vector quantization (LVQ)**, which is a supervised extension of competitive learning that assigns class labels to the competitive neurons and adjusts the weight vectors based on the correctness of the classification.
  - **Self-organizing map (SOM)**, which is a two-dimensional grid of competitive neurons that preserves the topological structure of the input data and forms a low-dimensional representation of the high-dimensional data.
  - **Adaptive resonance theory (ART)**, which is a family of competitive learning models that can handle both stable and dynamic data by incorporating a vigilance parameter that controls the degree of similarity required for a neuron to be activated.