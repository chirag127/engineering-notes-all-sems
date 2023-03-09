 Here is the content in markdown format for the topic ### activation functions for the notes of the Unit 1 - Neural Networks-I (Introduction & Architecture) in the subject of Application of Soft Computing:

#### Activation Functions

- An activation function is a function that is applied at each node of a neural network to introduce non-linearity. It determines the output of a neuron given an input or set of inputs.
- The most commonly used activation functions are:
    - Sigmoid: `σ(x) = 1 / (1 + e^-x)`
        - Output is bounded between 0 and 1
        - Differentiable everywhere
        - Vanishing gradient problem
    - Tanh: `tanh(x) = (e^x - e^-x) / (e^x + e^-x)`
        - Output is bounded between -1 and 1
        - Differentiable everywhere
        - Vanishing gradient problem
    - ReLU: `f(x) = max(0, x)`
        - Output is unbounded
        - Not differentiable at x = 0
        - Does not have the vanishing gradient problem
    - Leaky ReLU: `f(x) = max(0.01x, x)`
        - Overcomes the dead ReLU problem
        - Output is unbounded

- The choice of activation function depends on the problem and the network architecture. ReLU and its variants are most commonly used in modern deep networks due to their non-vanishing gradient property and computational efficiency.

- [Diagrams/Images/Codes/Examples/Applications...]

- The notes are formatted in markdown with headings and points for easy reading and reference for exams. Formal tone is maintained throughout. Please let me know if you would like me to elaborate on any part or modify the content.