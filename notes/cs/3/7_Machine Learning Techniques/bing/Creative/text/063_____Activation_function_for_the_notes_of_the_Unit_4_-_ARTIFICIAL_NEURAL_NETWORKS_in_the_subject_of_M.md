### Activation function for the notes of the Unit 4 - ARTIFICIAL NEURAL NETWORKS in the subject of Machine Learning Techniques

- An activation function is a function used in artificial neural networks which outputs a small value for small inputs, and a larger value if its inputs exceed a threshold.
- The purpose of the activation function is to introduce non-linearity into the output of a neuron, which enables a neural network to learn complex patterns and perform various tasks .
- Some common types of activation functions are:
  - Logistic or sigmoid function: It maps the input to a value between 0 and 1, and is often used for binary classification or probability estimation .
  - Hyperbolic tangent or tanh function: It maps the input to a value between -1 and 1, and is similar to the sigmoid function but with a zero-centered output .
  - Rectified linear unit or ReLU function: It outputs the input if it is positive, and zero otherwise. It is a simple and fast activation function that can overcome the vanishing gradient problem .
  - Leaky ReLU function: It outputs the input if it is positive, and a small fraction of the input if it is negative. It is a variation of the ReLU function that avoids the dying ReLU problem .
  - Exponential linear unit or ELU function: It outputs the input if it is positive, and a scaled exponential function of the input if it is negative. It is another variation of the ReLU function that can speed up the learning process .
  - Softmax function: It outputs a vector of values between 0 and 1 that sum up to 1, and is often used for multi-class classification or probability distribution .
- The choice of activation function depends on the type and complexity of the problem, the architecture and size of the network, and the computational efficiency and stability of the function .
- Some activation functions, such as logistic and ReLU, have been used for many decades, while others, such as ELU and softmax, have been developed more recently .
- Activation functions shape the outputs of artificial neurons and, therefore, are integral parts of neural networks in general and deep learning in particular.