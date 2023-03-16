## Unit 2 - DEEP NETWORKS

- A deep network is an artificial neural network with multiple layers between the input and output layers.
- A layer is a set of units (also called neurons) that perform some computation on the input data and produce some output data.
- A unit is a simple mathematical function that takes one or more inputs and produces one output. The output is usually a non-linear transformation of the weighted sum of the inputs plus a bias term.
- A weight is a numerical value that determines how much influence an input has on the output of a unit. A bias is a constant term that shifts the output of a unit.
- A deep network can learn complex non-linear relationships between the input and output data by adjusting the weights and biases of the units through a process called gradient descent.
- Gradient descent is an optimization algorithm that iteratively updates the weights and biases of the units by moving them in the opposite direction of the gradient of a loss function. The loss function measures how well the network predicts the output data given the input data.
- A deep network can have different types of layers and units, depending on the task and the data. Some common types of layers are:
  - Dense layer: a layer where each unit is connected to all the units in the previous layer and the next layer.
  - Convolutional layer: a layer where each unit is connected to a local region of the units in the previous layer, and applies a convolution operation to extract features from the input data.
  - Pooling layer: a layer that reduces the size of the input data by applying a pooling operation, such as max, average, or sum, to each region of the input data.
  - Recurrent layer: a layer that has a feedback loop that allows the units to store and access information from previous time steps, useful for sequential data such as text or speech.
  - Attention layer: a layer that learns to focus on the most relevant parts of the input data, useful for tasks such as machine translation or image captioning.